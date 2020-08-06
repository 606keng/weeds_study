#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: login.py
@time: 2020/08/05 
"""
from carsir_ui.page.app import App
from carsir_ui.utils.basepath import PagePath


class Login(App):

    def input_phone_number(self, number):
        self.data = self.read_yaml(PagePath + r"\carsir\login\steps\login.yaml")
        self._params["number"] = number
        self.steps(self.data["input_phone"])
