#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'GuQiao'

import os,sys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pywinauto.application import Application
from public.common import Browser

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

filepath = r"C:\Product Template.xls"
url_mkp = "https://b2b4tcsdev-plmcomm.cs19.force.com/MarketPlace/s/"

class WinAuto:

    def __init__(self, class_name, title_re):
        # 初始化driver
        self.driver = Browser.driver
        # 连接到指定窗口
        self.app = Application().connect(class_name = class_name, title_re = title_re)

    def loginMarketPlace(self, url):
        self.driver.get(url)
        print("\n----------------------------Login into MarketPlace----------------------------")
        self.driver.implicitly_wait(5)
        # Browser.driver.set_window_size(1552, 848)
        self.driver.maximize_window()
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
        WebDriverWait(self.driver, 30000).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(.,\'Add New Product\')]")))
        self.driver.find_element(By.XPATH, "//button[contains(.,\'Add New Product\')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,\'Upload Files\')]").click()

    def get_window(self, window_object, class_name = "", title_re = ""):
        return window_object.window(class_name = class_name, title_re = title_re)

    # 输入指定信息
    def file_input(self, file_path):
        # 定位到标题名为'Open'的对话框
        window = self.get_window(self.app, "#32770", "Open")
        # 定位到编辑框
        window = self.get_window(window, class_name = "Edit")
        # 向编辑框输入信息
        window.TypeKeys(file_path)

    # 点击打开按钮
    def open_button_click(self):
        # 定位到标题名为'Open'的对话框
        window = self.get_window(self.app, "#32770", "Open")
        # 定位到Open按钮
        button = self.get_window(window, class_name = "Button", title_re = "Open")
        # 点击Open按钮
        button.click()


    # def upload_file(filepath):
    #     # 一级窗口
    #     dialog = win32gui.FindWindow("#32770", "Open")
    #     # 找到窗口二级元素
    #     ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
    #     # 三级元素
    #     combox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)
    #     # EDIT元素
    #     edit = win32gui.FindWindowEx(combox, 0, "Edit", None)
    #     # 打开按钮元素
    #     button = win32gui.FindWindowEx(dialog, 0, "Button", None)
    #     win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filepath)
    #     # 点击打开按钮提交
    #     win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

    # def winauto(filename):
    #     # 使用pywinauto进行上传操作
    #     app = application.Application()
    #     # 连接到指定窗口
    #     app.connect(class_name=class_name, title_re=title_re)
    #     time.sleep(1)
    #     # 定位窗口
    #
    #     window = app.window_(class_name="#32770")
    #     # 文件所在路径不能含有空格
    #     window["Edit"].TypeKeys(filename)
    #     window["ScrollBar"].Click()
    #     window[u"Open(O)"].Click()



        # upload = Browser.driver.find_element_by_id('file')
        # time.sleep(5)
        # upload.send_keys(filepath)  # send_keys
        # print(upload.get_attribute('value'))  # check value

        # # # 上传文件
        # # upload_files(file_path)
        # # 点击文件上传，弹窗出现窗口
        # # 出现弹窗窗口,使用upload 方法
        # upload_file(filepath)
        # time.sleep(2)

        Browser.driver.quit()


if __name__ == '__main__':
    window = WinAuto("#32770", "Open")
    window.file_input(filepath)
    window.open_button_click()




