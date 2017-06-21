# -*- coding: utf8 -*-
import unittest
from app import db
from app.databaseBack import historyManagement
from app.databaseBack.historyManagement import HistoryManagement

from app.databaseBack.userManagement import UserManagement
from app.models import User, SuperDrama, HotList, PeakViewingTime, Video, Comment, VideoLink, History



class HistoryManagementTest(unittest.TestCase):


    def test_get_user_history(self):
        self.assertIsNotNone(HistoryManagement.get_user_history('xiaochao'))

    def test_a_get_history(self):
        user_id = User.query.filter_by(username='xiaochao').first().id
        video_link_id = VideoLink.query.filter_by(link='http://player.youku.com/player.php/sid/XMjY3NzU2MTA2MA==/v.swf').first().id
        self.assertIsNotNone(HistoryManagement.get_history(user_id, video_link_id))

