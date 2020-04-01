from selenium.webdriver.common.by import By

from selenium_study.qiyeweixin.test_pageobject.page.base_page import BasePage
from selenium_study.qiyeweixin.test_pageobject.page.register import Register


class Login(BasePage):
    def scan(self):
        pass
    def goto_register(self):
        self.find(By.CSS_SELECTOR,".login_registerBar_link").click()
        return Register(self._driver)