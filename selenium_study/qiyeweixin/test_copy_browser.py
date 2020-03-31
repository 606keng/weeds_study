import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class Testqiye():
    """
    复用浏览器：
        1.将Chrome.exe文件添加到环境变量中
        2.关闭所有的Chrome窗口
        3.重新打开dos窗口，输入chrome -remote-debugging-port=9222。回车后会弹出一个新的浏览器窗口
        4.打开企业微信，并登陆，不要关闭窗口
        5.在脚本中直接定位该页面的元素
    """
    def setup_method(self, method):
        # 声明一个变量，设置为chrometoptions
        chrome_opts = webdriver.ChromeOptions()
        # set address same as chrome debugging port
        chrome_opts.debugger_address = "127.0.0.1:9222"
        #将代理浏览器配置在webdriver中
        self.driver = webdriver.Chrome(options=chrome_opts)
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    def test_dou(self):

        # self.driver.get("https://home.testing-studio.com/")
        self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
