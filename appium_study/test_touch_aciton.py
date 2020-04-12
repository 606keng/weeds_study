from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDingWei:
    def setup(self):
        _package = "com.xueqiu.android"
        _activity = ".common.MainActivity"

        cps = {}
        #测试的平台，Android或iOS
        cps["platformName"] = "android"
        #链接的设备
        cps["deviceName"] = "doutest"
        #应用的包名
        cps["appPackage"] = _package
        #启动的页面名称
        cps["appActivity"] = _activity

        cps["autoGrantPermissions"] = True
        #设置为true，就不会清空应用的缓存数据
        cps["noReset"] = "true"
        #运行脚本时，不重启app
        cps['dontStopAppOnReset'] = 'true'
        #定义支持中文
        cps["unicodeKeyBoard"] = 'true'
        #定义支持中文
        cps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()
    def test_touch_action(self):
        """
        实现功能：将app页面向上滑动
        :return:
        """
        #定义一个TouchAction操作
        action = TouchAction(self.driver)
        #获取屏幕的尺寸
        window_rect = self.driver.get_window_rect()
        #获取屏幕的宽度
        width = window_rect["width"]
        #获取屏幕的高度
        height = window_rect["height"]
        #定义滑动的x坐标点为宽度的1/2
        x1 = int(width/2)
        #定义滑动的起始点为高度的0.8倍
        y_start = int(height*0.8)
        #定义滑动的终点为高度的0.2倍
        y_end = int(height*0.2)
        #press定义滑动的起始点坐标，模拟按下屏幕操作，wait(200)等待200毫秒，move_to定义滑动的终点坐标，
        # release松开屏幕。perform执行加载的动作
        action.press(x=x1,y=y_start).wait(200).move_to(x=x1,y=y_end).release().perform()
