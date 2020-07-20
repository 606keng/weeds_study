#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: conftest.py
@time: 2020/07/19
@remark：对hook进行修改
"""
from typing import List

import pytest

# 自定义hook函数pytest_collection_modifyitems，可以将收集上来的用例进行改写
# 控制用例的执行顺序，解决用例的编码问题，给用例添加标签
import yaml


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    # items代表测试用例的集合列表，颠倒测试用例的执行顺序
    items.reverse()
    # item表示每个测试用例，解决用例名称中文显示问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")

        # 自定义添加标签,给名称中包含add的用例添加add标签，
        # 可以通过命令pytest 用例文件名 -m add选中执行
        if "add" in item.nodeid:
            item.add_marker(pytest.mark.add)


# 在pytest --help中添加自己的组，显示结果如下注释
"""
    carsir:
         --env=ENV             carsir env switch
"""


def pytest_addoption(parser: "Parser", pluginmanager: "PytestPluginManager") -> None:
    """
    :param parser:
    :param pluginmanager:
    :return:
    """
    # 在pytest命令行中添加自己的组
    mygroup = parser.getgroup("carsir")
    # 给自己的组添加选项
    mygroup.addoption(
        "--env",  # 选项的命令是--env
        default="test",  # 选项的默认值是test
        dest="env",
        help="carsir env switch"  # 选项的说明
    )


# 在命令行输入pytest test_env.py --env dev 返回dev环境host
# 在命令行输入pytest test_env.py --env test 返回test环境host
@pytest.fixture(scope="session")
def cmdoption(request):
    # 获取--env后面的参数
    myenv = request.config.getoption("--env", default="test")
    # 如果test在myenv中，读取test.yml，并返回
    if "test" in myenv:
        with open("datas/test.yml") as f:
            return yaml.safe_load(f)
    # 如果dev在myenv中，读取dev.yml，并返回
    elif "dev" in myenv:
        with open("datas/dev.yml") as f:
            return yaml.safe_load(f)
