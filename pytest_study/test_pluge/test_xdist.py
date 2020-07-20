#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: test_xdist.py
@time: 2020/07/19
@remark：使用pytest-xdist并发执行用例,并发5个执行用例：pytest test_xdist.py -n 5
"""
from datetime import time
from time import sleep

import pytest


class TestXdist:
    @pytest.mark.parametrize("a", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_001(self, a):
        sleep(1)
        print(a)
