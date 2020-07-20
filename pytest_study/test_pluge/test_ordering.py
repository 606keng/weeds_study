#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: test_ordering.py
@time: 2020/07/19
@remark：
pytest用例默认的执行顺序根据方法在脚本中的位置自上而下执行。
如果需要修改该顺序，可以使用pytest-order
"""
import pytest


class TestOrder:
    # 在该脚本中，test_a第三个执行，因为其余三条用例都指定了执行顺序
    def test_a(self):
        print("a")

    # 该用例第二个执行
    @pytest.mark.run(order=2)
    def test_002(self):
        print("002")

    # 该用例第一个执行
    @pytest.mark.run(order=1)
    def test_001(self):
        print("001")

    # 该用例最后执行
    @pytest.mark.run(order=-1)
    def test_fianal(self):
        print("fianal")