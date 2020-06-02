from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from appium_study.page.base_page import BasePage
# from appium_study.page.meber_invite_page import MeberInvitePage


class ContactAddPage(BasePage):
    def input_name(self,username):
        #输入姓名
        self.find(MobileBy.XPATH,'//*[@text="姓名　"]/..//*[@resource-id="com.ten'
                                                'cent.wework:id/ase"]').send_keys(username)
        return self
    def set_gender(self,gender):
        # 点击性别
        self.find(MobileBy.XPATH, '//*[@text="性别"]/..//*[@resource-id="com.tencent.wework:id/ate"]').click()
        if gender == "男":
            self.find(MobileBy.XPATH, '//*[@text="男"]').click()
        else:
            self.find(MobileBy.XPATH, '//*[@text="女"]').click()
        return self
    def input_phone(self,phone_number):
        # 输入手机号
        self.find(MobileBy.ID,"com.tencent.wework:id/emh").send_keys(phone_number)
        return self
    def click_save(self):
        from appium_study.page.meber_invite_page import MeberInvitePage
        # 点击保存
        self.find(MobileBy.ID, "com.tencent.wework:id/gq7").click()
        return MeberInvitePage(self._driver)
