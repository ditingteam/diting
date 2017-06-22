# -*- coding: utf-8 -*-
from datetime import datetime
from flask import render_template, session, redirect, url_for, request

from app.databaseBack.commentManagement import CommentManagement
from app.databaseBack.historyManagement import HistoryManagement
from app.databaseBack.homePageManagement import HomePageManagement
from app.databaseBack.userManagement import UserManagement
from flask_login import login_user, logout_user, current_user, login_required

from app.databaseBack.videoManagement import VideoManagement
from . import main


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
        print (username, password)
        return redirect(url_for('main.login'))


@login_required
@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@login_required
@main.route('/information')
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
    new_password1 = request.form.get('mima1')
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
    else:
        nickname = request.form.get('nickname')
        sex_data = request.form.get('sex')
        p_sign = request.form.get('p_sign')
        birth = request.form.get('birthday')
        phone = request.form.get('phone')
        email = request.form.get('email')
        address = request.form.get('address')
        introduce = request.form.get('introduce')
        sex = True if sex_data == 'male' else False
        UserManagement.change_information(current_user.username, nickname, sex, p_sign,
                                          birth, phone, email, address, introduce)
        print ('change!',nickname)
        return redirect(url_for('main.index'))


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
        return main.send_static_file('search_result_after_login.html')
    else:
        return main.send_static_file('search_result_before_login.html')

@login_required
@main.route('/get_information')
def get_information():
    return UserManagement.get_information(current_user.username)

@main.route('/video_play_homepage')
def video_play_homepage():
    if current_user.is_authenticated:
        return main.send_static_file('play_home_video_after_login.html')
    else:
        return main.send_static_file('play_home_video_before_login.html')

@main.route('/video_play')
def video_play():
    if current_user.is_authenticated:
        video_link = request.args.get('playAddress')
        print ("add")
        HistoryManagement.add_history(current_user.username, video_link)
        return main.send_static_file('play_video_after_login.html')
    else:
        return main.send_static_file('play_video_before_login.html')

@main.route('/add_comment')
def add_comment():
    video_link = request.args.get('playAddress')
    username = current_user.username
    comment = request.args.get('comment')
    CommentManagement.add_comment(username, video_link, comment)
    return CommentManagement.get_comment(video_link)


@main.route('/get_comment')
def get_comment():
    video_link = request.args.get('playAddress')
    return CommentManagement.get_comment(video_link)

@main.route('/delete_comment')
def delete_comment():
    username = request.args.get('username')
    video_link = request.args.get('playAddress')
    comment_time = request.args.get('comment_time')
    CommentManagement.delete_commit(username, video_link, comment_time)
