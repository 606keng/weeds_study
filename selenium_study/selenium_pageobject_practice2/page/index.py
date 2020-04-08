from selenium.webdriver.common.by import By

from selenium_study.selenium_pageobject_practice2.page.add_member import AddMember
from selenium_study.selenium_pageobject_practice2.page.base import Base


class Index(Base):
    base_url = "https://work.weixin.qq.com/wework_admin/frame"
    def goto_add_member(self):
        self.find(By.ID,'menu_contacts').click()
        def wait(driver):
            ele_len = len(self.finds(By.ID, 'username'))
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            if ele_len < 1:
                self.find(By.CSS_SELECTOR,".js_has_member>div:nth-child(1) .js_add_member").click()
            return ele_len >= 1
        self.wait_for(wait)

        return AddMember(reuse=True)
