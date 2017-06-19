# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'xiaochao'
__mtime__ = '17-6-17'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

from datetime import *
from app import db
from app.databaseBack.userManagement import UserManagement
from app.databaseBack.videoManagement import VideoManagement
from app.models import History, VideoLink


class HistoryManagement(object):
    @classmethod
    def get_history(cls, user_id, video_link_id):
        return History.query.filter_by(Uid=video_link_id, Uno=user_id).first()


    @classmethod
    def add_history(cls, username, video_link):
        user_id = UserManagement.get_user_id(username)
        video_link_id = VideoLink.query.filter_by(link=video_link).first().id
        history = HistoryManagement.get_history(user_id, video_link_id)
        if history is not None:
            history.Hdate = datetime.now()
        else:
            history = History(Uno=user_id, Uid=video_link_id)

        db.session.add(history)
        db.session.commit()


    @classmethod
    def get_user_history(cls, username):
        user_id = UserManagement.get_user_id(username)
        user_history = History.query.order_by(History.Hdate).filter_by(Uno=user_id).all()
        history_all_data = []
        for history in user_history[:10]:
            history_data = {}
            history_data['video_name'] = VideoManagement
        return