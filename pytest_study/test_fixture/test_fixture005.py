#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: test_fixture005.py
@time: 2020/07/02
备注：@pytest.fixture(autouse="true"),让模块中每个用例自动添加login为前置函数，无需将前置函数作为参数传递给用例
"""
import pytest


@pytest.fixture(autouse="true")
def login():
    print("这是一个登陆方法")


class TestFixture001:
    def test_001(self):
        print("需要登陆1")

    def test_002(self):
        print("需要登陆2")
