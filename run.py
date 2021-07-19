#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'GUQIAO248'

import os,sys
import pytest

sys.path.append(os.path.dirname(__file__))
from config import setting

# 测试报告存放文件夹，如不存在，则自动创建一个report目录
if not os.path.exists(setting.TEST_REPORT):os.makedirs(setting.TEST_REPORT + '/' + "screenshot")

if __name__ =="__main__":
    pytest.main(['-s','-q','--alluredir',setting.TEST_REPORT_JSON])
    commond = 'allure generate ' + setting.TEST_REPORT_JSON + ' -o ' + setting.TEST_REPORT_HTML + ' --clean'
    os.system(commond)