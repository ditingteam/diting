from app import db
from app.models import User

class UserManagement(object):
    @staticmethod
    def has_user(username):
        user = User.query.filter_by(username=username).first()
        return True if user is not None else False

    @staticmethod
    def register(username, password):
        '''
        only when the user exist return false
        :param username:
        :param password:
        :return:
        '''
        if not UserManagement.has_user(username):
            user = User(username =username, password=password)
            db.session.add(user)
            db.session.commit()
            return True
        else:
            return False

    @staticmethod
    def login(username, password):
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

    @staticmethod
    def get_user(username):
        return User.query.filter_by(username=username).first()
