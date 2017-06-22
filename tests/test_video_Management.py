# -*- coding: utf-8 -*-
import unittest
from app import db
from app.databaseBack.videoManagement import VideoManagement
from app.models import User, SuperDrama, HotList, PeakViewingTime, Video, Comment, VideoLink, History


class VideomanagementTest(unittest.TestCase):



    def test_a_search_video(self):
        self.assertIsNotNone(VideoManagement.search_video(u'人民的名义'))

    def test_b_search_video_from_database(self):
        self.assertIsNotNone(VideoManagement.search_video_from_database(u'人民的名义'))


