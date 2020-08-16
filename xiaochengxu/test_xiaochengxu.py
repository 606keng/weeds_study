#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: test_xiaochengxu.py
@time: 2020/08/15
@remark：
"""
from time import sleep

import yaml
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Testxiaochengxu:
    def setup(self):
        with open("xiaochengxu.yaml", "r") as f:
            cps = yaml.safe_load(f)
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", cps)
        print(cps)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//*[@text='通讯录']")

    def test_carsir(self):
        # 原生自动化
        size = self.driver.get_window_size()
        self.driver.swipe(size["width"] * 0.5, size["height"] * 0.4, size["width"] * 0.5, size["height"] * 0.9)
        self.driver.find_element(By.ID,"com.tencent.mm:id/lj").click()
        self.driver.find_element(By.ID,"com.tencent.mm:id/bhn").send_keys("轻松卖")
        sleep(2)
        self.driver.back()
        sleep(2)
        self.driver.find_element(By.ID, "com.tencent.mm:id/bhn").click()
        # self.driver.find_element()
        self.driver.find_element(By.CLASS_NAME, "android.widget.Button").click()
        # sleep(15)
        print(self.driver.contexts)
        self.driver.switch_to.context(r"NATIVE_APP")
        print("开始切换")
        self.driver.switch_to.context(r"WEBVIEW_.*.*.*.")
        print("切换完成")
        self.driver.implicitly_wait(10)
        self.find_top_window()
        self.driver.find_element(By.XPATH, "//*[@text='车型管理']").click()
        self.driver.find_element(By.XPATH, "//*[@text='+ 新增车型']").click()
        print("执行self.driver.window_handles")
        WebDriverWait(self.driver,30).until(lambda x: len(self.driver.window_handles) > 2)
        print("self.driver.window_handles执行结束")
        print(self.driver.window_handles)
        self.find_top_window()
        self.driver.find_element(By.ID, 'hot').get_attribute('text')
        self.driver.find_element(By.XPATH, '//*[@class="text"]').send_keys("大众")

    def find_top_window(self):
        """
        找到顶层可用的窗口
        :return:
        """
        for window in self.driver.window_handles:
            # VISIBLE为顶层可用窗口，INVISIBLE为非顶层可用窗口
            if ":VISIBLE" in self.driver.title:
                print(self.driver.title)
            else:
                print(self.driver.title)
                # self.driver.switch_to.window(window)
