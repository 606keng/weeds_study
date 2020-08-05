#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: login.py
@time: 2020/08/05 
"""
from carsir_ui.page.app import App


class Login(App):
    def input_phone_number(self,number):
        self._params["number"] = number
        self.steps(r"..\steps\login.yaml")