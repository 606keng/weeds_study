from appium import webdriver


class TestWebview:
    def setup(self):
        _package = "com.xueqiu.android"
        _activity = ".view.WelcomeActivityAlias"

        cps = {}
        #测试的平台，Android或iOS
        cps["platformName"] = "android"
        #链接的设备
        cps["deviceName"] = "doutest"
        #应用的包名
        cps["appPackage"] = _package
        #启动的页面名称
        cps["appActivity"] = _activity

        cps["autoGrantPermissions"] = True
        #设置为true，就不会清空应用的缓存数据
        cps["noReset"] = "true"
        #运行脚本时，不重启app
        # cps['dontStopAppOnReset'] = 'true'
        #定义支持中文
        cps["unicodeKeyBoard"] = 'true'
        #定义支持中文
        cps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cps)
        self.driver.implicitly_wait(100)
    def teardown(self):
        self.driver.quit()

    def test_webview(self):
        self.driver.find_element_by_xpath("//*[@text='交易']").click()
        print(self.driver.execute_script("return window.performance.timing"))