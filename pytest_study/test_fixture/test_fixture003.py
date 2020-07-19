#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: test_fixture003.py
@time: 2020/07/02
备注：自动导入同一目录下conftest.py文件中的open函数。conftest.py用于存放所有被fixture装饰的前置函数
"""
import pytest


class TestFixture001:
    def test_001(self, open):
        print("登陆系统1")

    # 使用@pytest.mark.usefixtures(open)将open函数作为test_002的前置函数
    @pytest.mark.usefixtures("open")
    def test_002(self):
        print("登陆系统2")
