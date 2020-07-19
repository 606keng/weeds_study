#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: test_fixture002.py
@time: 2020/07/02
备注：将函数open作为参数传递给测试用例，用例执行前，执行yield之前的代码。用例执行后，执行yield之后的代码
"""
import pytest


# 默认scope等于function，作用域为函数级别，类似于setup、teardown.
# scope="module",作用域为module，类似于setup_module,teardown_module
# scope参数有四种选择：function（测试函数级别），class（测试类级别），
# module（测试模块“.py”级别），session（多个文件级别）。默认是function级别。
@pytest.fixture(scope="module")
def open():
    print("打开浏览器")
    yield
    print("关闭浏览器")


class TestFixture001:
    def test_001(self, open):
        print("登陆系统1")

    def test_002(self, open):
        print("登陆系统2")
