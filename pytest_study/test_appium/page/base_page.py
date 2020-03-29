import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _black_list = []
    _error_count = 0
    _error_max = 10
    _params = {}
    # driver:WebDriver定义driver的入参类型为WebDriver
    def __init__(self, driver: WebDriver=None):
        self._driver = driver

    def find(self, by, locator=None):
        try:
            #如果by参数的类型是tuple，则执行if前面的语句，否则执行else后面的语句
            element = self._driver.find_element(*by) if isinstance(by,tuple) else self._driver.find_element(by,locator)
            self._error_count = 0
            return element
        #处理app弹窗问题
        except Exception as e:
            self._error_count+=1
            #如果错误次数大于最大错误次数，抛出异常
            if self._error_count > self._error_max:
                raise e
            #遍历黑名单，查找黑名单的元素，并点击
            for blcak in self._black_list:
                element = self._driver.find_element(*blcak)
                if len(element) > 0:
                    element[0].click()
                    return self.find(by,locator)
            raise e

    def step(self,path):
        with open(path, encoding='utf-8') as f:
            steps : list[dict] = yaml.safe_load(f)
            for step in steps:
                if 'by' in step.keys():
                    element = self.find(step['by'], step['locator'])
                if 'action' in step.keys():
                    if 'click' == step['action']:
                        element.click()
                    if 'send' == step['action']:
                        content : str = step['value']
                        #个人感觉参数应该为self._params.keys()
                        print(self._params)
                        for param in self._params:
                            content = content.replace("{%s}"%param , self._params[param])
                        element.send_keys(content)
