#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: login.py
@time: 2020/07/23
@remark：
"""
from selenium.webdriver.common.by import By

from selenium_study.test_pageobject.page.base_page import BasePage
from selenium_study.test_pageobject.page.register import Register


class Login(BasePage):

    def goto_register(self):
        self.find(By.CSS_SELECTOR,".login_registerBar_link").click()
        return Register(self._driver)

    def scan(self):
        pass
