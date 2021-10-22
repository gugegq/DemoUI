#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'GuQiao'

import os, sys
import win32gui
import win32con
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pywinauto.application import Application
from public.common import Browser
from public.base.upload_files import upload_files

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

filepath = r"C:\ProductTemplate.xls"
url_mkp = "https://b2b4tcsdev-plmcomm.cs19.force.com/MarketPlace/s/"

class test_UP:

    def __init__(self):
        # 初始化driver
        self.driver = Browser.driver

    def loginMarketPlace(self, url):
        self.driver.get(url)
        print("\n----------------------------Login into MarketPlace----------------------------")
        self.driver.maximize_window()
        # Browser.driver.set_window_size(1552, 848)
        # WebDriverWait(Browser.driver, 30000).until(
        #     expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".btn")))
        # Browser.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "username").clear()
        self.driver.find_element(By.ID, "username").send_keys("demouser01@yopmail.com")
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "password").send_keys("Password1")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(5)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(.,\'Add New Product\')]")))
        self.driver.find_element(By.XPATH, "//button[contains(.,\'Add New Product\')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,\'Upload Files\')]").click()
        time.sleep(3)  # 需要稍作等待，因为点击上传按钮到文件选择窗口打开会有延迟

        # # 方法一：标准html的input格式，直接调用send_keys方法
        # # 直接传输文件
        # WebDriverWait(self.driver, 30).until(
        #     expected_conditions.visibility_of_element_located((By.ID, "input-file-19")))
        # self.driver.find_element(By.ID, "input-file-19").send_keys(filepath)
        # # 方法二：调用pywinauto第三方库，模拟windows窗口操作
        # app = Application()  # 实例化Application
        # # 这里用的class而没有加窗口title，主要为了保证兼容性
        # app.connect(class_name='#32770')  # 根据class_name找到弹出窗口
        # app["Dialog"]["Edit1"].TypeKeys(filepath)  # 在输入框中输入值
        # app["Dialog"]["Button1"].click()  # 点击打开/保存按钮

    def upload(filePath, browser_type="chrome"):
        '''
        windows 上传弹框已经可见，可以sleep1-2秒等待出现
        通过pywin32模块实现文件上传的操作
        :param filePath: 文件的绝对路径
        :param browser_type: 浏览器类型（默认值为chrome）
        :return:
        '''
        if browser_type.lower() == "chrome":
            title = "Open"
        elif browser_type.lower() == "firefox":
            title = "Open"
        elif browser_type.lower() == "ie":
            title = "选择要加载的文件"
        else:
            title = ""  # 这里根据其它不同浏览器类型来修改

        # 找元素
        # 一级窗口"#32770","Open"
        dialog = win32gui.FindWindow("#32770", title)
        # 向下传递
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
        # 编辑按钮
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 四级
        # 打开按钮
        button = win32gui.FindWindowEx(dialog, 0, 'Button', "&Open")  # 二级

        # 输入文件的绝对路径，点击“打开”按钮
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, filePath)  # 发送文件路径
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮

if __name__ == '__main__':
    test = test_UP()
    test.loginMarketPlace(url_mkp)
    test.upload(filepath)