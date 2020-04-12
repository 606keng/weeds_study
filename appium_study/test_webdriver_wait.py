from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDingWei:
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
    def test_dingwei(self):
        """
        显式等待查找元素
        :return:
        """

        locator = (MobileBy.ID,"com.xueqiu.android:id/tv_search")
        # 显式等待,等待10秒，每0.5秒查询一次，直到元素可以点击
        element = WebDriverWait(self.driver,10,0.5).until(expected_conditions.element_to_be_clickable(locator))
        #使用lambda表达式编写显式等待
        element = WebDriverWait(self.driver,10).until(lambda x: x.find_element(*locator))
