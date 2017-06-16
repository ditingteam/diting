# -*- coding: utf-8 -*-
from datetime import datetime
from flask import render_template, session, redirect, url_for, request
from app.models import HomePageData
from app.databaseBack.homePageManagement import HomePageManagement

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
    else:
        return main.send_static_file('main_page_before_login.html')

@main.route('/BigStarXu')
def nb():
    # HomePageManagement.init_homepage()
    # HomePageManagement.upgrade()
    return HomePageManagement().get_homepage()

@main.route('/init')
def init():
    HomePageManagement.init_homepage()

@main.route('/upgrade')
def upgrade():
    HomePageManagement.upgrade()

@main.route('/login', methods=['GET', 'POST'])
def login():
    print request.form.get('mima')
    return main.send_static_file('login.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    print request.form
    return main.send_static_file('register.html')