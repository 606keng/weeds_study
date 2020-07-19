#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: test_fixture001.py
@time: 2020/07/02
备注：用于满足有些用例需要登陆，有些无需登陆的场景
"""
import pytest


@pytest.fixture()
def login():
    print("这是一个登陆方法")


class TestFixture001:
    def test_001(self, login):
        print("需要登陆")

    def test_002(self):
        print("无需登陆")
