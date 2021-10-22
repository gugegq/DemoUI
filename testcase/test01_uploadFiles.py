#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'GuQiao'

import os, sys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pywinauto.application import Application
from public.common import Browser
# from public.base.upload_files import upload_files

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

filepath = r"D:\ProductTemplate.xls"
url_mkp = "https://b2b4tcsdev-plmcomm.cs19.force.com/MarketPlace/s/"

class testInputFiles:

    # def __init__(self):
    #     # 初始化driver
    #     Browser.driver = Browser.driver

    def loginMarketPlace(self, url):
        Browser.driver.get(url)
        print("\n----------------------------Login into MarketPlace----------------------------")
        Browser.driver.maximize_window()
        # Browser.driver.implicitly_wait(5)
        # Browser.driver.set_window_size(1552, 848)
        time.sleep(5)
        Browser.driver.find_element(By.ID, "username").clear()
        Browser.driver.find_element(By.ID, "username").send_keys("demouser01@yopmail.com")
        Browser.driver.find_element(By.ID, "password").clear()
        Browser.driver.find_element(By.ID, "password").send_keys("Password1")
        Browser.driver.find_element(By.ID, "submit").click()
        time.sleep(5)
        WebDriverWait(Browser.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(.,\'Add New Product\')]")))
        Browser.driver.find_element(By.XPATH, "//button[contains(.,\'Add New Product\')]").click()
        Browser.driver.find_element(By.XPATH, "//span[contains(.,\'Upload Files\')]").click()
        time.sleep(3) # 需要稍作等待，因为点击上传按钮到文件选择窗口打开会有延迟
        # # 方法一：标准html的input格式，直接调用send_keys方法
        # # 直接传输文件
        # WebDriverWait(Browser.driver, 30).until(
        #     expected_conditions.visibility_of_element_located((By.ID, "input-file-19")))
        # Browser.driver.find_element(By.ID, "input-file-19").send_keys(filepath)
        # 方法二：调用pywinauto第三方库，模拟windows窗口操作
        app = Application()  # 实例化Application
        time.sleep(3) # 需要稍作等待，因为点击上传按钮到文件选择窗口打开会有延迟
        # 这里用的class而没有加窗口title，主要为了保证兼容性
        app.connect(class_name='#32770')  # 根据class_name找到弹出窗口
        app["Dialog"]["Edit1"].TypeKeys(filepath)  # 在输入框中输入值
        app["Dialog"]["Button1"].click()  # 点击打开/保存按钮
        # upload_files("#32770", filepath)

        time.sleep(5)
        Browser.driver.quit()

if __name__ == '__main__':
    test = testInputFiles()
    test.loginMarketPlace(url_mkp)
    # pytest.main(['-vs','./baseLogin.py'])