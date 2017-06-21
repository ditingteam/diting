# -*- coding :utf-8 -*-
import unittest
from app import db
from app.databaseBack.userManagement import UserManagement
from app.models import User, SuperDrama, HotList, PeakViewingTime, Video, Comment, VideoLink, History



class UsermanagementTest(unittest.TestCase):
    def setUp(self):
        super(UsermanagementTest, self).setUp()
        db.create_all()

    def tearDown(self):
        super(UsermanagementTest, self).tearDown()
        db.drop_all()

    def test_a_register(self):
        UserManagement.register('xiaochao', 'a000000')
        self.assertFalse(UserManagement.register('xiaochao', 'a999999'))

    def test_b_login(self):

        self.assertIsNotNone('xiaochao','a000000')

    def test_c_has_user(self):
        self.assertIsNotNone(self.myDatabaseBack.has_user)

    def test_d_get_user(self):
        self.assertIsNotNone(self.myDatabaseBack.get_user)

    def test_e_change_password(self):
        self.assertFalse(UserManagement.change_password('xiaochao', 'a000000','s111111'))

    def test_f_get_information(self):
        self.assertIsNotNone(UserManagement.get_information('xiaochao'))
