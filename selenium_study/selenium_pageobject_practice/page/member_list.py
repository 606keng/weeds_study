from time import sleep

from selenium.webdriver.common.by import By

from selenium_study.selenium_pageobject_practice.page.base import Base
# from selenium_study.selenium_pageobject_practice.page.index import Index


class MemberList(Base):
    def get_member(self):
        return self._driver.find_element(By.CSS_SELECTOR,
                                         "#member_list tr:nth-child(3) td:nth-child(2)").text

    def delete_member(self):
        members : list = self._driver.find_elements(By.CSS_SELECTOR, "#member_list tr")
        for i in range(1,len(members)+1):
            name = self._driver.find_element(By.CSS_SELECTOR, "#member_list tr:nth-child(%d) td:nth-child(2)" %i).text
            print(name)
            if name == "高可乐":
                self._driver.find_element(By.CSS_SELECTOR, "#member_list tr:nth-child(%d) td:nth-child(1)" %i).click()

                self._driver.find_element(By.CSS_SELECTOR,".js_operationBar_footer a:nth-child(5)").click()

                self._driver.find_element_by_xpath('//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]').click()

                break
        self._driver.find_element_by_id('menu_index').click()
