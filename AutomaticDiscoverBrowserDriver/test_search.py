#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: test_search.py.py
@time: 2020/12/14 
"""
import pytest
from time import sleep
from selenium import webdriver

from AutomaticDiscoverBrowserDriver.utils.driver_util import automatic_discover_driver as automatic

class TestSearch:
    _CHROME_PATH = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    _EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    _browser = "Chrome"

    def setup(self):
        driver_path = automatic(self._CHROME_PATH, self._browser)
        if self._browser == "Chrome":
            self.driver = webdriver.Chrome(driver_path)
        elif self._browser == "Edge":
            self.driver = webdriver.Edge(driver_path)

    def teardown(self):
        self.driver.close()
        self.driver.quit()

    def test_search_bing(self):
        self.driver.get("https://cn.bing.com/")
        self.driver.find_element_by_id("sb_form_q").send_keys("selenium")
        self.driver.find_element_by_id("sb_go_par").click()
        sleep(3)


if __name__ == '__main__':
    pytest.main()