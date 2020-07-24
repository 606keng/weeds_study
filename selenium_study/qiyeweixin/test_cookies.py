#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: test_cookies.py
@time: 2020/07/24
@remark：
"""
import json
from typing import List, Dict

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCookies:
    def setup_method(self):
        # 声明一个变量，设置为chrometoptions
        chrome_opts = webdriver.ChromeOptions()
        # set address same as chrome debugging port
        chrome_opts.debugger_address = "127.0.0.1:9222"
        # 将代理浏览器配置在webdriver中
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com")
        self.driver.implicitly_wait(5)

    def test_cookies(self):
        # cookies = self.driver.get_cookies()
        # with open("cookies1.txt", "w") as f:
        #     json.dump(cookies, f)
        with open("cookies1.txt", "r") as f:
            cookies: List[Dict] = json.load(f)

        for cookie in cookies:
            # if "expiry" in cookie.keys():
            #     cookie.pop("expiry")
            # 切记，不要在打开网站前操作self.driver.add_cookie(cookie)，否则会报invalid cookie domain错误
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap").click()
        self.driver.find_element_by_id("username").send_keys("weeds")
