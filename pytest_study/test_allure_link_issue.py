#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: test_allure_link_issue.py
@time: 2020/07/15
@remark：allure关联链接
"""
import allure


# 在allure报告中展示该链接，链接的名称为百度
@allure.link("http://www.baidu.com", name="百度")
def test_allure_link():
    print("link")


TEST_CASE_LINK = "https://blog.csdn.net/doulihang/article/details/107328104"


# 在allure报告中展示该链接，链接的名称为登录成功
@allure.testcase(TEST_CASE_LINK, "登录成功")
def test_login_success():
    print("login success")


# 执行命令pytest test_allure_link_issue.py --allure-link-pattern=issue:bug管理系统的链接/{} --alluredir=result/5
@allure.issue("doulihang", "bug")
def test_bug():
    print("bug")
