import time

import pytest
from selenium import webdriver

from public.common import Browser


class baseLogin:

    def __init__(self):
        self.driver = Browser.driver

    def base_login(self):
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com")
        # driver.implicitly_wait(5)
        value = self.driver.title
        print(value)
        assert value in "百度一下，你就知道啊"
        time.sleep(10)

    def open_url(self,url):
        self.driver.get(url)

    def quit_url(self):
        self.driver.quit()


# if __name__ == '__main__':
#     pytest.main(['-vs','./baseLogin.py'])
