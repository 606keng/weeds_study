#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: test_main.py
@time: 2020/08/06 
"""
import pytest

from carsir_ui.page.app import App


class TestMain:
    def setup(self):
        self.login = App().start_carsir().login()

    @pytest.mark.parametrize("number,code", [("18791076614", "111111")])
    def test_click_easy_shou(self, number, code):
        self.login.input_phone_number(number)
        self.main = self.login.input_verification_code(code)
        self.main.easy_shou_button()
