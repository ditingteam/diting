# -*- coding :utf-8 -*-
import unittest
from app import db
from app.databaseBack.videoManagement import VideoManagement
from app.models import User, SuperDrama, HotList, PeakViewingTime, Video, Comment, VideoLink, History


class VideomanagementTest(unittest.TestCase):
    def setUp(self):
        super(VideomanagementTest, self).setUp()
        db.create_all()

    def tearDown(self):
        super(VideomanagementTest, self).tearDown()
        db.drop_all()

    def test_c_get_video(self):
        self.assertIsNotNone('龙珠传奇')

    def test_a_search_video(self):
        self.assertIsNotNone('龙珠传奇')

    def test_b_search_video_from_database(self):
        self.assertIsNotNone('龙珠传奇')


