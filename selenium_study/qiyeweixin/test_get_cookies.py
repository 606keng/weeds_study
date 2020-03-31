import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

class Testqiye():


    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)


    # def teardown_method(self, method):
    #     self.driver.quit()

    def test_dou(self):

        #获取cookies，并保存到文件cookies.txt
        #获取cookies的方法有两种，1.通过复用浏览器获取。2.通过等待20秒操作手动操作浏览器使其生成预期的cookies
        self.driver.get("https://work.weixin.qq.com")
        #等待20秒，手动登陆企业微信
        # sleep(20)
        #获取cookies，将cookies保存到本地
        # cookies = self.driver.get_cookies()
        # with open("cookies.txt","w",encoding="utf-8") as f:
        #     json.dump(cookies,f)
        #加载cookies
        with open("cookies.txt","r") as f:
            cookies:List[Dict] = json.load(f)
        cookies1 = getPureDomainCookies(cookies)
        #将cookies添加到webdriver中
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        #免登陆访问企业微信首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

        #self.driver.get("https://home.testing-studio.com/")
        self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
