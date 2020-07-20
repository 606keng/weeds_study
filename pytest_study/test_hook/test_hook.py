#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: test_hook.py
@time: 2020/07/20
@remark：
"""
import pytest


class TestHook:
    @pytest.mark.parametrize("a", [1], ids=["整数"])
    def test_add1(self, a):
        print(f"001{a}")

    def test_add2(self):
        print("002")

    def test_add3(self):
        print("003")

    def test_div1(self):
        print("001")

