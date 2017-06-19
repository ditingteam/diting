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
from app.databaseBack.videoManagement import VideoManagement
from app.models import Comment, VideoLink


class CommentManagement(object):
    @classmethod
    def get_comment(cls, video_name, episode):
        '''
        获得某个视频的评论的json数据
        :param video_name: 视频名称
        :param episode: 视频集数
        :return: 对应视频的所有评论
        '''
        video_link = VideoManagement.get_video_link(video_name, episode)
        video_link_id = VideoLink.query.filtry_by(link=video_link).first().id
        comments = Comment.query.filter_by(Uid = video_link_id).all()
        return json.dumps(comments, ensure_ascii=False)

    @classmethod
    def add_comment(cls, username, video_name, episode, comment):
        '''
        增加某用户对某视频的评论
        :param username: 用户名
        :param video_name: 电视剧名
        :param episode: 集数
        :param comment: 用户的评论
        :return: 无
        '''
        video_link = VideoManagement.get_video_link(video_name, episode)
        user_id = UserManagement.get_user_id(username)
        video_link_id = VideoLink.query.filtry_by(link = video_link).first().id
        new_comment = Comment(Uno = user_id, Uid = video_link_id, comment_text = comment)
        db.session.add(new_comment)
        db.session.commit()

    @classmethod
    def delete_commit(cls, username, video_name, episode):
        '''
        删除某人对视频的评论
        :param username: 用户名
        :param video_name: 视频名称
        :param episode: 集数
        :return: 无
        '''
        video_link = VideoManagement.get_video_link(video_name, episode)
        user_id = UserManagement.get_user_id(username)
        video_link_id = VideoLink.query.filtry_by(link = video_link).first().id
        db.session.query(Comment).filter(Comment.Uid==video_link_id, Comment.Uno==user_id).delete()
        db.session.commit()