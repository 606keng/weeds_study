#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: conftest.py
@time: 2020/07/02
备注：
        conftest.py这个文件名是固定的，不可以更改。
        conftest.py与运行用例在同一个包下，并且该包中有__init__.py文件
        使用的时候不需要导入conftest.py，会自动寻找。
"""
import pytest

# 默认scope等于function，作用域为函数级别，类似于setup、teardown.  scope="module",作用域为module，类似于setup_module,teardown_module
from carsir_ui.page.app import App


@pytest.fixture(scope="session", autouse=True)
def start():
    login = App().start_carsir().login()
    login.input_phone_number("16033333333")
    main = login.input_verification_code("111111")
    yield main
    main.logout()