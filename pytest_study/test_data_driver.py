#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: test_data_driver.py
@time: 2020/07/14
@remark：数据驱动
"""
import pytest
import yaml


class TestDemo:
    @pytest.mark.parametrize("env", yaml.safe_load(open("env.yaml")))
    def test_demo(self, env):
        if "test" in env:
            print(f"测试环境ip:{env.get('test')}")
        elif "dev" in env:
            print("开发环境")
