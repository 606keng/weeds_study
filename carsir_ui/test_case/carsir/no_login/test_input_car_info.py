#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: test_main.py
@time: 2020/08/06 
"""
import pytest

from carsir_ui.page.app import App


class TestInputCarInfo:
    @pytest.fixture()
    def enter_input_car_info(self, start):
        yield start.easy_shou_button()
        start.carsir_back()

    def test_no_city_submit(self, enter_input_car_info):
        self.page = enter_input_car_info
        self.page.submit()
        pytest.assume(self.page.get_toast(), "请选择业务办理城市")

    @pytest.mark.parametrize(("city"), [("日照")])
    def test_select_city(self, enter_input_car_info, city):
        self.page = enter_input_car_info
        self.page.select_city(city=city)

