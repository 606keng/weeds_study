#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: main.py
@time: 2020/08/06 
"""
import os

from carsir_ui.page.app import App
from carsir_ui.page.carsir.input_car_info.input_car_info import InputCarInfo


class Main(App):
    def easy_shou_button(self):
        self.data = self.read_yaml(os.path.dirname(__file__), r"main.yaml")
        self.steps(self.data["easy_shou_btn"])
        return InputCarInfo(self._driver)

    def easy_shou_card(self):
        pass

    def easy_pei_button(self):
        pass

    def easy_pei_card(self):
        pass

    def easy_gou_button(self):
        pass

    def easy_gou_card(self):
        pass

    def logout(self):
        from carsir_ui.page.carsir.login.login import Login
        self.data = self.read_yaml(os.path.dirname(__file__), r"main.yaml")
        self.steps(self.data["logout"])
        return Login(self._driver)


if __name__ == '__main__':
    Main()
