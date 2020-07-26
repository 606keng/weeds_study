from selenium.webdriver.common.by import By

from selenium_study.base import Base


class Frame(Base):
    base_url = "https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"

    def case_frame(self):
        """
        frame练习
        进入指定网站
        打印frame下的指定元素文本信息
        再打印出frame外的指定元素文本信息
        :return:
        """
        # self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # #进入frame节点
        # self.driver.switch_to.frame("iframeResult")
        # print(self.driver.find_element_by_id("droppable").text)
        # #退出frame节点，与self.driver.switch_to_default_content()效果相同
        # self.driver.switch_to.parent_frame()
        #
        # print(self.driver.find_element_by_id("submitBTN").text)

        self.frame(locator="iframeResult")
        print(self.find(By.ID, "droppable").text)
        self.frame(operation="out")
        print(self.find(By.ID, "submitBTN").text)


class TestFrame:
    def setup(self):
        self.frame = Frame()

    def teardown(self):
        self.frame._driver.quit()

    def test_frame(self):
        self.frame.case_frame()