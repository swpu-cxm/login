from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField  # 导入表单字段
from wtforms.validators import DataRequired, Length, email  # 导入表单验证


class LoginForm(FlaskForm):  # 继承FlaskForm
    username = StringField('username', render_kw={'class': 'form-control', 'placeholder': 'Username/Email'},
                           validators=[DataRequired(), Length(1, 20)])  # 用户名,必填,render_kw可以设置其他的标签属性
    password = PasswordField('password', render_kw={'class': 'form-control', 'placeholder': 'Password'},
                             validators=[DataRequired(), Length(1, 20)])  # 密码输入框
    submit = SubmitField(render_kw={'class': 'form-control btn-info', 'value': '登录'})  # 表单提交按钮,可以设置value值来设置按钮的内容


class SigninForm(FlaskForm):
    username = StringField('username', render_kw={'class': 'form-control', 'placeholder': 'Username'},
                           validators=[DataRequired(), Length(1, 20)])
    mail = StringField('mail', render_kw={'class': 'form-control', 'placeholder': 'Email'},
                       validators=[DataRequired(), email()])  # 邮箱输入框并验证
    password = PasswordField('password', render_kw={'class': 'form-control', 'placeholder': 'Password'},
                             validators={DataRequired(), Length(1, 20)})
    re_password = PasswordField('password', render_kw={'class': 'form-control', 'placeholder': 'Repassword'},
                                validators={DataRequired(), Length(1, 20)})  # 验证密码
    submit = SubmitField(render_kw={'class': 'form-control btn-info', 'value': '注册'})


class ForgetForm(FlaskForm):
    method = SelectField('method', render_kw={'class': 'form-control'}, validators=[DataRequired()]
                         , choices=[(1, '邮箱'), (2, '用户名')], coerce=int)
    mail = StringField('mail', render_kw={'class': 'form-control'},validators=[DataRequired()])
    submit = SubmitField(render_kw={'class': 'form-control btn-info', 'value': '找回密码'})

class ChangeForm(FlaskForm):
    password = PasswordField('password', render_kw={'class': 'form-control', 'placeholder': 'Password'},
                             validators={DataRequired(), Length(1, 20)})
    re_password = PasswordField('password', render_kw={'class': 'form-control', 'placeholder': 'Repassword'},
                                validators={DataRequired(), Length(1, 20)})  # 验证密码
    submit = SubmitField(render_kw={'class': 'form-control btn-info', 'value': '更改密码'})
