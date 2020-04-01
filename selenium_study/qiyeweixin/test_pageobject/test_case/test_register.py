from selenium_study.qiyeweixin.test_pageobject.page.main import Main


class TestRegister:
    def setup(self):
        self.main = Main()

    def test_register(self):
        self.main.goto_register().register()
