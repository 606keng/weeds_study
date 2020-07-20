#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: conftest.py
@time: 2020/07/19
@remark：
"""
from typing import List


def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None: