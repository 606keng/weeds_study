from pytest_study.test_appium.page.base_page import BasePage
from pytest_study.test_appium.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.step("../page/market.yaml")
        return Search(self._driver)