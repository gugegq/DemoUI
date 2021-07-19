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

    def __init__(self):
        self.driver = Browser.driver

    def test_demo_01(self):
        Browser.browser().open_browser("http://www.baidu.com")
        print("\n----------------------------Demo----------------------------")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, setting.ele_百度首页['搜索框']['element']).send_keys("AIRTEST")
        self.driver.find_element(By.XPATH, setting.ele_百度首页['百度一下按钮']['element']).click



    # def test_login(self):
    #
    #     log = Log()
    #     log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(datayaml['id'],datayaml['detail']))
    #     # 调用登录方法
    #     self.user_login_verify(datayaml['data']['phone'],datayaml['data']['password'])
    #     po = login(self.driver)
    #     if datayaml['screenshot'] == 'phone_pawd_success':
    #         log.info("检查点-> {0}".format(po.user_login_success_hint()))
    #         self.assertEqual(po.user_login_success_hint(), datayaml['check'][0], "成功登录，返回实际结果是->: {0}".format(po.user_login_success_hint()))
    #         log.info("成功登录，返回实际结果是->: {0}".format(po.user_login_success_hint()))
    #         screenshot.insert_img(self.driver, datayaml['screenshot'] + '.jpg')
    #         log.info("-----> 开始执行退出流程操作")
    #         self.exit_login_check()
    #         po_exit = login(self.driver)
    #         log.info("检查点-> 找到{0}元素,表示退出成功！".format(po_exit.exit_login_success_hint()))
    #         self.assertEqual(po_exit.exit_login_success_hint(), '注册',"退出登录，返回实际结果是->: {0}".format(po_exit.exit_login_success_hint()))
    #         log.info("退出登录，返回实际结果是->: {0}".format(po_exit.exit_login_success_hint()))
    #     else:
    #         log.info("检查点-> {0}".format(po.phone_pawd_error_hint()))
    #         self.assertEqual(po.phone_pawd_error_hint(),datayaml['check'][0] , "异常登录，返回实际结果是->: {0}".format(po.phone_pawd_error_hint()))
    #         log.info("异常登录，返回实际结果是->: {0}".format(po.phone_pawd_error_hint()))
    #         screenshot.insert_img(self.driver,datayaml['screenshot'] + '.jpg')
#
# if __name__=='__main__':
#     pytest.main(['-vs','test_demo.py'])