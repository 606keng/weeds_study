from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestMember:
    def setup_class(self):
        _package = "com.tencent.wework"
        _activity = ".launch.WwMainActivity"

        cps = {}
        # 测试的平台，Android或iOS
        cps["platformName"] = "android"
        # 链接的设备
        cps["deviceName"] = "doutest"
        # 应用的包名
        cps["appPackage"] = _package
        # 启动的页面名称
        cps["appActivity"] = _activity

        cps["autoGrantPermissions"] = True
        # 设置为true，就不会清空应用的缓存数据
        cps["noReset"] = "true"
        # 运行脚本时，不重启app
        # cps['dontStopAppOnReset'] = 'true'
        # 定义支持中文
        cps["unicodeKeyBoard"] = 'true'
        # 定义支持中文
        cps['resetKeyBoard'] = 'true'
        print(cps)
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cps)
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.quit()
    #调用add_member方法时，调用方执行前，执行yield之前的代码，调用方执行完毕后，再执行yield后面的代码
    @pytest.fixture()
    def add_member(self):
        yield
        self.driver.find_element_by_id("com.tencent.wework:id/gpp").click()

    @pytest.mark.parametrize(("username", "gender","phone_number"),
                             [
                                 ("test001", "男","15600000000"),
                                 ("test002", "男","15600000001")
                              ])
    #调用add_member方法
    def test_add_member(self,add_member,username,gender,phone_number):
        """
        打开企业微信（提前登录）
        进入通讯录
        滚动查找添加成员并点击
        点击手动输入添加
        输入姓名
        选择性别
        输入手机号
        点击选择部门
        点击确定
        点击保存联系人
        点击返回
        点击消息
        :return:
        """
        #点击通讯录
        self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        #滚动查找添加成员，并点击
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("添加成员").'
                                                        'instance(0));').click()
        #点击手动添加员工
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/c56").click()
        #输入姓名
        self.driver.find_element_by_xpath('//*[@text="姓名　"]/..//*[@resource-id="com.tencent.wework:id/ase"]').send_keys(username)
        #点击性别
        self.driver.find_element_by_xpath('//*[@text="性别"]/..//*[@resource-id="com.tencent.wework:id/ate"]').click()
        if gender == "男":
            self.driver.find_element_by_xpath('//*[@text="男"]').click()
        else:
            self.driver.find_element_by_xpath('//*[@text="女"]').click()
        #输入手机号
        self.driver.find_element_by_id("com.tencent.wework:id/emh").send_keys(phone_number)
        #点击保存
        self.driver.find_element_by_id("com.tencent.wework:id/gq7").click()
        sleep(2)
        #打印当前页面的源码
        # print(self.driver.page_source)
        #获取添加成功提示
        sucess_msg=self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        assert sucess_msg == "添加成功"


    @pytest.mark.parametrize(("username"),
                             [
                                 ("test001"),
                                 ("test002")
                              ])
    def test_delete_member(self,username):
        """
        点击通讯录
        选择已test开头的用户，并点击
        点击更多
        点击编辑员工
        点击删除成员
        获取删除成功toast
        :param add_member:
        :return:
        """
        # 点击通讯录
        self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        #点击要删除的用户
        self.driver.find_element_by_xpath(f'//*[@text="{username}"]').click()
        #点击更多
        self.driver.find_element_by_id("com.tencent.wework:id/gq0").click()
        #点击编辑成员
        self.driver.find_element_by_id("com.tencent.wework:id/axr").click()
        #点击删除成员
        self.driver.find_element_by_id("com.tencent.wework:id/drk").click()
        #点击确定
        self.driver.find_element_by_id("com.tencent.wework:id/b89").click()
        # 点击消息
        self.driver.find_element_by_xpath('//*[@text="消息"]').click()
        # 点击通讯录
        self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()

        sleep(2)
        elements = self.driver.find_elements_by_android_uiautomator(f'new UiSelector().textStartsWith("{username}")')
        assert len(elements) == 0


