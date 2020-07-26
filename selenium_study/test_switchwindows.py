from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from base import Base


class SwitchWindows(Base):
    """
    窗口切换练习
    打开百度
    点击登录
    弹框中点击立即注册，输入用户名账号
    返回刚才的登录页面，点击关闭登录弹窗
    """
    # def setup(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.implicitly_wait(5)
    #     self.driver.maximize_window()
    # def teardown(self):
    #     self.driver.quit()
    base_url = "https://www.baidu.com/"

    def case_switchwindows(self):
        self.operation_element((By.LINK_TEXT, "登录"), "c")
        self.operation_element((By.LINK_TEXT, "立即注册"), "c")
        self.switch_window(-1)
        self.operation_element((By.NAME, "userName"), "s", value="doulihang")
        self.switch_window(0)
        self.operation_element((By.ID, "TANGRAM__PSP_4__closeBtn"), "c")
        # self.driver.find_element_by_link_text("登录").click()
        # #打印当前窗口
        # print(self.driver.current_window_handle)
        # self.driver.find_element_by_link_text("立即注册").click()
        # #打印当前窗口
        # print(self.driver.current_window_handle)
        # #打印所有窗口
        # print(self.driver.window_handles)
        # #获取所有窗口的列表
        # windows = self.driver.window_handles
        # #切换到最后一个窗口
        # self.driver.switch_to_window(windows[-1])
        # self.driver.find_element_by_name("userName").send_keys("doulihang")
        # sleep(5)
        # #切换到第一个窗口
        # self.driver.switch_to_window(windows[0])
        # self.driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
        sleep(3)


class TestSwitchWindows:
    def setup(self):
        self.switch = SwitchWindows()

    def teardown(self):
        self.switch._driver.quit()

    def test_switch(self):
        self.switch.case_switchwindows()
