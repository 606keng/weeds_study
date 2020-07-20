#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: test_assume.py
@time: 2020/07/19
@remark：用于练习多重校验第三方包pytest-assume
pytest-assume用于解决一条用例多个assert断言时，其中一个断言失败，该断言之后所有的断言都不会在进行判断的问题
"""
import pytest


# 第二条断言失败时，第三条依旧会校验
def test_assume():
    pytest.assume(1 == 1)
    pytest.assume(False)
    pytest.assume(True)

def test_aaa():
    print("aaa")

def test_ccc():
    print("ccc")

def test_bbb():
    print("bbb")