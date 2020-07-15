#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: test_allure_fixture.py
@time: 2020/07/15
@remark：学习allure fixture的基本使用
1.如果用例中包含登录和退出模块，只想执行退出功能，
执行命令：pytest test_allure_fixture.py --allure-features "登录" --alluredir=result01/3
2.如果只想运行登录成功这条用例，
执行命令： pytest test_allure_fixture.py --allure-stories "输入正确的用户名及密码，登录成功" --alluredir=result01/3
"""
import allure

"""
功能模块：登录
    用例1：输入正确的用户名和密码，登录成功
        步骤：
            输入用户名：admin
            输入密码：123456
            点击登录
    用例2：输入错误的用户名和密码，登录失败
            输入用户名：admin
            输入密码：111111
            点击登录
"""


# 定义功能模块名称
@allure.feature("登录")
class TestLogin:
    # 定义用例名称
    @allure.story("输入正确的用户名及密码，登录成功")
    def test_login_success(self):
        # 定义步骤名称
        with allure.step("输入用户名：admin"):
            print("admin")
        with allure.step("输入密码：123456"):
            print("123456")
        with allure.step("点击登录"):
            print("登录")

    @allure.story("输入错误的用户名及密码，登录失败")
    def test_login_fail(self):
        with allure.step("输入用户名：admin"):
            print("admin")
        with allure.step("输入密码：111111"):
            print("123456")
        with allure.step("点击登录"):
            print("登录")


# 定义功能模块名称
@allure.feature("退出")
class TestLoginOut:
    # 定义用例名称
    @allure.story("用户点击退出，页面正常退出")
    def test_loginout_success(self):
        with allure.step("点击退出"):
            print("退出")
