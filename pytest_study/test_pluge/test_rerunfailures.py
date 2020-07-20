#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: test_rerunfailures.py
@time: 2020/07/19
@remark：reruns不能结合setup_class使用
    用例失败时，重新运行5遍：pytest test_rerunfailures.py --reruns 5
    用例失败时，重新运行5遍,用例执行时间间隔两秒：pytest test_rerunfailures.py --reruns 5 --reruns-delay 2 -vs

"""
import pytest


@pytest.mark.parametrize("a,b", [(1, 0)])
# 在方法中添加该装饰器，使用功能：用例失败时，重新运行5遍,用例执行时间间隔两秒。
# 如果方法中添加和该装饰器，命令行执行时，重新运行次数及间隔时间与装饰器配置不符，以装饰器的为准
@pytest.mark.flaky(reruns=5, reruns_delay=2)
def test_div(a, b):
    print(a / b)
