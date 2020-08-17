#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: xiaochengxu.py
@time: 2020/08/17
@remark：
"""
from appium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

desired_caps = {
            'platformName': 'Android',
            'fastReset': 'false',
            'noReset': True,
            # 'platformVersion': '9',
            'deviceName': '79UNW19701000783',
            'appPackage': 'com.tencent.mm',
            'appActivity': 'com.tencent.mm.ui.LauncherUI',
            'fullReset': 'false',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'chromeOptions': {
                'androidProcess': 'com.tencent.mm:appbrand0'
                },
            "chromedriverExecutable": "/Users/doulihang/work/project/weeds_study/xiaochengxu/chromedriver 5"
            }


driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
sleep(5)
driver.find_element_by_android_uiautomator('text("微信")').click() #点击微信Tab


# 定义一个滑动屏幕的方法
def swipeDown(t):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    x1 = int(x * 0.5)  # x坐标
    y1 = int(y * 0.25)  # 起始y坐标
    y2 = int(y * (0.25 + t))  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, 500)


swipeDown(0.4) # 向下滑动屏幕的40%，准备从顶部进入小程序
sleep(2)
driver.find_element_by_android_uiautomator('text("优信养车")').click() #点击顶部的图标进入小程序
sleep(5)
print(driver.contexts)
driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')
print("切换成功")
sleep(5)
# driver.find_element_by_css_selector(".footer2").click()
print(driver.page_source)
driver.find_element(By.XPATH, "/html/body/wx-view/wx-view[1]/wx-view[2]/wx-view/wx-view[1]/wx-view[2]/wx-view[1]").click()