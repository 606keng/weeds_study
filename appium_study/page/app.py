from appium import webdriver
# from appium.webdriver import webdriver

from appium_study.page.base_page import BasePage
from appium_study.page.main import Main


class App(BasePage):
    def start(self):
        #启动app
        _package = "com.tencent.wework"
        _activity = ".launch.WwMainActivity"

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
        self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cps)
        self._driver.implicitly_wait(5)
        return self

    def stop(self):
        #停止app、
        pass

    def restart(self):
        #重启app
        pass
    def main(self):
        #
        return Main(self._driver)