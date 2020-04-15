from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import assert_that, close_to
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
        self.driver.find_element_by_id("com.xueqiu.android:id/action_close").click()
    @pytest.mark.parametrize("search_key, type, expect_price",[
        ("阿里巴巴", "阿里巴巴", "200"),
        ("小米", "小米集团-W", "10")
    ])
    def test_param(self,search_key, type, expect_price):
        """
        1.打开雪球app
        2.点击搜索输入框
        3.向搜索框输入阿里巴巴 或者小米
        4.选择第一只股票
        5.获取这只股票的股价，并判断这只股价的价格>190
        :return:
        """

        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(search_key)
        self.driver.find_element_by_xpath(f"//*[@resource-id='com.xueqiu.android:id/name' and @text='{ type }']").click()
        current_price = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/current_price']").text
        expect_price = float(expect_price)
        assert_that(float(current_price), close_to(expect_price, expect_price*0.1))

