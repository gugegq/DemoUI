#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'GuQiao'

import time

import pytest
from selenium import webdriver

from public.common import Browser


class baseActions:

    def __init__(self):
        self.driver = Browser.driver

    def base_login(self):
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com")
        # driver.implicitly_wait(5)
        value = self.driver.title
        print(value)
        assert value in "百度一下，你就知道啊"
        time.sleep(10)