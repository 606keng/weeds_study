#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: test_fixture005.py
@time: 2020/07/02
备注：@pytest.fixture(params=[["豆立航","dlh12378612873"],["野草","dlh12378612873"]])前置函数传入参数，request.param提取传入的参数
"""
import pytest


@pytest.fixture(params=[["豆立航","dlh12378612873"],["野草","dlh12378612873"]])
def login(request):
    print("登录用户名{},登录密码{}".format(request.param[0],request.param[1]))


class TestFixture001:
    def test_001(self,login):
        print("需要登陆1")
