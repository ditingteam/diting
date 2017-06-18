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
from app.databaseBack.userManagement import UserManagement
from app.models import Comment


class CommentManagement(object):
    @classmethod
    def get_comment(cls, username):
        user_id = UserManagement.get_user_id(username)
        comments = Comment.query.filter_by(Uno=user_id).all()
        return comments

    @classmethod
    def add_comment(cls, username, video_link):
        # todo add comment
        pass