#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: test_fixture004.py
@time: 2020/07/02
备注：使用pytestmark=pytest.mark.usefixtures("open_everyone")，让该模块中所有的用例的前置函数都为open_everyone
"""
import pytest

pytestmark = pytest.mark.usefixtures("open_everyone")


class TestFixture001:
    def test_001(self):
        print("登陆系统1")

    def test_002(self):
        print("登陆系统2")
