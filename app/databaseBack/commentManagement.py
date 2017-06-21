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

from app import db
from app.databaseBack.userManagement import UserManagement
from app.models import Comment, VideoLink


class CommentManagement(object):
    @classmethod
    def get_comment(cls, video_link):
        '''
        获得某个视频的评论的json数据
        :param video_link 视频链接
        :return: 对应视频的所有评论
        '''
        video_link_id = VideoLink.query.filtry_by(link=video_link).first().id
        comments = Comment.query.filter_by(Uid = video_link_id).all()
        all_data = []
        for comment in comments:
            data = {}
            user_id = comment.Uno
            username = UserManagement.get_user_name(user_id)
            data['username'] = username
            data['comment'] = comment.comment_text
            data['date'] = comment.Hdate
            all_data.append(data)

        return json.dumps(all_data, ensure_ascii=False)

    @classmethod
    def add_comment(cls, username, video_link, comment):
        '''
        增加某用户对某视频的评论
        :param username: 用户名
        :param video_link 视频链接
        :param comment: 用户的评论
        :return: 无
        '''
        user_id = UserManagement.get_user_id(username)
        video_link_id = VideoLink.query.filtry_by(link = video_link).first().id
        new_comment = Comment(Uno = user_id, Uid = video_link_id, comment_text = comment)
        db.session.add(new_comment)
        db.session.commit()

    @classmethod
    def delete_commit(cls, username, video_link):
        '''
        删除某人对视频的评论
        :param username: 用户名
        :param video_link 视频链接
        :return: 无
        '''
        user_id = UserManagement.get_user_id(username)
        video_link_id = VideoLink.query.filtry_by(link = video_link).first().id
        db.session.query(Comment).filter(Comment.Uid==video_link_id, Comment.Uno==user_id).delete()
        db.session.commit()