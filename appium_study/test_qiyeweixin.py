from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestToast:
    def setup_class(self):
        _package = "com.tencent.wework"
        _activity = ".launch.WwMainActivity"

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
        print(cps)
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cps)
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.quit()
    @pytest.mark.parametrize(("send_message"),[("晚上好"),  ("辛苦了"),  ("早点睡")])
    def test_qiyeweixin(self,send_message):
        """
        打开企业微信（提前登录）
        进入通讯录
        点击搜索按钮
        输入 已存在的联系人姓名, 例如“aa”，
        点击联系人，进入聊天页面
        输入“测试code”
        点击发送
        点击返回
        :return:
        """
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/dnj' and @text='通讯录']").click()
        self.driver.find_element_by_id("com.tencent.wework:id/gq_").click()
        self.driver.find_element_by_id("com.tencent.wework:id/ffq").send_keys("豆")
        self.driver.find_element_by_id("com.tencent.wework:id/de1").click()
        self.driver.find_element_by_id("com.tencent.wework:id/aaj").click()
        self.driver.find_element_by_id("com.tencent.wework:id/dtv").send_keys(send_message)
        self.driver.find_element_by_id("com.tencent.wework:id/dtr").click()
        self.driver.find_element_by_id("com.tencent.wework:id/gpp").click()
