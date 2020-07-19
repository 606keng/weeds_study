#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: test_pytest_assume.py
@time: 2020/07/02
备注：用于练习pytest-assume，使用前需要安装第三方包pytest-assume，使用场景：用例一条失败时，其他断言仍然可以执行
"""
import pytest


class TestPytestAssume:
    def test_001(self):
        """
        pytest.assume:有多条断言时，当断言失败时，其他断言依旧会校验
        :return:
        """
        pytest.assume(1 == 2)
        pytest.assume(2 == 3)
        pytest.assume(2 == 2)

    def test_002(self):
        """
        assert:有多条断言时，当断言失败时，失败断言之后的断言不会再校验
        :return:
        """
        assert 1 == 2
        assert 2 == 3
        assert 2 == 2
