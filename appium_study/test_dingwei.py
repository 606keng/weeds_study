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
        1.打开雪球app
        2.点击搜索输入框
        3.向搜索框输入阿里巴巴
        4.在搜索结果里面选择阿里巴巴，然后点击
        5.获取这只阿里巴巴的股价，并判断这只股价的价格>190
        :return:
        """

        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/current_price']").text
        assert float(current_price) > 190

        #self.driver.find_element_by_accessibility_id()
        # self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]').click()
        #显式等待
        # element = WebDriverWait(driver,10,0.5).until(expected_conditions.visibility_of_element_located((MobileBy.ID,"com.xueqiu.android:id/tv_search")))
