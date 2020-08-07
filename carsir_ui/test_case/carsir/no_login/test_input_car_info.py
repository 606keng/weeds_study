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

    def test_click_easy_shou(self,start):
        self.page = start.easy_shou_button()
        self.page.select_city()
        self.page.select_brand_series()
        self.page.back()