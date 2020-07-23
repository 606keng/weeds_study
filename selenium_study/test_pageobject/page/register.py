#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: register.py
@time: 2020/07/23
@remark：
"""
from selenium.webdriver.common.by import By

from selenium_study.test_pageobject.page.base_page import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.ID, "corp_name").send_keys("doulihang")
        self.find(By.ID, "manager_name").send_keys("gaogao")
