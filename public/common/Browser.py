#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'GuQiao'

from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
from config import setting

driver = WebChrome(executable_path=setting.DRIVER_DIR + r"/chromedriver.exe")

class browser:

    def __init__(self):
        self.driver = driver
        self.driver.implicitly_wait(setting.wait_time)
        self.driver.maximize_window()

    def open_browser(self, url):
        """
        启动浏览器驱动
        """
        try:
            self.driver.get(url)
        except Exception as msg:
            print("驱动异常-> {0}".format(msg))

    def quit_browser(self):
        """
        关闭浏览器
        """
        self.driver.quit()

# '''
# 调试代码用，可注销
# '''
# if __name__ == '__main__':
#     br = browser()
#     br.open_browser("http://www.baidu.com")

