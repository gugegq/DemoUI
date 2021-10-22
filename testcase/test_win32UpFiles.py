#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'GuQiao'

import os, sys
import time

import win32con
import win32gui
from airtest_selenium.proxy import WebChrome
from config import setting
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pywinauto.application import Application
# from public.base.upload_files import upload_files

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
driver = WebChrome(executable_path=setting.DRIVER_DIR + r"/chromedriver.exe")

filepath = r"D:\ProductTemplate.xls"
url_mkp = "https://b2b4tcsdev-plmcomm.cs19.force.com/MarketPlace/s/"

class testUploadFiles:

    def testUpFiles(self):
        driver.get(url_mkp)
        print("\n----------------------------Login into MarketPlace----------------------------")
        driver.maximize_window()
        time.sleep(5)
        driver.find_element(By.ID, "username").clear()
        driver.find_element(By.ID, "username").send_keys("demouser01@yopmail.com")
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys("Password1")
        driver.find_element(By.ID, "submit").click()
        time.sleep(5)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(.,\'Add New Product\')]")))
        driver.find_element(By.XPATH, "//button[contains(.,\'Add New Product\')]").click()
        driver.find_element(By.XPATH, "//span[contains(.,\'Upload Files\')]").click()
        time.sleep(3) # 需要稍作等待，因为点击上传按钮到文件选择窗口打开会有延迟
        # # 方法一：标准html的input格式，直接调用send_keys方法
        # # 直接传输文件
        # WebDriverWait(driver, 30).until(
        #     expected_conditions.visibility_of_element_located((By.ID, "input-file-19")))
        # driver.find_element(By.ID, "input-file-19").send_keys(filepath)
        # # 方法二：调用pywinauto第三方库，模拟windows窗口操作
        # app = Application()  # 实例化Application
        # time.sleep(3) # 需要稍作等待，因为点击上传按钮到文件选择窗口打开会有延迟
        # # 这里用的class而没有加窗口title，主要为了保证兼容性
        # app.connect(class_name='#32770')  # 根据class_name找到弹出窗口
        # app["Dialog"]["Edit1"].TypeKeys(filepath)  # 在输入框中输入值
        # app["Dialog"]["Button1"].click()  # 点击打开/保存按钮
        # # upload_files("#32770", filepath)
        # 方法三：调用pywin32第三方库，模拟windows窗口操作
        '''
            通过pywin32模块实现文件上传的操作
            :param filePath: 文件的绝对路径
            :param browser_type: 浏览器类型（默认值为chrome）
            :return:
            '''
        # 找元素
        # 一级窗口"#32770","打开"
        dialog = win32gui.FindWindow("#32770", "Open")
        # 向下传递
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
        comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
        # 编辑按钮
        edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
        # 打开按钮
        button = win32gui.FindWindowEx(dialog, 0, 'Button', "&Open")  # 二级

        # 输入文件的绝对路径，点击“打开”按钮
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filepath)  # 发送文件路径
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮

        time.sleep(5)
        driver.quit()

if __name__ == '__main__':
    test = testUploadFiles()
    test.testUpFiles()
    # pytest.main(['-vs','./baseLogin.py'])