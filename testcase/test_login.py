#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'GuQiao'

import os,sys
import time

import pytest_html
import pytest
import win32con
import pywin32_system32
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pywinauto import application

from public.common import Browser

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import setting
from public.common.log import Log


class TestLogin:
    
    filepath = r"C:\Product Template.xls"

    
    def upload_file(self, filepath):
        # 一级窗口
        dialog = win32gui.FindWindow("#32770", "Open")
        # 找到窗口二级元素
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
        # 三级元素
        combox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)
        # EDIT元素
        edit = win32gui.FindWindowEx(combox, 0, "Edit", None)
        # 打开按钮元素
        button = win32gui.FindWindowEx(dialog, 0, "Button", None)
        # edit 中输入文件全名称（完整路径）
        # "E:\testimg\QQ1.jpg" 设置为参数
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filepath)
        # 点击打开按钮提交
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

    def winauto(self, filepath):

        # 使用pywinauto进行上传操作
        app = application.Application()
        window = app.window_(class_name="#32770")
        # 文件所在路径不能含有空格
        window["Edit"].TypeKeys(r"C:\test.jpg")
        window["ScrollBar"].Click()
        window[u"打开(O)"].Click()

    def loginMarketPlace(self, url):
        Browser.browser().open_browser("https://b2b4tcsdev-plmcomm.cs19.force.com/MarketPlace/s/")
        print("\n----------------------------Login into MarketPlace----------------------------")
        Browser.driver.implicitly_wait(5)
        # Browser.driver.logging.info("\n----------------------------Login into MarketPlace----------------------------")
        # Browser.driver.set_window_size(1552, 848)
        Browser.driver.maximize_window()
        # WebDriverWait(Browser.driver, 30000).until(
        #     expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".btn")))
        # Browser.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        time.sleep(5)
        Browser.driver.find_element(By.ID, "username").clear()
        Browser.driver.find_element(By.ID, "username").send_keys("demouser01@yopmail.com")
        Browser.driver.find_element(By.ID, "password").clear()
        Browser.driver.find_element(By.ID, "password").send_keys("Password1")
        Browser.driver.find_element(By.ID, "submit").click()
        time.sleep(5)
        WebDriverWait(Browser.driver, 30000).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(.,\'Add New Product\')]")))
        Browser.driver.find_element(By.XPATH, "//button[contains(.,\'Add New Product\')]").click()
        Browser.driver.find_element(By.XPATH, "//span[contains(.,\'Upload Files\')]").click()

    upload = Browser.driver.find_element_by_id('file')
    time.sleep(5)
    upload.send_keys(filepath)  # send_keys
    # print(upload.get_attribute('value'))  # check value

    # # # 上传文件
    # # upload_files(file_path)
    # # 点击文件上传，弹窗出现窗口
    # # 出现弹窗窗口,使用upload 方法
    # upload_file(filepath)
    # time.sleep(2)

if __name__ == '__main__':
    pytest.main(['-vs','./test_login.py'])




