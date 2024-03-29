import time

import pytest
from selenium import webdriver

from public.common import Browser


class baseLogin:

    def __init__(self):
        self.driver = Browser.driver

    def base_login(self):
        self.driver.maximize_window()
        self.driver.get("https://b2b4tcsdev-plmcomm.cs19.force.com/MarketPlace/s/")
        time.sleep(10)

    def open_url(self,url):
        self.driver.get(url)

    def quit_url(self):
        self.driver.quit()


# if __name__ == '__main__':
#     pytest.main(['-vs','./baseLogin.py'])
