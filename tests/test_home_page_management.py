# -*- coding :utf-8 -*-
import unittest
from app import db
from app.databaseBack.homePageManagement import HomePageManagement


class HomePageManagementTest(unittest.TestCase):
    def setUp(self):
        super(HomePageManagementTest, self).setUp()
        db.create_all()

    def tearDown(self):
        super(HomePageManagementTest, self).tearDown()
        db.drop_all()

    def test_init_homepage(self):
        self.assertIsNotNone(self.myDatabaseBack.init_homepage)

    def test_get_homepage(self):
        self.assertIsNotNone(self.myDatabaseBack.get_homepage)

