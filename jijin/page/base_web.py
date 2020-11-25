import logging
from time import sleep
from typing import List

import yaml
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

from jijin.utils.basepath import DriverPath


class BaseWeb:
    # 把driver提取出来，
    _driver = ''
    base_url = ''
    # 创建一个字典，用于存储传入的参数
    _params = {}

    def __init__(self, reuse=True, touch_option=True):
        """

        :param reuse: 如果reuse等于True，则复用driver
        :param touch_option: 如果touch_option等于True，则使用重新定义适合下拉滑动的浏览器
        """
        driver_path = DriverPath + "/chromedriver"
        if reuse:
            if not touch_option:
                self.chrome_opt = webdriver.ChromeOptions()
                # 启动chrome：chrome -remote-debugging-port=9222
                self.chrome_opt.debugger_address = "127.0.0.1:9222"
                self._driver = webdriver.Chrome(executable_path=driver_path, options=self.chrome_opt)
            else:
                self.chrome_opt = webdriver.ChromeOptions()
                self.chrome_opt.debugger_address = "127.0.0.1:9222"
                self.chrome_opt.add_experimental_option("w3c", False)
                self._driver = webdriver.Chrome(executable_path=driver_path, options=self.chrome_opt)

        else:
            if not touch_option:
                self._driver = webdriver.Chrome(executable_path=driver_path)
            else:
                self.chrome_opt = webdriver.ChromeOptions()
                self.chrome_opt.add_experimental_option("w3c", False)
                self._driver = webdriver.Chrome(executable_path=driver_path, options=self.chrome_opt)
        if self.base_url != '':
            self._driver.get(self.base_url)
        self._driver.maximize_window()
        self._driver.implicitly_wait(5)

    def click_find(self, locator, value):
        # 如果locator为元组，执行self._driver.find_element(*locator)，否则执行self._driver.find_element(locator,value)
        return self.wait_for(expected_conditions.element_to_be_clickable(**locator)) if isinstance(locator,
                                                                                                   tuple) else self.wait_for(
            expected_conditions.element_to_be_clickable((locator, value)))

    def find(self, locator, value):
        # 如果locator为元组，执行self._driver.find_elements(*locator)，否则执行self._driver.find_elements(locator,value)
        return self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(
            locator, value)

    def finds(self, locator, value):
        # 如果locator为元组，执行self._driver.find_elements(*locator)，否则执行self._driver.find_elements(locator,value)
        return self._driver.find_elements(*locator) if isinstance(locator, tuple) else self._driver.find_elements(
            locator, value)

    def steps(self, file):
        """
        用于封装测试步骤驱动
        :param file: 包含测试步骤的yaml文件路径
        :return:
        """
        if isinstance(file, list):
            self.run_step(file)
        else:
            with open(file, encoding="utf-8") as f:
                steps: List[dict] = yaml.safe_load(f)
                self.run_step(steps)

    def run_step(self, steps):
        element: WebElement
        for step in steps:
            logging.info(step)
            if "ele_index" in step.keys():
                if "by" in step.keys():
                    by = step["by"]
                    if by == "id":
                        element = self.finds(By.ID, step["locator"])[step["ele_index"]]
                    if by == "xpath":
                        element = self.finds(By.XPATH, step["locator"])[step["ele_index"]]
            elif "ele_index" not in step.keys():
                if "by" in step.keys():
                    by = step["by"]
                    if step["action"] == "click":
                        if by == "id":
                            element = self.click_find(By.ID, step["locator"])
                        if by == "xpath":
                            element = self.click_find(By.XPATH, step["locator"])
                    else:
                        if by == "id":
                            element = self.find(By.ID, step["locator"])
                        if by == "xpath":
                            element = self.find(By.XPATH, step["locator"])
                        # 如果定位方式为text时，使用滚动查找,支持模糊查询
                        if by == "text":
                            content: str = step["locator"]
                            if "{" in content:
                                for key in self._params.keys():
                                    content = content.replace("{%s}" % key, self._params[key])
                                element = self.scroll_find(content)
                            else:
                                element = self.scroll_find(content)

            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    element.click()
                elif action in ["send", "input"]:
                    content: str = step["value"]
                    for key in self._params.keys():
                        content = content.replace("{%s}" % key, str(self._params[key]))
                    element.send_keys(content)
                elif action == "clear":
                    element.clear()
                elif action == "text":
                    element.text
                elif action == "attribute":
                    element.get_attribute(step["value"])

    def read_yaml(self, path, file):
        """
        读取yaml文件
        :param file:
        :return:
        """
        with open(path + "/" + file, encoding="utf-8") as f:
            return yaml.safe_load(f)

    def wait_for(self, fun):
        # 如果fun返回的是true，那么就退出显示等待
        return WebDriverWait(self._driver, 10).until(fun)

    def operation_element(self, ele, operation, value=None):
        """
        常用的操作元素方法
        :param ele: 要操作的元素
        :param operation: 要操作的方法
        :return:
        """
        ele = self.find(*ele)
        if operation in ["click", "c"]:
            ele.click()
        elif operation in ["send_keys", "s"]:
            ele.send_keys(value)

    def click(self, by, locator, type="click"):
        """
        用于模拟鼠标操作，单击/右键/双击
        :param by:定位类型
        :param locator:元素位置
        :param type:点击鼠标的类型，目前支持三种类型，单击，右键，双击
        :return:
        """
        ele = self.find(by, locator)
        action = ActionChains(self._driver)
        if type == "click":
            action.click(ele)
            action.perform()
        elif type == "context_click":
            action.context_click(ele)
            action.perform()
        elif type == "double_click":
            action.double_click(ele)
            action.perform()

    def moveto(self, by, locator):
        """
        用于将鼠标移动到元素上
        :param by: 定位类型
        :param locator: 元素位置
        :return:
        """
        ele = self.find(by, locator)
        action = ActionChains(self._driver)
        action.move_to_element(ele)
        action.perform()

    def drag_drop(self, target, source):
        """
        鼠标拖拽某个元素到另一个元素
        :param target: 要拖拽的终点元素，格式：(By.ID, "dragger")
        :param source: 要拖拽的元素，格式：(By.ID, "dragger")
        :return:
        """
        target = self.find(*target)
        source = self.find(*source)
        action = ActionChains(self._driver)
        action.click_and_hold(source).release(target)
        action.perform()

    def key(self, type, seconds=1, ele: tuple = None, value=None):
        """
        模拟键盘操作，如回车，空格，F1等等
        :param type: 键盘操作的类型
        :param seconds: 操作后等待时间，默认为1
        :param ele: 要操作的元素，默认为None，该值一般在输入框操作时填写
        :param value: 要操作的值：默认为None，该值一般在输入框操作时填写
        :return:
        """
        action = ActionChains(self._driver)
        if value and ele:
            ele = self.find(*ele)
            ele.click()
            action.send_keys(value).pause(seconds)
            action.send_keys(type)
            action.perform()
        else:
            action.send_keys(type)
            action.perform()

    def upload_file(self, ele, file):
        """
        简单的通过输入框上传文件的封装，更复杂的场景后续再封装
        :param ele: 上传文件的输入框
        :param file: 要上传的文件路径
        :return:
        """
        self.operation_element(ele, "s", file)

    def frame(self, locator=None, operation="to"):
        """
        操作frame，进入或退出
        :param locator: frame ID
        :param operation: 操作，默认为进入frame。传入其他值，退出frame
        :return:
        """
        if operation == "to":
            self._driver.switch_to.frame(locator)
        else:
            self._driver.switch_to.parent_frame()

    def switch_window(self, num=0):
        """
        切换到指定的窗口
        :param num: 要切换的窗口的下标，0表示第一个
        :return:
        """
        # 获取所有的窗口
        windows = self._driver.window_handles
        # 切换到指定下标的窗口
        self._driver.switch_to.window(windows[num])

    def touch(self, ele, start=0, end=1000):
        """
        注意：调用该方法时，对类进行实例化时，一定要传入参数touch_option=False
        下拉操作,
        :param ele: 要点击的元素，对元素无特殊要求，只要在当前页面中即可
        :param start: 下拉的开始坐标，默认为0
        :param end: 下拉的结束坐标，默认为1000，可以根据实际情况输入
        :return:
        """
        ele = self.find(*ele)
        action = TouchActions(self._driver)
        # 点击元素
        action.tap(ele)
        # 执行操作
        action.perform()
        # 滑动到页面底部，scroll_from_element(self, on_element, xoffset, yoffset):
        # 如果不清楚偏移量是多少时，要滑动到底部，尽量写大一些
        action.scroll_from_element(ele, start, end).perform()

    def accept_alter(self):
        """
        接受alter
        :return:
        """
        # self.wait_for显式等待，EC.alert_is_present()判断alter是否出现
        self.wait_for(EC.alert_is_present())
        alter = self._driver.switch_to_alert()
        alter.accept()

    def close(self):
        self._driver.close()

    def refresh_web(self):
        self._driver.refresh()

    def scroll(self,num=1000):
        js = f"var q=document.documentElement.scrollTop={num}"

        self._driver.execute_script(js)
