from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestMember:
    def setup_class(self):
        _package = "com.consumer.carsir"
        _activity = ".activity.StartPageActivity"

        cps = {}
        # 测试的平台，Android或iOS
        cps["platformName"] = "android"
        # 链接的设备
        cps["deviceName"] = "doutest"
        # 应用的包名
        cps["appPackage"] = _package
        # 启动的页面名称
        cps["appActivity"] = _activity

        cps["autoGrantPermissions"] = True
        # 设置为true，就不会清空应用的缓存数据
        cps["noReset"] = "true"
        # 运行脚本时，不重启app
        # cps['dontStopAppOnReset'] = 'true'
        # 定义支持中文
        cps["unicodeKeyBoard"] = 'true'
        # 定义支持中文
        cps['resetKeyBoard'] = 'true'
        print(cps)
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cps)
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.quit()
    #调用add_member方法时，调用方执行前，执行yield之前的代码，调用方执行完毕后，再执行yield后面的代码

    def test_carsir(self):
        pass