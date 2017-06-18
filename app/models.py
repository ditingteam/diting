# -*- coding: utf-8 -*-
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app import db, login_manager
from app.spider.Ver2 import spider
from datetime import *


# Flask-Login 要求程序实现一个回调函数
# 加载用户的回调函数接收以Unicode 字符串形式表示的用户标识符。如果能找到用户，这
# 个函数必须返回用户对象；否则应该返回None。
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64),unique = True, index = True)
    username = db.Column(db.String(64), unique = True)
    password_hash = db.Column(db.String(128))
    sex = db.Column(db.Boolean)
    birth = db.Column(db.String(20))
    tel = db.Column(db.String(11))
    place = db.Column(db.String(200))
    introduce = db.Column(db.String(200))
    register_time = db.Column(db.DateTime, default=datetime.now())
    role = db.Column(db.String(1), default='g') # general 普通用户 admin 管理员（管理员用户是手动在后台添加的）

    @property
    # 只可以写，写的方法在下面，如果试图读，会返回错误
    # 这个修饰器可以简单地将方法转换为类属性，可以用.来访问的那种
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def reset_password(self, new_password):
        self.password = new_password
        db.session.add(self)
        db.session.commit()

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
    __tablename__ = 'hotlist'
    Hid = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    Hpaly_times = db.Column(db.String(64))
    Hlink = db.Column(db.String(100))
    Hlabel = db.Column(db.String(100))
    Hname = db.Column(db.String(50))

class ExclusiveVideoWebsite(db.Model):
    __tablename__ = 'exclusive_video_website'
    Eid = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    Einfo = db.Column(db.String(64))
    Elink = db.Column(db.String(100))
    Eimg = db.Column(db.String(100))
    Etitle = db.Column(db.String(50))


class ExclusivePlanning(db.Model):
    __tablename__ = 'exclusiveplanning'
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

class Video(db.Model):
    __tablename__ = 'video'
    id = db.Column(db.Integer, primary_key=True)
    Uname = db.Column(db.String(100), unique=True)
    Uimage = db.Column(db.String(100))
    Uinfo = db.Column(db.Text)

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    Uid = db.Column(db.Integer, db.ForeignKey('video_link.id'))
    Uno = db.Column(db.Integer, db.ForeignKey('users.id'))
    Hdate = db.Column(db.DateTime, default=datetime.now())
    comment_text = db.Column(db.String(200))

class VideoLink(db.Model):
    __tablename__ = 'video_link'
    id = db.Column(db.Integer, primary_key=True)
    Vid = db.Column(db.Integer, db.ForeignKey('video.id'))
    episode = db.Column(db.Integer) #集数
    link = db.Column(db.String(20), unique=True)

class History(db.Model):
    __tablename__ = 'history'
    id = db.Column(db.Integer, primary_key=True)
    Uid = db.Column(db.Integer, db.ForeignKey('video_link.id'))
    Uno = db.Column(db.Integer, db.ForeignKey('users.id'))
    Hdate = db.Column(db.DateTime, default=datetime.now())