#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: test_login.py
@time: 2020/08/05 
"""
from carsir_ui.page.app import App


class TestLogin:
    def setup(self):
        self.login = App().start_carsir().login()

    def test_login(self):
        self.login.input_phone_number("1879106614")
