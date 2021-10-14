#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'GuQiao'

import os,sys
import pytest_html
import pytest
from selenium.webdriver.common.by import By

from public.common import Browser

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import setting
from public.common.log import Log

class Test_demo:

    # def __init__(self):
    #     self.driver = Browser.driver
    #     self.logging = Log()

    def test_demo_01(self):
        Browser.browser().open_browser("https://b2b4tcsdev-plmcomm.cs19.force.com/MarketPlace/SpHomePagee")
        print("\n----------------------------Demo----------------------------")
        self.driver.implicitly_wait(5)
        self.logging.info("输入搜索内容")
        # self.driver.find_element(By.XPATH, setting.ele_百度首页['搜索框']['element']).send_keys("AIRTEST")
        # self.logging.info("点击 百度一下 按钮")
        # self.driver.find_element(By.XPATH, setting.ele_百度首页['百度一下按钮']['element']).click