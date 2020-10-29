#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: conftest.py
@time: 2020/08/06
备注：
        conftest.py这个文件名是固定的，不可以更改。
        conftest.py与运行用例在同一个包下，并且该包中有__init__.py文件
        使用的时候不需要导入conftest.py，会自动寻找。
"""
from time import sleep
from typing import List

import pytest

# 默认scope等于function，作用域为函数级别，类似于setup、teardown.  scope="module",作用域为module，类似于setup_module,teardown_module
from carsir_ui.page.app import App


@pytest.fixture(scope="session", autouse=True)
def start():
    """
    need_login目录下的所有测试用例自动运行start（）方法
    :return:
    """
    login = App().start_carsir().login()
    # 定义是否为debug模式，如果是，则无需做登录/登出操作
    debug = True
    if debug:
        # 首先登录app，如果无法定位到登录元素，证明已经登录成功，直接跳转到主页
        try:
            login.input_phone_number("16033333333")
            main = login.input_verification_code("111111")
        except:
            main = login.goto_main()
        # 返回main对象
        yield main
        # 执行完成后，退出登录
        main.logout()
    elif debug is not True:
        main = login.goto_main()
        yield main
        pass

def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    # item表示每个测试用例，解决用例名称中文显示问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")

