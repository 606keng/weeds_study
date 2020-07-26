from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class Base:
    _driver = ''
    _url = ''

    # driver要指定类型，python才能识别
    def __init__(self, driver: WebDriver = None):
        # 让pycharm知道有一个self.driver的实例属性
        self._driver = None
        # 如果driver为None，复用浏览器，初始化driver。在第一个子类第一次实例化时，driver为None
        # 非第一个子类第一次实例化时，需要在实例化时，将上一个子类的driver传递给调用的子类实例
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
