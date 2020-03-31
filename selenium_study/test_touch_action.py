from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("w3c", False)

        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()
    def test_touchaction_scrollbottom(self):
        """
        打开Chrome
        向搜索框输入https://www.baidu.com/
        向搜索框输入selenium测试
        通过touchaction点击搜索框
        滑动到底部，点击下一页
        关闭Chrome
        :return:
        """
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys("selenium测试")
        el_search = self.driver.find_element_by_xpath('//*[@id="su"]')
        action = TouchActions(self.driver)
        #点击搜索按钮
        action.tap(el_search)
        #执行操作
        action.perform()
        #滑动到页面底部，scroll_from_element(self, on_element, xoffset, yoffset):
        #如果不清楚偏移量是多少时，要滑动到底部，尽量写大一些
        action.scroll_from_element(el_search,0,10000).perform()
        sleep(3)