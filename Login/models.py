from flask import Flask
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from Login import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # id主键
    username = db.Column(db.String(20))  # 用户名
    mail = db.Column(db.String(64))  #邮箱
    password = db.Column(db.String(128))  # 密码

