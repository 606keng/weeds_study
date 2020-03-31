from time import sleep

from selenium import webdriver


class TestSwitchWindows:
    """
    打开百度
    点击登录
    弹框中点击立即注册，输入用户名账号
    返回刚才的登录页面，点击登录
    输入用户名和密码，点击登录
    """
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()

    def test_switchwindows(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        #打印当前窗口
        print(self.driver.current_window_handle)
        self.driver.find_element_by_link_text("立即注册").click()
        #打印当前窗口
        print(self.driver.current_window_handle)
        #打印所有窗口
        print(self.driver.window_handles)
        #获取所有窗口的列表
        windows = self.driver.window_handles
        #切换到最后一个窗口
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element_by_name("userName").send_keys("doulihang")
        sleep(5)
        #切换到第一个窗口
        self.driver.switch_to_window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
        sleep(3)

