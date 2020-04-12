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
        self.driver.implicitly_wait(100)
    def teardown(self):
        self.driver.quit()
    def test_dingwei(self):
        """
        1.打开雪球app
        2.点击搜索输入框
        3.向搜索框输入阿里巴巴
        4.在搜索结果里面选择阿里巴巴，然后点击
        5.获取阿里巴巴香港的股价，并判断这只股价的价格>190
        :return:
        """

        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text

        assert float(current_price) > 190

    def test_uiautomator_dingwei(self):
        """
        1.点击我的，进入到个人信息页面
        2.点击登录，进入登录页面
        3.输入用户名，输入密码
        4.点击登录
        :return:
        """
        #注意new UiSelector().text("我的")必须要用单引号，点击我的。
        # 定位方式，匹配页面中文字为“我的”的元素
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        #匹配页面中文字包含“帐号密码”的元素，点击
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        #使用resource_id定位账号输入框
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("18791076614")
        # 使用resource_id定位密码输入框
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("1123123123")
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()
        #使用resourceId和text组合定位,定位resourceId为某个参数并且text为某个值的元素
        #self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")').click()
        #使用父子关系进行定位，查找resourceId为某个值的元素的子节点中text为股票的元素
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/title_container").childSelector(text("股票"))').click()

    def test_scroll_find_element(self):
        #进入我的关注页面
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
        #滚动查找text为“朋克民族”，查找时间为设置的隐式等待时间，超过隐式等待时间未查到到，则报错
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("朋克民族").'
                                                        'instance(0));').click()

