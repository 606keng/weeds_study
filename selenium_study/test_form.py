from time import sleep

from selenium import webdriver


class TestForm:
    """
    练习表单操作，进入testhome登录页面，输入用户名密码，勾选记住密码，点击登录
    """
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys("doulihang")
        self.driver.find_element_by_id("user_password").send_keys("doudoudo")
        self.driver.find_element_by_id("user_remember_me").click()
        self.driver.find_element_by_name("commit").click()
        sleep(5)