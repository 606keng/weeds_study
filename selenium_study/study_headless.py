#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: study_headless.py
@time: 2021/01/07 
"""
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('headless')  # 静默模式
# 打开chrome浏览器
driver = webdriver.Chrome( chrome_options=option)
driver.get("https://www.cnblogs.com/yoyoketang")
print(driver.title)