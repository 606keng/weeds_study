from time import sleep

from hamcrest import *
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAtttribute:
    def setup(self):
        _package = "com.xueqiu.android"
        _activity = ".view.WelcomeActivityAlias"

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
        # cps['dontStopAppOnReset'] = 'true'
        #定义支持中文
        cps["unicodeKeyBoard"] = 'true'
        #定义支持中文
        cps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()
    def test_get_attribute(self):
        search_ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        #get_attribute获取元素的属性，入参为属性名称
        print(search_ele.get_attribute("resource-id"))

    def test_assert(self):
        a = 10
        b = 20
        assert a < b
    def test_hamcrest(self):
        #断言10=10
        assert_that(10,equal_to(10),"这是一个提示")
        #判断13是不是在8到12之间
        assert_that(13, close_to(10, 2))
        #判断string是否包含在"contain some string"中
        assert_that("contain some string",contains_string("string"))
