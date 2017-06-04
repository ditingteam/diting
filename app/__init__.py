# -*- coding: utf8 -*-
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import config

login_manager = LoginManager()
# session_protection 属性可以设为None、'basic' 或'strong'，以提
# 供不同的安全等级防止用户会话遭篡改。设为'strong' 时，Flask-Login 会记录客户端IP
# 地址和浏览器的用户代理信息，如果发现异动就登出用户。
login_manager.session_protection = 'strong'
# login_view 属性设置登录页面的端点,也就是auth/views.py中的路由
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    #导入蓝本的路由之类的信息
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix = '/user')

    return app