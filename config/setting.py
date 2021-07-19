#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Administrator'

import os,sys

from public.common import GetYaml

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# 配置文件
CONFIG_DIR = os.path.join(BASE_DIR,"database","user.ini")
# 测试用例目录
TEST_DIR = os.path.join(BASE_DIR,"testcase")
# 测试报告目录
TEST_REPORT = os.path.join(BASE_DIR,"report")
# 测试JSON报告
TEST_REPORT_JSON = os.path.join(TEST_REPORT,"result")
# 测试HTML报告
TEST_REPORT_HTML = os.path.join(TEST_REPORT,"html")
# 日志目录
LOG_DIR = os.path.join(BASE_DIR,"logs")
# 测试数据文件
TEST_DATA_YAML = os.path.join(BASE_DIR,"testdata")
# 元素控件
TEST_Element_YAML = os.path.join(BASE_DIR,"testyaml")

''''解析yaml页面元素文件'''
ele_百度首页 = GetYaml.getyaml(TEST_Element_YAML + r"/login_ele.yaml")


# 浏览器驱动目录
DRIVER_DIR = os.path.join(BASE_DIR,"driver")

'''全局变量'''
wait_time = 2
url="http://www.baidu.com"
username="xxxxxx"
password="xxxxxx"

'''Email设置'''
email_address="smtp.163.com.cn"
email_user="Jason"
email_pwd="xxxxx"



