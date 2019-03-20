from flask import Flask
# from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from Login.settings import BaseConfig
from flask_mail import Mail
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(BaseConfig)  # 导入配置
db = SQLAlchemy(app)  # 初始化SQlalchemy
mail = Mail(app)  # 初始化flask_mail
login_manager = LoginManager(app)  # 初始化Flask_login
login_manager.init_app(app)

login_manager.login_view = 'login'  # 登录页面的视图函数
login_manager.login_message_category = 'warning'  # 设置flash消息的类别
login_manager.login_message = '请先登录'  # 设置flash消息内容


