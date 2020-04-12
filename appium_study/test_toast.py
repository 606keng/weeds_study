from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestToast:
    def setup(self):
        _package = "io.appium.android.apis"
        _activity = "io.appium.android.apis.view.PopupMenu1"

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
    # def teardown(self):
    #     self.driver.quit()
    def test_dingwei_toast(self):
        """
        识别toast
        :return:
        """

        self.driver.find_element_by_xpath("//*[@class='android.widget.Button']").click()
        self.driver.find_element_by_xpath("//*[@text='Search']").click()
        #打印出当前页面的dom树
        #print(self.driver.page_source)
        #打印toast提示的文字信息
        print(self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text)