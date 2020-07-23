#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: test_register.py
@time: 2020/07/23
@remark：
"""
from selenium_study.test_pageobject.page.base_page import BasePage
from selenium_study.test_pageobject.page.main import Main


class TestRegister():
    def setup(self):
        self.main = Main()


    def test_register(self):
        self.main.goto_register().register()
