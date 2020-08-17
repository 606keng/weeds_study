from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium_study.base import Base


class ActionChains(Base):
    """
    鼠标事件练习
    """
    base_url = "http://sahitest.com/demo/label.htm"

    def case_click(self):
        self.click(By.XPATH, '//input[@value="click me"]', "click")
        self.click(By.XPATH, '//input[@value="right click me"]', "context_click")
        self.click(By.XPATH, '//input[@value="dbl click me"]', "double_click")

    def case_moveto(self):
        self.moveto(By.ID, "s-usersetting-top")

    def case_drag_drop(self):
        source = (By.ID, "dragger")
        target = (By.XPATH, '/test.html/body/div[2]')
        self.drag_drop(target=target, source=source)

    def case_key(self):
        """
        实现功能：进入页面，在username输入框中输入username，按键盘空格键，
        再输入dou，然后在按一下键盘删除键
        :return:
        """
        ele = (By.XPATH,'/test.html/body/label[1]/input')
        value1 = "doulihang"
        type1 = Keys.SPACE
        value2 = "dou"
        type2 = Keys.BACK_SPACE
        self.key(type=type1,ele=ele,value=value1)
        self.key(type=type2,ele=ele,value=value2)


class TestActionChains():
    def setup(self):
        self.action = ActionChains()

    def teardown(self):
        self.action._driver.quit()

    def test_case_click(self):
        """
        测试鼠标单击、右击、双击元素事件
        :return:
        """
        # self.driver.get("http://sahitest.com/demo/clicks.htm")
        # element_click = self.driver.find_element_by_xpath('//input[@value="click me"]')
        # element_right_click = self.driver.find_element_by_xpath('//input[@value="right click me"]')
        # element_dbl_click = self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        self.action.case_click()

        # 生成一个动作
        # action = ActionChains(self.driver)
        # # 将点击事件添加到动作中
        # action.click(element_click)
        # # 将右键点击事件添加到动作中
        # action.context_click(element_right_click)
        # # 将双击事件添加到动作中
        # action.double_click(element_dbl_click)
        # # 调用perform方法，执行添加到动作中的事件
        # action.perform()
        sleep(3)

    def test_moveto(self):
        """
        测试鼠标移动到某个元素上
        :return:
        """
        self.action.case_moveto()
        sleep(3)

    def test_drag_drop(self):
        """
        测试鼠标拖拽某个元素到另一个元素
        :return:
        """
        # self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        # element_drag = self.driver.find_element_by_id("dragger")
        # element_drop = self.driver.find_element_by_xpath("/test.html/body/div[2]")
        # action = ActionChains(self.driver)
        # drag_and_drop需要传入source, target，source为要拖拽的元素，target为要拖拽到哪个元素
        # action.drag_and_drop(element_drag, element_drop)
        """
        如下是drag_and_drop的源码，我们可以看出它实际是调用了click_and_hold和release方法
            def drag_and_drop(self, source, target):
                self.click_and_hold(source)
                self.release(target)
                return self
        """
        # 使用click_and_hold和release方法拖拽元素
        # action.click_and_hold(element_drag).release(element_drop)
        # action.perform()
        self.action.case_drag_drop()

    def test_keys(self):
        """
        实现功能：进入页面，在username输入框中输入username，按键盘空格键，
        再输入dou，然后在按一下键盘删除键
        :return:
        """
        self.action.case_key()
        sleep(3)
        # self.driver.get("http://sahitest.com/demo/label.htm")
        # element_keys = self.driver.find_element_by_xpath("/test.html/body/label[1]/input")
        # element_keys.click()
        # action = ActionChains(self.driver)
        # # 输入username,然后等待1秒
        # action.send_keys("username").pause(1)
        # # 按一下键盘空格键
        # action.send_keys(Keys.SPACE).pause(1)
        # # 输入dou
        # action.send_keys("dou").pause(1)
        # # 按一下删除键
        # action.send_keys(Keys.BACK_SPACE)
        # action.perform()
        # sleep(3)


if __name__ == '__main__':
    action = TestActionChains(True)
    action.test_case_click()
