from appium import webdriver
from pytest_study.test_appium.page.base_page import BasePage
from pytest_study.test_appium.page.main import Main


class App(BasePage):
    def start(self):
        _package = "com.xueqiu.android"
        _activity = ".view.WelcomeActivityAlias"
        if self._driver is None:
            cps = {}
            cps["platformName"] = "android"
            cps["deviceName"] = "doutest"
            cps["appPackage"] = _package
            cps["appActivity"] = _activity
            cps["autoGrantPermissions"] = True
            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cps)
            self._driver.implicitly_wait(10)
        else:
            self._driver.start_activity(_package,_activity)
        return self

    def main(self):
        return Main(self._driver)
