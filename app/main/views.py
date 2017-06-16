# -*- coding: utf-8 -*-
from datetime import datetime
from flask import render_template, session, redirect, url_for, request
from app.models import HomePageData
from app.databaseBack.homePageManagement import HomePageManagement
from app.databaseBack.userManagement import UserManagement
from flask_login import login_user, logout_user, current_user, login_required

from app.spider.Ver2 import spider
from . import main
from .. import db
import json


@main.route('/main_page_data')
def main_page_data():
    return HomePageManagement.get_homepage()


@main.route('/')
@main.route('/index', methods=['GET', 'POST'])
def index():
    if request.args.get('sousuo')  is not None:
        print request.args.get('sousuo')
        return main.send_static_file('search_result.html')
    elif current_user.is_authenticated:
        return main.send_static_file('home_page_after_login.html')
    else:
        return main.send_static_file('main_page_before_login.html')


@main.route('/init')
def init():
    HomePageManagement.init_homepage()


@main.route('/upgrade')
def upgrade():
    HomePageManagement.upgrade()


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return main.send_static_file('login.html')
    username = request.form.get('yonghuming')
    password = request.form.get('mima')

    user = UserManagement.login(username, password)
    if user is not None:
        login_user(user, request.form.get('rememberMe'))
        print current_user.username
        return redirect(request.args.get('next') or url_for('main.index'))
    return redirect(url_for('main.login'))


@main.route('/register', methods=['GET', 'POST'])
def register():
    username = request.form.get('yonghuming')
    password = request.form.get('mima')
    password1 = request.form.get('mima1')
    if password != password1:
        print 'passwd f', password, password1
        return main.send_static_file('register.html')
    if UserManagement.has_user(username):
        print 'user exist'
        return main.send_static_file('register.html')
    if UserManagement.register(username, password):
        print 'registe!'
        print username, password
        return redirect(url_for('main.login'))
    return 'ffffff'


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/information')
@login_required
def information():
    main.send_static_file('information.html')