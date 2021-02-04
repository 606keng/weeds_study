#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: test_H5.py
@time: 2021/01/20 
"""
from time import sleep

from appium import webdriver


class TestH5:
    def setup(self):
        cps = {}
        cps["platformName"] = "android"
        cps["deviceName"] = "79UNW19701000783"
        cps["appPackage"] = "com.consumer.carsir"
        cps["appActivity"] = ".activity.StartPageActivity"
        cps["noReset"] = "true"
        cps["automationName"] = "uiautomator1"
        # 定义支持中文
        cps["unicodeKeyboard"] = True
        # 定义支持中文
        cps['resetKeyboard'] = True
        cps["chromedriverExcutable"] = r"D:\work\auto\weeds_study\venv\chromedriver.exe"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", cps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_h5(self):
        # 进入carsir APP首页，点击车辆名称进入车辆详情
        eles = self.driver.find_elements_by_id("com.consumer.carsir:id/tv_car_desc")
        eles[0].click()
        sleep(20)
        # 获取H5context
        print(self.driver.contexts)
        # 切换driver的context
        self.driver.switch_to.context("WEBVIEW_com.consumer.carsir")
        print(self.driver.page_source)
        # 进入h5页面，点击修改车辆价格
        self.driver.find_element_by_xpath("//*[@class='particulars-header-changefee']").click()
        sleep(10)