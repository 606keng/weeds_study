import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

class Testqiye():


    def setup_method(self, method):
        #声明一个变量，设置为chrometoptions
        chrome_opts=webdriver.ChromeOptions()
        #set address same as chrome debugging port
        chrome_opts.debugger_address="127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)


    # def teardown_method(self, method):
    #     self.driver.quit()

    def test_dou(self):

        #获取cookies，并保存到文件cookies.txt
        self.driver.get("https://work.weixin.qq.com")
        # sleep(20)
        # cookies = self.driver.get_cookies()
        # with open("cookies.txt","w",encoding="utf-8") as f:
        #     json.dump(cookies,f)
        with open("cookies.txt","r") as f:
            cookies:List[Dict] = json.load(f)
        cookies1 = getPureDomainCookies(cookies)
        print(cookies1)
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

        #self.driver.get("https://home.testing-studio.com/")
        self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
