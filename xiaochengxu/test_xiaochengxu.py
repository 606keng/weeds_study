#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: test_xiaochengxu.py
@time: 2020/08/15
@remark：
"""
import os
from time import sleep

import yaml
from appium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Testxiaochengxu:
    def setup(self):
        with open("config.yaml", "r") as f:
            cps = yaml.safe_load(f)

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cps)
        print(cps)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//*[@text='通讯录']")

    def test_carsir(self):
        # 原生自动化
        self.driver.implicitly_wait(20)
        size = self.driver.get_window_size()
        self.driver.swipe(size["width"] * 0.5, size["height"] * 0.4, size["width"] * 0.5, size["height"] * 0.9)
        self.driver.find_element(By.ID, "com.tencent.mm:id/lj").click()
        self.driver.find_element(By.ID, "com.tencent.mm:id/bhn").send_keys("优信养车")
        # self.driver.find_element(By.ID, "com.tencent.mm:id/bhn").click()
        # ActionChains(self.driver).send_keys("优信养车").perform()
        # sleep(2)
        # 执行adb命令，调起百度键盘
        os.system('adb shell settings put secure default_input_method com.baidu.input/.ImeService')
        # sleep(2)
        t = 0
        while True:
            sleep(0.5)
            self.driver.press_keycode(84)
            try:
                self.driver.find_element(By.CLASS_NAME, "android.widget.Button").click()
                break
            except:
                pass


        # self.driver.find_element()

        # sleep(5)
        # print(self.driver.contexts)
        # self.driver.switch_to.context(r"NATIVE_APP")
        print("开始切换")
        self.driver.switch_to.context(r"WEBVIEW_com.tencent.mm:appbrand0")
        # print("切换完成")
        # print("sleep before",self.driver.window_handles)
        # # sleep(5)
        # print("sleep after",self.driver.window_handles)
        # # self.find_top_window()
        # # print(self.driver.page_source)
        # WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > 1)
        # 点击车型管理
        t = 0
        while True:

            try:
                self.wait("/html/body/wx-view/wx-view[1]/wx-view[2]/wx-view/wx-view[1]/wx-view[2]/wx-view[1]").click()
                break
            except:
                sleep(0.5)
                t += 0.5
            if t > 20:
                break
        # self.driver.find_element(By.XPATH,
        #                          "/html/body/wx-view/wx-view[1]/wx-view[2]/wx-view/wx-view[1]/wx-view[2]/wx-view[1]").click()
        # sleep(2)
        self.find_top_window()
        self.wait("/html/body/wx-view/wx-view").click()
        # self.driver.find_element(By.XPATH, "/html/body/wx-view/wx-view").click()
        # sleep(5)
        self.find_top_window()
        # print("执行self.driver.window_handles")
        # WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > 2)
        # print("self.driver.window_handles执行结束")
        # print(self.driver.window_handles)
        self.wait('/html/body/wx-view/wx-view[1]/wx-view/wx-view/wx-text').click()
        # self.driver.find_element(By.XPATH, '/html/body/wx-view/wx-view[1]/wx-view/wx-view/wx-text').click()

        self.driver.switch_to.context(r"NATIVE_APP")
        # 执行adb命令，调起百度键盘
        # os.system('adb shell settings put secure default_input_method io.appium.settings/.UnicodeIME')
        # 输入文字，目前不支持输入中文，具体解决方案待定
        ActionChains(self.driver).send_keys("ALP").perform()
        self.driver.switch_to.context(r"WEBVIEW_com.tencent.mm:appbrand0")
        # sleep(3)
        self.wait('/html/body/wx-view/wx-view[2]/wx-scroll-view/div/div[1]/div/wx-view/wx-view[2]').click()
        # self.driver.find_element(By.XPATH,
        #                          '/html/body/wx-view/wx-view[2]/wx-scroll-view/div/div[1]/div/wx-view/wx-view[2]').click()
        self.find_top_window()
        # sleep(3)
        self.wait('/html/body/wx-view/wx-scroll-view/div/div[1]/div/wx-view/wx-view[2]/wx-view[2]/wx-text').click()
        # self.driver.find_element(By.XPATH,
        #                          "/html/body/wx-view/wx-scroll-view/div/div[1]/div/wx-view/wx-view[2]/wx-view[2]/wx-text").click()

    def find_top_window(self):
        """
        找到顶层可用的窗口
        :return:
        """
        for window in self.driver.window_handles:
            # VISIBLE为顶层可用窗口，INVISIBLE为非顶层可用窗口
            if ":VISIBLE" in self.driver.title:
                pass
            else:
                self.driver.switch_to.window(window)

    def wait(self, locator):
        WebDriverWait(self.driver, 30).until(lambda x: self.driver.find_element_by_xpath(locator))
        return self.driver.find_element_by_xpath(locator)
