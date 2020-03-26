from pytest_study.test_appium.page.base_page import BasePage

class App(BasePage):
    def start(self):
        if self._driver is None:
            pass