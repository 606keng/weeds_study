from time import sleep

from selenium.webdriver.common.by import By

from selenium_study.selenium_pageobject_practice.page.base import Base


# from selenium_study.selenium_pageobject_practice.page.index import Index


class MemberList(Base):
    def get_member(self):
        # 获取id为member_list的tr子元素的父元素的第一个孩子，该孩子的td子元素的父元素的第二个孩子
        return self._driver.find_element(By.CSS_SELECTOR,
                                         "#member_list tr:nth-child(3) td:nth-child(2)").text

    def delete_member(self):
        # 获取成员列表
        members: list = self._driver.find_elements(By.CSS_SELECTOR, "#member_list tr")

        # 遍历成员列表，如果有姓名等于高可乐的直接删除
        for i in range(1, len(members) + 1):
            name = self._driver.find_element(By.CSS_SELECTOR, "#member_list tr:nth-child(%d) td:nth-child(2)" % i).text
            print(name)
            if name == "高可乐":
                self._driver.find_element(By.CSS_SELECTOR, "#member_list tr:nth-child(%d) td:nth-child(1)" % i).click()

                self._driver.find_element(By.CSS_SELECTOR, ".js_operationBar_footer a:nth-child(5)").click()

                self._driver.find_element_by_xpath('//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]').click()

                break
        self._driver.find_element_by_id('menu_index').click()
