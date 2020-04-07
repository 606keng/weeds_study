from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class Base:
    _driver = ''
    _url = ''
    def __init__(self, driver : WebDriver = None):
        if driver is None:
            self.chrome_opt = webdriver.ChromeOptions()
            self.chrome_opt.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=self.chrome_opt)
            if self._url != '':
                self._driver.get(self._url)
        else:
            self._driver = driver
        self._driver.maximize_window()
        self._driver.implicitly_wait(5)
