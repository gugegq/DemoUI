#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'GuQiao'

from pywinauto import Application

def upload_files(classname, filepath):
    # 方法二：调用pywinauto第三方库，模拟windows窗口操作
    app = Application()  # 实例化Application
    # 这里用的class而没有加窗口title，主要为了保证兼容性
    # app.connect(class_name='#32770')  # 根据class_name找到弹出窗口
    app.connect(class_name=classname)
    app["Dialog"]["Edit1"].TypeKeys(filepath)  # 在输入框中输入值
    app["Dialog"]["Button1"].click()  # 点击打开/保存按钮

# if __name__ == '__main__':
#     class_name = input("Pls input class_name, common value is '#32770': \r")
#     filepath = input("Pls input filepath: \r")
#     upload_files(class_name, filepath)
