#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: test_logout.py
@time: 2020/08/06 
"""
from carsir_ui.page.app import App


class TestLogout:
    def setup(self):
        self.obj = App().start_carsir().goto_main()

    def test_logout(self):
        self.obj.logout()
