from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    #把driver提取出来，
    _driver = ''
    base_url = ''
    def __init__(self, reuse=False):
        #如果reuse等于True，则复用浏览器
        if reuse == True:
            self.chrome_opt = webdriver.ChromeOptions()
            self.chrome_opt.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=self.chrome_opt)

        else:
            self._driver = webdriver.Chrome()
        if self.base_url != '':
            self._driver.get(self.base_url)
        self._driver.maximize_window()
        self._driver.implicitly_wait(5)


    def find(self, by, locator):
        return  self._driver.find_element(by,locator)

    def finds(self, by, locator):
        return  self._driver.find_elements(by,locator)
    def wait_for(self, fun):
        #如果fun返回的是true，那么就退出显示等待
        WebDriverWait(self._driver, 10).until(fun)