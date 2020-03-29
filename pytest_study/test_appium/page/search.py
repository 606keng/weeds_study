from pytest_study.test_appium.page.base_page import BasePage


class Search(BasePage):
    def search(self,value):
        self._params["value"] = value
        self.step("../page/search.yaml")