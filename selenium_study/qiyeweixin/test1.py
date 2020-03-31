import json
from time import sleep
from typing import List, Dict

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTest():
    def setup_method(self, method):
        #声明一个变量，设置为chrometoptions
        chrome_opts=webdriver.ChromeOptions()
        #set address same as chrome debugging port
        chrome_opts.debugger_address="127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.implicitly_wait(3)

    # def teardown_method(self, method):
    #     self.driver.quit()

    def test_test(self):
        # sleep(15)
        # cookies=self.driver.get_cookies()
        # with open("cookies.txt", 'w') as f:
        #      json.dump(cookies, f)
        with open("cookies.txt", "r") as f:
            cookies:List[Dict]=json.load(f)
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap').click()