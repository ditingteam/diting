# -*- coding: utf8 -*-
import unittest
from app import db
from app.databaseBack import historyManagement

from app.databaseBack.userManagement import UserManagement
from app.models import User, SuperDrama, HotList, PeakViewingTime, Video, Comment, VideoLink, History



class HistoryManagementTest(unittest.TestCase):
    def setUp(self):
        db.create_all()
        UserManagement.register('xiaochao', 'a000000')
        video = Video(Uname="测试",id=10)
        db.session.add(video)
        videoLink = VideoLink(Vid=10, link='http://player.youku.com/player.php/sid/XMjgwNjYyNjEwMA==/v.swf')
        historyManagement.add_history('xiaochao','http://player.youku.com/player.php/sid/XMjgwNjYyNjEwMA==/v.swf')
        super(HistoryManagementTest, self).setUp()


    def tearDown(self):
        super(HistoryManagementTest, self).tearDown()
        db.drop_all()

    def test_get_user_history(self):
        self.assertIsNotNone(historyManagement.get_user_management('xiaochao',historyManagement.get_history('xiaochao')))

    def test_a_get_history(self):
        self.assertIsNotNone(historyManagement.get_history('xiaochao'))

