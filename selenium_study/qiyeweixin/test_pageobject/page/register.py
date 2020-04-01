from selenium.webdriver.common.by import By

from selenium_study.qiyeweixin.test_pageobject.page.base_page import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.ID,"corp_name").send_keys("doudoudou")
        return True