from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import os
from flask_mail import Message
from Login import mail
from flask import url_for
from Login.settings import BaseConfig

salt = '12345678'
t = Serializer(salt, expires_in=600)


def send_email(messgage, email, way):
    # msg = Message('验证码', sender='sendmail@mail.cxmgxj.cn', recipients=['cxm1998@vip.qq.com'])
    # msg = Message('邮箱验证码', sender='cxmpypy@163.com', recipients=['cxm1998@vip.qq.com'])
    if way == 1:
        msg = Message('邮箱验证', sender=BaseConfig.FLASKY_MAIL_SENDED, recipients=[email])
        msg.body = '邮箱验证'
        msg.html = '您正在注册,为了验证你的邮箱,请点击一下链接,如果不是本人操作,请忽略<br><a>' + url_for('confirm', confirm_url=encode_msg(messgage),
                                                                      _external=True) + '</a><br>验证码十分钟有效'
    elif way==2:
        msg = Message('找回密码', sender=BaseConfig.FLASKY_MAIL_SENDED, recipients=[email])
        msg.body = '找回密码'
        msg.html = '您正在找回密码,请点击一下链接,如果不是本人操作,请忽略<br><a>' + url_for('change', change_url=encode_msg(messgage),
                                                                      _external=True) + '</a><br>验证码十分钟有效'
    mail.send(msg)


def encode_msg(msg):
    res = t.dumps(msg)
    token = res.decode('utf-8')
    return token


def decode_msg(token):
    res = t.loads(token)
    return res

# import os
# print(os.getenv('windir'), '123')
