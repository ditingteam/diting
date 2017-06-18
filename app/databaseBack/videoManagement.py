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
from app import db
from app.models import Video, VideoLink
from app.spider.Ver2 import spider


class VideoManagement(object):
    @classmethod
    def get_video(cls, video_name):
        return Video.query.filter_by(Uname=video_name).first()

    @classmethod
    def save_video(cls, video):
        name = video.get('title')
        img = video.get('img')
        info = video.get('info')
        new_video = Video(Uname=name,
                          Uinfo=info,
                          Uimage=img)
        db.session.add(new_video)
        db.session.commit()
        links = video.get('links')
        VideoManagement.save_links(name, links)

    @classmethod
    def search_video(cls, video_name):
        data = VideoManagement.search_video_from_database(video_name)
        return data if data is not None else VideoManagement.search_video_from_internet(video_name)


    @classmethod
    def search_video_from_database(cls, video_name):
        videos = db.session.query(Video).filter(Video.Uname.like(video_name)).all()

        pass

    @classmethod
    def search_video_from_internet(cls, video_name):
        data = VideoManagement.get_data_from_spider(video_name)
        for video in data:
            VideoManagement.save_video(video)
        return data

    @classmethod
    def get_data_from_spider(cls, video_name):
        my_spider = spider()
        return my_spider.search(video_name)

    @classmethod
    def get_video_id(cls, video_name):
        return VideoManagement.get_video(video_name).id

    @classmethod
    def save_links(cls, video_name, links):
        video_id = VideoManagement.get_video_id(video_name)
        for i in range(links):
            link = links[i]
            video_link = VideoLink(Vid=video_id,
                                   link=link,
                                   episode=i)
            db.session.add(video_link)
        db.session.commit()



