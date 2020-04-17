#!/usr/bin/env python
#-*-coding: UTF-8 -*-
import subprocess
import time
import os
from appium import webdriver
import random
from selenium.webdriver.support.wait import WebDriverWait
from AppiumAndroid import *

class appium_server(object):
    random_port = random.randint(1111, 9999)
    random_bp = random.randint(11111,55555)
    @caps
    # def __init__(self,udid,app_path,adb_path,aapt_path):
    def __init__(self,udid,caps):
        #配置基础参数
        # self.aapt_path = aapt_path
        # self.adb_path = adb_path
        # self.app_path = app_path
        self.udid = udid
        # try:
        cmd = "appium -a 127.0.0.1 -U %s -p %s -bp %s --command-timeout 100000 --session-override"%(udid,self.random_port,self.random_bp)
        subprocess.Popen(cmd,shell=True)
        print("正在启动appium服务，请稍等.....")
        time.sleep(6)

        print("正在安装应用服务，请稍等.....")

        self.driver = webdriver.Remote('http://127.0.0.1:%s/wd/hub'%(self.random_port),caps)
        self.driver.implicitly_wait(15)

    def __del__(self):
        pass


    def wait_element(self):
        WebDriverWait()

    @closeServer
    def closeAppium(self):
        return self.random_port

    @isAppium
    def isStartAppium(self):
        return self.random_port

    @get_element
    def set_element(self):
        return self.driver

    def permissions_check(self):
        for i in range(3):
            el = self.set_element("classes", "android.widget.Button")
            for i in el:
                if "允许" in str(i.text) or "确定" in str(i.text):
                    permissions_element = "//android.widget.Button[@text='%s']"%(str(i.text))
                    permissions_el = self.set_element("xpath", permissions_element)
                    permissions_el.click()


    def click(self,typed,element):
        el = self.set_element(typed,element)
        el.click()

    def clicks(self,typed,element,n):
        el = self.set_element(typed,element)
        el[int(n)].click()

    def input(self,typed,element,text):
        el = self.set_element(typed, element)
        el.send_keys(str(text))

    def inputs(self,typed,element,n,text):
        el = self.set_element(typed, element)
        el[int(n)].clear()
        el[int(n)].send_keys(str(text))

    def get_text(self,typed,element):
        el = self.set_element(typed, element)
        return el.text()

    def gets_text(self,typed,element,n):
        el = self.set_element(typed, element)
        return el.text()

    def install(self,app_path):
        self.driver.install_app(app_path)

    def callBack(self):
        self.driver.back()

    def downSroll(self):
        print("---lzh-->")
        time.sleep(1)
        element_size = self.driver.get_window_size()
        x = element_size["width"]
        y = element_size["height"]
        self.driver.swipe(500,int(y)/2+120,500,100)


    def upwardSroll(self):
        print("---lzh-->")
        time.sleep(1)
        element_size = self.driver.get_window_size()
        x = element_size["width"]
        y = element_size["height"]
        self.driver.swipe(500, 100, 500, int(y) / 2 + 120)

    def screenshot(self,screenshot_path,name):
        self.driver.get_screenshot_as_file(screenshot_path+"/"+name+".png")



if __name__ == '__main__':
    aapt_path = "/Library/android_sdk/build-tools/26.0.2/aapt" #环境变量配置好后，无需再配置aapt路径
    adb_path = "/Library/android_sdk/platform-tools/adb" #环境变量配置好后，无需再配置adb路径
    app_path = "/Users/liaozhenghong/Downloads/douyin.apk"
    udid = "emulator-5554"
    '''
        udid、app_path必选参数
    '''
    appiumServer = appium_server(udid,app_path,aapt_path=aapt_path)
    # appiumServer = appium_server(udid,app_path)

    appiumServer.screenshot("/Users/liaozhenghong/Downloads","name")
    for i in range(5):
        appiumServer.downSroll()
        print('sourcll....')
        time.sleep(1)

    time.sleep(5)
    appiumServer.permissions_check()
    for i in range(5):
        appiumServer.downSroll()
        print('sourcll....')
        time.sleep(1)

    for i in range(5):
        appiumServer.upwardSroll()
        print('sourcll....')
        time.sleep(1)

    time.sleep(10)

    appiumServer.closeAppium()
    # time.sleep(20)
    # appiumServer.closeAppium()
    # for i in range(3):
    #     appiumServer.click("xpath","//*[@text='允许']")
    # caps = appiumServer.driver_caps()
    # appiumServer.startDriver(caps)
    # time.sleep(5)
    # print(appiumServer.closeAppiumServer())

