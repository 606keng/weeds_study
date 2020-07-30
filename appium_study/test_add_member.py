#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: test_add_member.py
@time: 2020/07/28
@remark：
"""
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class TestAddMember():
    def setup(self):
        cps = {}
        cps["platformName"] = "android"
        cps["deviceName"] = "emulator-5554"
        cps["appPackage"] = "com.tencent.wework"
        cps["appActivity"] = ".launch.WwMainActivity"
        cps["noReset"] = "true"
        cps["automationName"] = "uiautomator1"
        # 定义支持中文
        cps["unicodeKeyboard"] = True
        # 定义支持中文
        cps['resetKeyboard'] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", cps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_add_member(self):
        # 点击通讯录
        self.driver.find_element(By.XPATH, "//*[@text='通讯录']").click()
        # 滚动查找添加成员
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                               'scrollable(true).instance(0)).'
                                                               'scrollIntoView(new UiSelector().text("添加成员").'
                                                               'instance(0));').click()
        # 点击手动添加成员
        self.driver.find_element(By.ID, "com.tencent.wework:id/cfu").click()

        # 输入姓名
        self.driver.find_elements(By.ID, "com.tencent.wework:id/ayv")[0].send_keys(u"豆立航")

        # 点击性别
        self.driver.find_element(By.ID, "com.tencent.wework:id/e93").click()
        # 选择nv
        self.driver.find_elements(By.ID, "com.tencent.wework:id/ben")[1].click()

        # 输入手机号
        self.driver.find_element(By.ID, "com.tencent.wework:id/f8g").send_keys("18700001111")

        # 输入邮箱
        self.driver.find_element(By.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/e8x']//*[@resource-id='com.tencent.wework:id/ayv']").send_keys(
            "18791076614@163.com")

        # 输入地址
        self.driver.find_element(By.ID,"com.tencent.wework:id/e8a").click()
        self.driver.find_element(By.ID, "com.tencent.wework:id/bys").send_keys(u"西安市雁塔区青松路")
        self.driver.find_element(By.ID, "com.tencent.wework:id/hi9").click()


        # 点击保存
        self.driver.find_element(By.ID,"com.tencent.wework:id/hi9").click()