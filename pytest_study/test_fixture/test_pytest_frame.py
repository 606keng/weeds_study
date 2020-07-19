#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: test_pytest_frame.py
@time: 2020/07/02
备注：该文件用于pytest框架结构测试
"""
import pytest

def setup_module(self):
    print("开始执行setup_module")


def setup_function(self):
    """
    该方法不能在类中
    :param self:
    :return:
    """
    print("开始执行setup_function")


def teardown_module(self):
    print("开始执行teardown_module")


def teardown_function(self):
    print("开始执行teardown_function")

def test_003():
    print(3)


class TestPytestFrame:
    """
    执行该类时，执行步骤为setup_module-》setup_class-》setup-》teardown-》setup-》teardown-》teardown_class-》teardown_module
    注意，由于该类中有两条测试用例，所以setup、teardown执行两次，类中有多少测试用例，setup、teardown就执行多少次
    """
    def setup_class(self):
        print("开始执行setup_class")

    def setup(self):
        print("开始执行setup")

    def teardown_class(self):
        print("开始执行teardown_class")

    def teardown(self):
        print("开始执行teardown")

    def test_001(self):
        """
        执行该方法时，执行步骤为setup_module-》setup_class-》setup-》teardown-》teardown_class-》teardown_module
        :return:
        """
        print(1)

    def test_002(self):
        print(2)
