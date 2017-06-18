# -*- coding: utf-8 -*-
from datetime import datetime
from flask import render_template, session, redirect, url_for, request
from app.databaseBack.homePageManagement import HomePageManagement
from app.databaseBack.userManagement import UserManagement
from flask_login import login_user, logout_user, current_user, login_required

from app.databaseBack.videoManagement import VideoManagement
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

    if current_user.is_authenticated:
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
        return redirect(request.args.get('next') or url_for('main.index'))
    return redirect(url_for('main.login'))


@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return main.send_static_file('register.html')
    username = request.form.get('yonghuming')
    password = request.form.get('mima')
    password1 = request.form.get('mima1')
    if password != password1:
        return main.send_static_file('register.html')
    if UserManagement.has_user(username):
        return main.send_static_file('register.html')
    if UserManagement.register(username, password):
        print username, password
        return redirect(url_for('main.login'))


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@main.route('/information')
@login_required
def information():
    return main.send_static_file('information.html')


@login_required
@main.route('/change_password', methods=['POST', 'GET'])
def change_password():
    if request.method == 'GET':
        return main.send_static_file('change_passwd.html')
    username = current_user.username
    old_password = request.form.get('old_password')
    new_password = request.form.get('new_password')
    new_password1 = request.form.get('new_password1')
    if new_password != new_password1:
        return main.send_static_file('change_passwd.html')
    elif UserManagement.change_password(current_user.username, old_password, new_password):
        return redirect(url_for('main.information'))
    else:
        return main.send_static_file('change_passwd.html')


@login_required
@main.route('/compile_information', methods=['POST', 'GET'])
def compile_information():
    if request.method == 'GET':
        return main.send_static_file('compile_information.html')

@main.route('/search_data')
def search_data():
    video_name = session.get('video_name')
    return VideoManagement.search_video(video_name)

@main.route('/search')
def search():
    if request.args.get('sousuo')  is not None:
        video_name = request.args.get('sousuo')
        session['video_name'] = video_name
    if current_user.is_authenticated:
        return main.send_static_file('search.html')
    else:
        return main.send_static_file('search.html')