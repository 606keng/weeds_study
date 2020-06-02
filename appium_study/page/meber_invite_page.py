# from appium_study.page.address_list_page import AddressListPage
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from appium_study.page.base_page import BasePage
# from appium_study.page.contact_add_page import ContactAddPage


class MeberInvitePage(BasePage):
    def click_addmenual(self):
        from appium_study.page.contact_add_page import ContactAddPage
        # 点击手动添加员工
        self.find(MobileBy.ID, "com.tencent.wework:id/c56").click()
        return ContactAddPage(self._driver)
    def click_back(self):
        from appium_study.page.address_list_page import AddressListPage
        self._driver.back()
        return AddressListPage(self._driver)
    def veriy_toast(self):
        self.find(MobileBy.XPATH,"//*[@class='android.widget.Toast']")
        return self