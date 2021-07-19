#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'GuQiao'

import allure
import pytest

from config import setting
from public.common import Browser

pytest.fixture(scope="session")
@allure.feature("调用conftest文件")
def init():

    print('\n---------------conftest文件init方法开始执行----------------------------')
    # 打开浏览器，登录系统
    Browser.browser().open_browser(setting.url)

    yield

    Browser.browser().quit_browser()
    print('----------------conftest.py文件init方法执行结束---------------------------')


