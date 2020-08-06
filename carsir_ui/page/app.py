from appium import webdriver
# from appium.webdriver import webdriver
from carsir_ui.page.base_page import BasePage
from carsir_ui.utils.basepath import ConfigPath


class App(BasePage):
    def start_carsir(self):
        # 启动app
        cps = self.read_yaml(ConfigPath + r"\carsir.yaml")

        self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cps)
        self._driver.implicitly_wait(5)
        return self

    def stop(self):
        # 停止app、
        pass

    def restart(self):
        # 重启app
        pass

    def login(self):
        from carsir_ui.page.carsir.login.login import Login
        return Login(self._driver)
