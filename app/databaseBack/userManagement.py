# -*- coding:utf8 -*-
import json

from app import db
from app.models import User
from datetime import *





class UserManagement(object):
    @classmethod
    def has_user(cls, username):
        '''
        检查数据库是否存在此用户
        :param username:
        :return:
        '''
        user = UserManagement.get_user(username)
        return True if user is not None else False

    @classmethod
    def register(cls, username, password):
        '''
        注册函数
        :param username:
        :param password:
        :return:
        '''
        if not UserManagement.has_user(username):
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return True
        else:
            return False

    @classmethod
    def login(cls, username, password):
        '''
        登录函数
        :param username:
        :param password:
        :return: user or None
        '''
        user = UserManagement.get_user(username)
        if user is not None:
            if user.verify_password(password):
                return user
            else:
                return None
        else:
            return None

    @classmethod
    def get_user(cls, username):
        '''
        根据用户名获取用户实体
        :param username:
        :return:
        '''
        return User.query.filter_by(username=username).first()

    @classmethod
    def change_password(cls, username, old_password, password):
        '''
        修改密码
        :param username:
        :param old_password:
        :param password:
        :return:
        '''
        user = UserManagement.get_user(username)
        if user.verify_password(old_password):
            user.reset_password(password)
            return True
        else:
            return False

    @classmethod
    def get_user_id(cls, username):
        return UserManagement.get_user(username).id

    @classmethod
    def change_information(cls, username, nickname, sex, p_sign, birthday, phone, email, address, introduce):
        '''
        根据给定的信息修改个人信息
        :param username:
        :param nickname:
        :param sex:
        :param p_sign:
        :param birthday:
        :param phone:
        :param email:
        :param address:
        :param introduce:
        :return:
        '''
        user = cls.get_user(username)
        user.nickname = nickname
        user.sex = sex
        user.p_sign = p_sign
        user.birth = birthday
        user.tel = phone
        user.email = email
        user.place = address
        user.introduce = introduce
        db.session.add(user)
        db.session.commit()

    @classmethod
    def default1(cls, obj):
        '''
        时间格式化工具函数
        不需要写测试
        :param obj:
        :return:
        '''
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            raise TypeError('%r is not JSON serializable' % obj)
    @classmethod
    def get_information(cls, username):
        '''
        获取个人信息
        :param username:
        :return:json格式的个人信息
        '''
        user = cls.get_user(username)
        information = {}
        information['username'] = user.username
        information['nickname'] = user.nickname
        information['sex'] = 'male' if user.sex else 'female'
        information['p_sign'] = user.p_sign
        information['birth'] = user.birth
        information['phone'] = user.tel
        information['email'] = user.email
        information['address'] = user.place
        information['introduce'] = user.introduce
        information['register_time'] = user.register_time
        from app.databaseBack.historyManagement import HistoryManagement
        information['history'] = HistoryManagement.get_user_history(username)
        return json.dumps(information, ensure_ascii=False, default=UserManagement.default1)

    @classmethod
    def get_user_name(cls, user_id):
        return User.query.filter_by(id=user_id).first().username