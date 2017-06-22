# -*- coding :utf-8 -*-
import unittest
from app import db
from app.databaseBack.homePageManagement import HomePageManagement
from app.models import User, SuperDrama, HotList, PeakViewingTime, Video, Comment, VideoLink, History



class HomePageManagementTest(unittest.TestCase):


    def test_get_homepage(self):
        self.assertIsNotNone(HomePageManagement.get_homepage())

