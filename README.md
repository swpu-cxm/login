# 一个flask框架的登录模板
## 功能:
    - 用户注册,并通过flask_mail发送邮件验证邮箱
    - 忘记密码,通过用户名/邮箱找回密码
    - 登录,通过flask_login模块实现
## 如何开始:
    - 新建一个目录
    - git clone git@github.com:swpu-cxm/login.git
    - cd login
    - pienv install --dev
    - pipenv shell
    - cd Login
    - 注意,请在settings.py文件中配置你的数据库路径和SMTP邮箱服务器**\
    - flask run
    
