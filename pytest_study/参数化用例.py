#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: 参数化用例.py
@time: 2020/07/14
@remark：pytest参数化用了
"""
import pytest

# 要参数的变量使用string，参数化的值使用list[touple]
import yaml


@pytest.mark.parametrize("a,b", [(1, 2), (2, 3)])
def test_add(a, b):
    print(a + b)


# 要参数化的变量使用list，参数化的值使用tuople(touple)
@pytest.mark.parametrize(["a", "b"], ((1, 2), (3, 4)))
def test_add01(a, b):
    print(a + b)


# 使用yaml进行参数化
data = yaml.safe_load(open("data.yaml"))

@pytest.mark.parametrize("a,b",data)
def test_add02(a, b):
    print(a + b)
