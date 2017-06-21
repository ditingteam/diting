# -*- coding :utf-8 -*-
import unittest
from app import db
from app.databaseBack import historyManagement

from app.databaseBack.userManagement import UserManagement


class HistoryManagementTest(unittest.TestCase):
    def setUp(self):
        db.create_all()
        UserManagement.register('xiaochao', 'a000000')
        historyManagement.add_history('xiaochao','http://player.youku.com/player.php/sid/XMjgwNjYyNjEwMA==/v.swf')
        super(HistoryManagementTest, self).setUp()


    def tearDown(self):
        super(HistoryManagementTest, self).tearDown()
        db.drop_all()

    def test_get_user_history(self):
        self.assertIsNotNone(historyManagement.get_user_management('xiaochao',historyManagement.get_history('xiaochao')))

    def test_a_get_history(self):
        self.assertIsNotNone(historyManagement.get_history('xiaochao'))

