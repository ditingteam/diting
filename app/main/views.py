# -*- coding: utf-8 -*-
from datetime import datetime
from flask import render_template, session, redirect, url_for
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
@main.route('/index')
def index():
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