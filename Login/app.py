from flask import Flask, render_template, request, flash, redirect, url_for
from Login.settings import BaseConfig
from Login.forms import SigninForm, LoginForm, ForgetForm, ChangeForm
from Login.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from Login import app, db
from sqlalchemy import or_
from Login.untils import decode_msg, encode_msg, send_email
from Login import login_manager
from flask_login import login_user,logout_user,login_required


@login_manager.user_loader
def load_user(user_id):
    """
        通过获取user对象存储到session中
    :param user_id:
    :return:
    """
    user = User.query.get(int(user_id))
    return user


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    登录页面路由,可以通过邮箱或用户名登录,登录成功后将user对象存储到浏览器中,重定向到index页面
    :return:
    """
    form = LoginForm()
    if form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter(or_(User.username == username, User.mail == username)).first()
        if not user:
            flash('用户名不存在', 'error')
        elif (username == user.username or username == user.mail) and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('用户名或密码错误!', 'error')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    """
    退出登录视图,清除浏览器中的登录缓存,重定向到index页面
    :return:
    """
    logout_user()
    return redirect(url_for('index'))


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    """
    注册页面视图,首先服务端验证两次密码是否一致,其次验证用户名,邮箱是否存在,
    最后通过邮件发送验证链接,用户点击验证链接后,注册成功
    :return:
    """
    form = SigninForm()
    if form.validate_on_submit():
        username = request.form.get('username')
        mail = request.form.get('mail')
        password = request.form.get('password')
        re_password = request.form.get('re_password')
        if password != re_password:
            flash('两次密码输入不一致', 'error')
        user_exist = User.query.filter_by(username=username).first()
        email_exist = User.query.filter_by(mail=mail).first()
        if user_exist:
            flash('用户名已存在', 'error')
        elif email_exist:
            flash('邮箱已被注册', 'error')
        else:
            password_hash = generate_password_hash(password)
            msg = {'username': username, 'mail': mail, 'password_hash': password_hash}
            send_email(messgage=msg, email=mail, way=1)
            flash('验证链接已发送至您的邮箱', 'ok')
    return render_template('signin.html', form=form)


@app.route('/confirm/<string:confirm_url>')
def confirm(confirm_url):
    """
    通过动态url获取用户验证的加密口令,若口令错误,则解码失败,解码成功后将用户信息添加进数据库中
    :param confirm_url:
    :return:
    """
    try:
        msg = decode_msg(confirm_url)
        user = User(username=msg['username'], mail=msg['mail'], password=msg['password_hash'])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    except Exception as e:
        return render_template('404.html')


@app.route('/forget', methods=['GET', 'POST'])
def forget():
    """
    忘记密码路由,可以通过用户名或者邮箱找回密码,然后发送更改密码链接至用户邮箱
    用户点击链接后即可在改密码界面更改密码
    :return:
    """
    form = ForgetForm()
    if form.validate_on_submit():
        method = request.form.get('method')
        mail = request.form.get('mail')
        user_exist = User.query.filter(or_(User.username == mail, User.mail == mail)).first()
        if user_exist:
            msg = {'username': user_exist.username, 'mail': user_exist.mail, 'password_hash': user_exist.password}
            send_email(messgage=msg,email=user_exist.mail, way=2)
            flash('验证链接已发送至您的邮箱','ok')
        else:
            flash('用户名或邮箱不存在','error')
    return render_template('forget.html',form=form)

@app.route('/change/<string:change_url>',methods=['GET', 'POST'])
def change(change_url):
    """
    更改密码路由,,首先解码动态url,成功后用户输入要更改的密码
    :param change_url:
    :return:
    """
    form = ChangeForm()
    try:
        msg = decode_msg(change_url)
        if form.validate_on_submit():
            password = request.form.get('password')
            re_password = request.form.get('re_password')
            if password != re_password:
                flash('两次密码输入不一致', 'error')
            else:
                user = User.query.filter_by(username=msg['username']).first()
                user.password = generate_password_hash(password)
                db.session.commit()
                return redirect(url_for('login'))
        return render_template('change.html',form=form)
    except Exception:
        return render_template('404.html')


@app.route('/')
def index():
    """
    首页视图,用户状态
    :return:
    """
    return render_template('login_status.html')


@app.route('/admin')
@login_required
def admin():
    """
    login_required测试,若用户为登录,则跳转到登录视图
    :return:
    """
    return render_template('login_status.html')

if __name__ == '__main__':
    app.run()
