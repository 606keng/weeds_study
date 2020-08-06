import logging
from typing import List
import yaml

from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


def exception_handle(fun):
    """
    对查找元素的函数进行装饰
    :param fun: 要查找元素的函数
    :return:
    """

    def magic(*args, **kwargs):
        # 标记instance的类型为BasePage
        instance: BasePage = args[0]
        try:
            # 执行被装饰的函数
            result = fun(*args, **kwargs)
            # 初始化定位报错次数为0
            instance._error_num = 0
            # 如果被装饰的函数未报错，直接返回被装饰的函数返回的结果
            return result

        except Exception as e:
            # 累加定位报错的次数
            instance._error_num += 1
            # 如果定位报错的次数大于定义的最大错误数，直接抛出异常
            if instance._error_num > instance._error_max:
                raise e

            # 对黑名单中的弹窗进行处理
            for e in instance._black_list:
                # 查找黑名单中的元素
                elements = instance._driver.find_elements(*e)
                # 如果黑名单中的元素数量大于0
                if len(elements) > 0:
                    # 点击所有查找到的黑名单元素
                    for element in elements:
                        element.click()
                    # 隐式等待10秒
                    instance._driver.implicitly_wait(10)
                    # 继续执行被装饰的函数
                    return fun(*args, **kwargs)

    return magic


class BasePage:
    logging.basicConfig(level=logging.INFO)
    _black_list = [
        (MobileBy.XPATH, "//*[@text='确定']"),
        (MobileBy.XPATH, "//*[@text='允许']")
    ]
    # 初始化定位错误的次数
    _error_num = 0
    # 定义定位错误的最大次数
    _error_max = 3
    # 创建一个字典，用于存储传入的参数
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    @exception_handle
    def find(self, locator, value):
        logging.info(locator)
        logging.info(value)
        # 如果locator为元组，执行self._driver.find_element(*locator)，否则执行self._driver.find_element(locator,value)
        return self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(
            locator, value)

    @exception_handle
    def finds(self, locator, value):
        logging.info(locator)
        logging.info(value)
        # 如果locator为元组，执行self._driver.find_elements(*locator)，否则执行self._driver.find_elements(locator,value)
        return self._driver.find_elements(*locator) if isinstance(locator, tuple) else self._driver.find_element(
            locator, value)

    # def find(self, locator, value):
    #     logging.info(locator)
    #     logging.info(value)
    #     try:
    #         # 如果locator为元组，执行self._driver.find_element(*locator)，否则执行self._driver.find_element(locator,value)
    #         return self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(
    #             locator, value)
    #     except Exception as e:
    #         # 处理弹框
    #         if self._error_num > self._error_max:
    #             raise e
    #         # 记录一直异常的次数
    #         self._error_num += 1
    #         # 对黑名单的弹窗进行处理
    #         for ele in self._black_list:
    #             elelist = self._driver.find_elements(*ele)
    #             if len(elelist) > 0:
    #                 elelist[0].click()
    #                 self.find(locator, value)
    #
    #         raise e

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
            if "by" in step.keys():
                by = step["by"]
                if by == "id":
                    element = self.find(MobileBy.ID, step["locator"])
                if by == "xpath":
                    element = self.find(MobileBy.XPATH, step["locator"])

            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    element.click()
                elif action in ["send", "input"]:
                    content: str = step["value"]
                    for key in self._params.keys():
                        content = content.replace("{%s}" % key, self._params[key])
                    element.send_keys(content)
                elif action == "text":
                    element.text
                elif action == "attribute":
                    element.get_attribute(step["value"])

    def read_yaml(self, file):
        """
        读取yaml文件
        :param file:
        :return:
        """
        with open(file,encoding="utf-8") as f:
            return yaml.safe_load(f)
