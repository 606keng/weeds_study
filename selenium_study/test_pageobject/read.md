#企业微信首页pageobject练习
##封装basepage
定义类变量url用于后期子类中url的传入

定义构造函数，传入driver，且driver的默认值为None。构造函数中定义变量self._driver="",
当driver等于None时，对self.driver进行初始化，当driver不为空时，self.driver
等于driver。此处传入的driver用于页面之间跳转时，继续使用已有driver，避免driver的重复启动

定义find函数，入参为by，locator。返回self._driver.find_element，避免page中重复调用self._driver.find_element

##封装page
根据首页功能，需要封装三个page，分别为main，register，login

###封装mainpage
创建main模块，定义Main类，并继承BasePage,定义两个方法。
对父类中的url进行改写
####goto_register
用于封装功能：点击注册按钮，跳转到注册页面
实现逻辑：由于继承BasePage，子类可以使用父类的方法，调用self.find()方法点击立即注册按钮。返回Register类，并将self._driver作为
入参传递。

###封装registerpage
封装过程同mainpage

###封装loginpage
封装过程同mainpage

###注册用例编写
完全模拟用户操作，在setup中定义self.main=Main()
定义test_register，模拟用户操作点击立即注册，跳转到注册页面，输入注册信息，点击提交。self.main.goto_register().register()