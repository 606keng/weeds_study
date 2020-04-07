from selenium.webdriver.common.by import By

from selenium_study.selenium_pageobject_practice.page.base import Base
from selenium_study.selenium_pageobject_practice.page.member_list import MemberList


class AddMember(Base):
    def add_member(self):
        self._driver.find_element(By.CSS_SELECTOR,"#username").send_keys("高可乐")
        self._driver.find_element(By.CSS_SELECTOR,"#memberAdd_acctid").send_keys("gaokele")
        self._driver.find_element(By.CSS_SELECTOR,"#memberAdd_phone").send_keys("18200000000")
        self._driver.find_element(By.CSS_SELECTOR,".member_colRight_operationBar a:nth-child(2)").click()
        return MemberList(self._driver)
