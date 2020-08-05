from appium import webdriver
# from appium.webdriver import webdriver

from appium_study.page.base_page import BasePage
from appium_study.page.main import Main
from carsir_ui.page.carsir.login.login import Login
from carsir_ui.utils.basepath import ConfigPath


class App(BasePage):
    def start_carsir(self):
        # 启动app
        _package = "com.tencent.wework"
        _activity = ".activity.StartPageActivity"

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

    def main(self):
        #
        return Main(self._driver)

    def login(self):
        return Login(self._driver)
