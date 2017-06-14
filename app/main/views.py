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
    my_spider = spider()
    return json.dumps(my_spider.get_data(), ensure_ascii=False)

@main.route('/')
@main.route('/index')
def index():
    return main.send_static_file('index.html')

@main.route('/BigStarXu')
def nb():
    # HomePageManagement.init_homepage()
    HomePageManagement.upgrade()
    return HomePageManagement().get_homepage()