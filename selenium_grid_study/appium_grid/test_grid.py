import os

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestGrid:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "9.0"
        caps["appPackage"] = "com.server.carsir"
        caps["appActivity"] = ".garage.MainActivity"
        """
        deviceName:有一台设备时，
        
        """
        #运行脚本时，在命令行输入的udid。指定设备运行用例
        udid = os.getenv("udid")
        #
        caps["udid"] = udid
        # caps["noReset"] = True
        
        self.driver = webdriver.Remote("http://172.17.3.1:4444/wd/hub",caps)
        self.driver.implicitly_wait(10)
        

    def teardown(self):
        self.driver.quit()
    def test_case1(self):
        self.driver.find_element(MobileBy.ID,"com.server.carsir:id/phoneInput").send_keys("18700000001")
        self.driver.find_element(MobileBy.ID,"com.server.carsir:id/pwdInput").send_keys("111111")
        self.driver.find_element(MobileBy.ID,"com.server.carsir:id/submit").click()
