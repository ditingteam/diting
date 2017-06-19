import json

from app import db
from app.models import User, History
from app.databaseBack.videoManagement import VideoManagement
from datetime import *



class UserManagement(object):
    @classmethod
    def has_user(cls, username):
        user = UserManagement.get_user(username)
        return True if user is not None else False

    @classmethod
    def register(cls, username, password):
        '''
        only when the user exist return false
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
        return User.query.filter_by(username=username).first()

    @classmethod
    def change_password(cls, username, old_password, password):
        user = UserManagement.get_user(username)
        if user.verify_password(old_password):
            user.reset_password(password)
            return True
        else:
            return False

    @classmethod
    def get_user_id(cls, username):
        return UserManagement.get_user_id(username)

    @classmethod
    def change_information(cls, username, nickname, sex, p_sign, birthday, phone, email, address, introduce):
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
    def get_information(cls, username):
        user = cls.get_user(username)
        information = {}
        information['nickname'] = user.username
        information['sex'] = 'male' if user.sex else 'female'
        information['p_sign'] = user.p_sign
        information['birth'] = user.birth
        information['phone'] = user.tel
        information['email'] = user.email
        information['address'] = user.place
        information['introduce'] = user.introduce
        return json.dumps(information, ensure_ascii=False)