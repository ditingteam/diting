# -*- coding:utf8 -*-

import unittest
from app.spider.Ver2 import spider

class SpiderTestcase(unittest.TestCase):

    def setUp(self):
        super(SpiderTestcase, self).setUp()
        self.myspider=spider()
    def test_prime_time(self):
        self.assertIsNotNone(self.myspider.prime_time())

    def test_online_teleplay(self):
        self.assertIsNotNone(self.myspider.online_teleplay)

    def test_exclusive_planning(self):
        self.assertIsNotNone(self.myspider.exclusive_planning())


    def test_search(self):
        self.assertTrue(len(self.myspider.search(key_word='智障'.decode('utf-8')))== 0)

    def test_rank(self):
        self.assertIsNotNone(self.myspider.Rank())
    def test_get_data(self):
        self.assertIsNotNone(self.myspider.get_data())
