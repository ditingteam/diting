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
import json
from datetime import *
from app import db
from app.databaseBack.userManagement import UserManagement
from app.databaseBack.videoManagement import VideoManagement
from app.models import History, VideoLink, Video


class HistoryManagement(object):
    @classmethod
    def get_history(cls, user_id, video_link_id):
        '''
        根据用户id和视频链接id获取历史纪录
        :param user_id:
        :param video_link_id:
        :return:
        '''
        return History.query.filter_by(Uid=video_link_id, Uno=user_id).first()


    @classmethod
    def add_history(cls, username, video_link):
        '''
        根据用户名和视频链接增加历史记录
        :param username:
        :param video_link:
        :return:无
        '''
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
        '''
        获取某用户的历史记录
        :param username:
        :return:
        '''
        user_id = UserManagement.get_user_id(username)
        user_history = History.query.order_by(History.Hdate).filter_by(Uno=user_id).all()
        history_all_data = []
        for history in user_history[:10]:
            history_data = {}
            video_link = VideoLink.query.filter_by(id=history.Uid).first()
            video = Video.query.filter_by(id=video_link.Vid).first()
            history_data['episode'] = video_link.episode
            history_data['video_name'] = video.Uname
            history_data['link'] = video_link.link
            history_all_data.append(history_data)
        return history_all_data