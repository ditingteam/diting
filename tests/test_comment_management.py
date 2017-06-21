# -*- coding: utf-8 -*-
import unittest
from app import db
from app.databaseBack import commentManagement
from app.databaseBack.commentManagement import CommentManagement
from app.databaseBack.historyManagement import HistoryManagement
from app.databaseBack.userManagement import UserManagement
from app.models import User, SuperDrama, HotList, PeakViewingTime, Video, Comment, VideoLink, History



class CommentManagementTest(unittest.TestCase):


    def test_get_comment(self):
        CommentManagement.add_comment('xiaochao', 'http://player.youku.com/player.php/sid/XMjY3NzU2MTA2MA==/v.swf', '666')
        self.assertIsNotNone(CommentManagement.get_comment('http://player.youku.com/player.php/sid/XMjY3NzU2MTA2MA==/v.swf'))



