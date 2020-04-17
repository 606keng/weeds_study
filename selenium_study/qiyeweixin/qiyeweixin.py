from selenium import webdriver

from selenium_study.base import Base


class TestQiYe:
    def setup(self):
        chrome_opts = webdriver.ChromeOptions()
        chrome_opts.debugger_address="127.0.0.1:9999"
        self.driver = webdriver.Chrome(options=chrome_opts)
    def test_login(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]').click()
