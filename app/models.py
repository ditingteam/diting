# -*- coding: utf-8 -*-
from app import db
from flask_login import UserMixin
from app.spider.Ver2 import spider
from datetime import *

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64),unique = True, index = True)
    username = db.Column(db.String(64), unique = True)
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default = False)

class SuperDrama(db.Model):
    __tablename__ = 'super_drama'
    Sid = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    Sinfo = db.Column(db.String(64))
    Slink = db.Column(db.String(100))
    Simg = db.Column(db.String(100))
    Stitle = db.Column(db.String(50))
    Stime = db.Column(db.DateTime, default=datetime.now())

    def update_data(self):

        my_spider = spider()
        all_data = my_spider.get_data()
        data = all_data.get(u'超级网剧')
        for juji in data:
            self.Sinfo = juji.get('info')

class NewDramaTrailer(db.Model):
    __tablename__ = 'new_drama_trailer'
    Nid = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    Ninfo = db.Column(db.String(64))
    Nlink = db.Column(db.String(100))
    Nimg = db.Column(db.String(100))
    Ntitle = db.Column(db.String(50))

class HotList(db.Model):
    __tablename__ = 'Hotlist'
    Hid = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    Hpaly_times = db.Column(db.String(64))
    Hlink = db.Column(db.String(100))
    Hlabel = db.Column(db.String(100))
    Hname = db.Column(db.String(50))

class ExclusiveVideoWebsite(db.Model):
    __tablename__ = 'Exclusive_video_website'
    Eid = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    Einfo = db.Column(db.String(64))
    Elink = db.Column(db.String(100))
    Eimg = db.Column(db.String(100))
    Etitle = db.Column(db.String(50))


class ExclusivePlanning(db.Model):
    __tablename__ = 'Exclusiveplanning'
    Eid = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    Einfo = db.Column(db.String(64))
    Elink = db.Column(db.String(100))
    Eimg = db.Column(db.String(100))
    Etitle = db.Column(db.String(50))


class PeakViewingTime(db.Model):
    __tablename__ = 'peakviewingtime'
    Pid = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    Pinfo = db.Column(db.String(64))
    Plink = db.Column(db.String(100))
    Pimg = db.Column(db.String(100))
    Ptitle = db.Column(db.String(50))


class HomePageData(object):
    @staticmethod
    def BigStarXu():
        from datetime import datetime, timedelta

        NOW = datetime.utcnow()
        count = SuperDrama.query.filter(
            SuperDrama.Stime.between(NOW - timedelta(seconds=12* 3600 - 1), NOW - timedelta(hours=0))).all()
        drama = SuperDrama(Sid=0, Sinfo='')
        db.session.add(drama)
        db.session.commit()
        if len(count) == 0:
            return '666'

if __name__ == '__main__':
    HomePageData.BigStarXu()
