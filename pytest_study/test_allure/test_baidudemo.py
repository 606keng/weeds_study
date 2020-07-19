#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: test_baidudemo.py
@time: 2020/07/15
@remark：使用pytest allure生成测试报告
"""
import time

import allure
import pytest
from selenium import webdriver


@allure.testcase("https://blog.csdn.net/doulihang",name="测试用例编号")
@allure.feature("百度搜索")
@pytest.mark.parametrize("testdata", ["python", "allure", "selenium"])
def test_step_demo(testdata):
    with allure.step("打开百度"):
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com")
        driver.maximize_window()

    with allure.step(f"输入搜索关键词{testdata}"):
        driver.find_element_by_id("kw").send_keys(testdata)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(3)
    with allure.step("保存图片"):
        driver.save_screenshot("./resouces/b.jpg")
        allure.attach.file("./resouces/b.jpg", name="搜索截图", attachment_type=allure.attachment_type.JPG)
        allure.attach("<body>首页</body>", name="首页", attachment_type=allure.attachment_type.HTML)
    with allure.step("退出浏览器"):
        driver.quit()
