# -*- coding :utf-8 -*-
import unittest
from app import db
from app.databaseBack.homePageManagement import HomePageManagement
from app.models import User, SuperDrama, HotList, PeakViewingTime, Video, Comment, VideoLink, History



class HomePageManagementTest(unittest.TestCase):
    def setUp(self):
        super(HomePageManagementTest, self).setUp()
        db.create_all()
        HomePageManagement.init_homepage()

    def tearDown(self):
        super(HomePageManagementTest, self).tearDown()
        db.drop_all()



    def test_get_homepage(self):
        self.assertIsNotNone(HomePageManagement.get_homepage())

