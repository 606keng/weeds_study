#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: H5性能测试.py
@time: 2021/01/18
@remark：
"""
import json

from selenium import webdriver


class TestData:
    def test_data(self):
        driver = webdriver.Chrome()
        driver.get("https://www.selenium.dev/")
        data = json.loads(driver.execute_script("return JSON.stringify(window.performance.timing)"))
        print()
        all_time = int(data["connectEnd"]) - int(data["connectStart"])
        print(all_time)