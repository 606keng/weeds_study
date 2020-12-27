import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class Testweb1():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    # def teardown(self):
    #     self.driver.quit()
    def test_switchwindows(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element_by_xpath('//*[@id="u1"]/a').click()
        self.driver.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a').click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        action = ActionChains(self.driver)
        #输入用户名
        self.driver.find_element_by_name('userName').send_keys('4561')
        #输入手机号
        ele=self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__phone"]')
        ele.send_keys('19092778754')
        #复制手机号框中的值
        # action.move_to_element(ele).click()
        action.move_to_element(ele).key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND)
        action.move_to_element(ele).key_down(Keys.COMMAND).send_keys('c').key_up(Keys.COMMAND)
        action.perform()
        action = ActionChains(self.driver)
        # ele=self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__phone"]')
        # ele.send_keys('19092778754')
        # ele.send_keys(Keys.COMMAND,'a')
        # ele.send_keys(Keys.COMMAND,'c')
        #输入密码框中的值
        oele=self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__password"]')
        oele.send_keys('li123456')
        action.move_to_element(oele)
        action.pause(1)
        # action.send_keys(Keys.NULL).pause(1)
        action.move_to_element(oele).send_keys(Keys.BACKSPACE).pause(1)
        action.move_to_element(oele).send_keys('7').pause(1)
        action.move_to_element(oele).send_keys(Keys.TAB).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND)
        action.perform()
        ele2 = self.driver.find_element_by_id('TANGRAM__PSP_4__verifyCode')
        # 关闭当前窗口，返回原来窗口
        # self.driver.close()
        print(ele2.get_attribute("value"))
        time.sleep(6)