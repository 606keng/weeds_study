from appium.webdriver.common.mobileby import MobileBy

from appium_study.page.address_list_page import AddressListPage
from appium_study.page.base_page import BasePage


class Main(BasePage):

    def goto_message(self):
        pass

    def goto_addresslist(self):
        # 点击通讯录
        # self.find(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        self.steps("../steps/mainsteps.yml")
        return AddressListPage(self._driver)

    def goto_workbench(self):
        pass

    def goto_profile(self):
        pass
