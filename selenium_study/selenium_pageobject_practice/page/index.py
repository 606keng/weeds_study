from selenium.webdriver.common.by import By

from selenium_study.selenium_pageobject_practice.page.add_member import AddMember
from selenium_study.selenium_pageobject_practice.page.base import Base


class Index(Base):

    def goto_add_member(self):

        self._driver.find_element(By.CSS_SELECTOR,".index_service a:nth-child(1)").click()
        return AddMember(self._driver)
