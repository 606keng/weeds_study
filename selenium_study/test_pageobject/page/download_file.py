#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: download_file.py
@time: 2020/12/08
@remark：
"""
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium_study.test_pageobject.page.base_page import BasePage
from selenium_study.test_pageobject.page.register import Register


class down(BasePage):
    _url = "https://sci-hub.st/downloads/2019-10-27/60/salman2019.pdf?rand=5fcf799f8d8ad?download=true"

    def goto_register(self):
        # self.find(By.XPATH, '//*[@id="buttons"]/ul/li/a').click()
        sleep(20)
        a = True
        while a:
            try:
                self.find(By.XPATH, '//*[@id="icon"]/iron-icon').click()
                a = False
            except:
                sleep(10)


if __name__ == '__main__':
    down().goto_register()
