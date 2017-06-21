# -*- coding :utf-8 -*-
import unittest
from app import db
from app.databaseBack import commentManagement
from app.databaseBack.userManagement import UserManagement


class CommentManagementTest(unittest.TestCase):
    def setUp(self):
        db.create_all()
        UserManagement.register('xiaochao','0000000')
        commentManagement.add_comment('xiaochao','http://player.youku.com/player.php/sid/XMjgwNjYyNjEwMA==/v.swf','智障电视剧')
        super(CommentManagementTest, self).setUp()


    def tearDown(self):
        super(CommentManagementTest, self).tearDown()
        db.drop_all()
    def test_get_comment(self):
        self.assertIsNotNone(commentManagement.get_comment('http://player.youku.com/player.php/sid/XMjgwNjYyNjEwMA==/v.swf'))



