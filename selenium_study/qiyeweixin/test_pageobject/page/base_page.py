from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ''
    #让pycharm知道有一个实例变量：_driver
    _driver = ''
    print(_base_url)
    def __init__(self, driver:WebDriver = None):
        if driver is None:
            self._driver = webdriver.Chrome()
        #从上一个页面跳转的话，会将driver以参数的形式传入，不用每跳一个页面都要初始化一个webdriver
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)
        self._driver.implicitly_wait(5)
        self._driver.maximize_window()

    def find(self, by, locator):
        return self._driver.find_element(by,locator)