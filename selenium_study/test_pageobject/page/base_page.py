#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: base_page.py
@time: 2020/07/23
@remark：
"""
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _url = ""

    def __init__(self, driver: WebDriver = None):
        self._driver = ""
        if driver is None:
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver

        if self._url != "":
            self._driver.get(self._url)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)
