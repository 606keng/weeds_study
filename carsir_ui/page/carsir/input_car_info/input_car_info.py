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
    def submit(self):
        data = self.read_yaml(os.path.dirname(__file__), r"input_car_info.yaml")
        self.steps(data['submit'])

    def select_city(self, city="日照"):
        data = self.read_yaml(os.path.dirname(__file__), r"input_car_info.yaml")
        self._params["city"] = city
        self.steps(data['select_city'])

    def select_brand_series(self, brand="奥迪", series="奥迪A3", model="2014款 Limousine 35 TFSI 进取型"):
        data = self.read_yaml(os.path.dirname(__file__), r"input_car_info.yaml")
        self._params["brand"] = brand
        self._params["series"] = series
        self._params["model"] = model
        self.steps(data['select_car'])

    def input_vin(self):
        pass

    def select_registration_time(self):
        pass

    def show_mileage(self):
        pass
