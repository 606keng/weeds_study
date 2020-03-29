from pytest_study.test_appium.page.base_page import BasePage
from pytest_study.test_appium.page.market import Market


class Main(BasePage):
    def goto_market(self):
        #使用..是因为方法要在testcase目录调用
        self.step("../page/main.yaml")
        return Market(self._driver)