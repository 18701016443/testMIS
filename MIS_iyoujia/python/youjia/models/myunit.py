#!/usr/bin/env python3
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/19 11:20
"""
import unittest

from models.driver import browser


class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = browser()
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()

    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = browser()
    #     cls.driver.maximize_window()
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()


