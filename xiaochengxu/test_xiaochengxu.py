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
from selenium.webdriver.android.webdriver import WebDriver
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
        # 获取屏幕的尺寸
        size = self.driver.get_window_size()
        # 下拉操作
        self.driver.swipe(size["width"] * 0.5, size["height"] * 0.4, size["width"] * 0.5, size["height"] * 0.9)
        # 点击搜索框
        self.driver.find_element(By.ID, "com.tencent.mm:id/lj").click()
        self.driver.find_element(By.ID, "com.tencent.mm:id/bhn").send_keys("优信养车")
        # 执行adb命令，调起百度键盘
        os.system('adb shell settings put secure default_input_method com.baidu.input/.ImeService')
        # 每隔0.5秒点击优信养车小程序
        while True:
            self.driver.press_keycode(84)
            try:
                sleep(0.5)
                self.driver.find_element(By.CLASS_NAME, "android.widget.Button").click()
                break
            except:
                pass

        sleep(5)
        print(self.driver.contexts)
        # 切换到小程序android进程
        self.driver.switch_to.context(r"WEBVIEW_com.tencent.mm:appbrand0")
        sleep(5)
        # 点击车型管理
        self.wait_time("/html/body/wx-view/wx-view[1]/wx-view[2]/wx-view/wx-view[1]/wx-view[2]/wx-view[1]").click()
        # 跳转到最顶部的窗口
        self.find_top_window()
        # 点击新增车型
        self.wait_time("/html/body/wx-view/wx-view").click()
        self.find_top_window()
        # 给小程序输入文字
        self.send_kenys('/html/body/wx-view/wx-view[1]/wx-view/wx-view/wx-text', "大众")

        # 选择列表中的第二个车系
        self.wait_time('/html/body/wx-view/wx-view[2]/wx-scroll-view/div/div[1]/div/wx-view/wx-view[2]').click()
        self.find_top_window()
        # 选择第一个车型
        self.wait_time('/html/body/wx-view/wx-scroll-view/div/div[1]/div/wx-view/wx-view[2]/wx-view[2]/wx-text').click()
        sleep(5)
        # self.find_top_window()
        # # 点击删除
        # self.wait_time(
        #     '/html/body/wx-view/wx-scroll-view/div/div[1]/div/wx-view[2]/wx-view[2]/wx-view[2]/wx-text[2]/span[2]').click()
        # # 切换到原生页面
        # self.driver.switch_to.context(r"NATIVE_APP")
        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()

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

    def wait_time(self, locator):
        WebDriverWait(self.driver, 30).until(lambda x: self.driver.find_element_by_xpath(locator))
        return self.driver.find_element_by_xpath(locator)

    def send_kenys(self, locator, vaule):
        # 执行adb命令，调起adbkeyboard键盘
        os.system('adb shell settings put secure default_input_method com.android.adbkeyboard/.AdbIME')
        # 点击搜索框，
        self.wait_time(locator).click()
        # 切换到原生页面
        self.driver.switch_to.context(r"NATIVE_APP")
        sleep(2)
        # 输入文字，支持中文
        os.system(f'adb shell am broadcast -a ADB_INPUT_TEXT --es msg "{vaule}"')
        # 切换回小程序
        self.driver.switch_to.context(r"WEBVIEW_com.tencent.mm:appbrand0")



