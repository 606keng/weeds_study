#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: login.py
@time: 2020/08/05 
"""
import os

from carsir_ui.page.app import App
from carsir_ui.page.carsir.main.main import Main
from carsir_ui.utils.basepath import PagePath


class Login(App):
    def input_phone_number(self, number):
        self.data = self.read_yaml(os.path.dirname(__file__), r"login.yaml")
        self._params["number"] = number
        self.steps(self.data["input_phone"])

    def input_verification_code(self, code):
        self.data = self.read_yaml(os.path.dirname(__file__), r"login.yaml")
        self._params["code"] = code
        self.steps(self.data["input_verification_code"])
        return Main(self._driver)

    def goto_main(self):
        return Main(self._driver)
