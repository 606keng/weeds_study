from appium.webdriver.common.mobileby import MobileBy

from appium_study.page.base_page import BasePage
# from appium_study.page.meber_invite_page import MeberInvitePage


class AddressListPage(BasePage):
    def click_addmember(self):
        from appium_study.page.meber_invite_page import MeberInvitePage
        # 滚动查找添加成员，并点击
        self.find(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("添加成员").'
                                                        'instance(0));').click()
        return MeberInvitePage(self._driver)