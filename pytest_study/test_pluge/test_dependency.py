#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: test_dependency.py
@time: 2020/07/19
@remark：如果用例执行顺序有依赖时，可以使用dependency定义依赖关系
"""
import pytest


class TestDepend:
    """
    业务场景为新增/查看列表/删除
    查看列表用例依赖新增用例
    删除用例依赖查看列表用例
    """

    # 定义用例的别名
    @pytest.mark.dependency(name="create")
    def test_create(self):
        print("create")

    # 定义用例的别名为list，需要依赖的用例create，
    # 如果create执行失败，则list用例不会再执行
    # 如果list执行失败，delete则不会再执行
    @pytest.mark.dependency(name="list", depends=["create"])
    def test_list(self):
        print("list")
        assert False

    # 定义用例的别名为delete，需要依赖的用例为"create", "list"
    @pytest.mark.dependency(name="delete", depends=["create", "list"])
    def test_delete(self):
        print("delete")
