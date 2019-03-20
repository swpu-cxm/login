"""
flask app配置,
SQlalchemy路径配置
SMTP邮箱配置
"""

import pymysql


class BaseConfig():
    SECRET_KEY = 'asgmaopdjiqawnbvau'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 是否追踪对象的修改
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/test"
    # SQLALCHEMY_ECHO = True #将SQlalchemy输出为原生sql语句

    MAIL_SERVER = 'smtp.163.com'  # SMTP服务器地址
    MAIL_PORT = '25'  # SMTP端口
    MAIL_USERNAME = 'xxx@163.com'  # 你的用户名
    MAIL_PASSWORD = 'xxxxxxx'  # SMTP密码,不是
    FLASKY_MAIL_SENDED = 'cxmpypy@163.com'  # 发件人


