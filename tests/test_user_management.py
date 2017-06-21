# -*- coding: utf-8 -*-
import unittest
from app import db
from app.databaseBack.userManagement import UserManagement
from app.models import User, SuperDrama, HotList, PeakViewingTime, Video, Comment, VideoLink, History



class UsermanagementTest(unittest.TestCase):


    def test_a_register(self):
        # 已经有用户xiaochao，密码是a000000
        self.assertFalse(UserManagement.register('xiaochao', 'a999999'))

    def test_b_login(self):

        self.assertIsNotNone(UserManagement.login('xiaochao', 's111111'))

    def test_c_has_user(self):
        self.assertTrue(UserManagement.has_user('xiaochao'))
        self.assertFalse(UserManagement.has_user('xiaohong'))

    def test_d_get_user(self):
        self.assertIsNotNone(UserManagement.get_user('xiaochao'))

    def test_e_change_password(self):
        self.assertTrue(UserManagement.change_password('xiaochao', 's111111','a000000'))
        self.assertIsNone(UserManagement.login('xiaochao', 's111111'))
        self.assertIsNotNone(UserManagement.login('xiaochao', 'a000000'))

    def test_f_get_information(self):
        self.assertIsNotNone(UserManagement.get_information('xiaochao'))
