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
        return main.send_static_file('serch_result.html')
    else:
        return main.send_static_file('index.html')

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