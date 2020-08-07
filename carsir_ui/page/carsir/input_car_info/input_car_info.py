#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: input_car_info.py
@time: 2020/08/06 
"""
import os

from carsir_ui.page.app import App
from carsir_ui.utils.basepath import PagePath


class InputCarInfo(App):
    def select_city(self):
        self.data = self.read_yaml(os.path.dirname(__file__), r"input_car_info.yaml")
        self.steps(self.data['select_city'])

    def select_brand_series(self):
        self.data = self.read_yaml(os.path.dirname(__file__), r"input_car_info.yaml")
        self.steps(self.data['select_car'])

    def input_vin(self):
        pass

    def select_registration_time(self):
        pass

    def show_mileage(self):
        pass
