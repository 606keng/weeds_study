#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: main.py
@time: 2020/07/23
@remark：
"""
from selenium.webdriver.common.by import By

from selenium_study.test_pageobject.page.base_page import BasePage
from selenium_study.test_pageobject.page.login import Login
from selenium_study.test_pageobject.page.register import Register


class Main(BasePage):
    _url = "https://work.weixin.qq.com/"

    def goto_login(self):
        self.find(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return Login()

    def goto_register(self):
        self.find(By.CSS_SELECTOR,".index_head_info_pCDownloadBtn").click()
        return Register(self._driver)
