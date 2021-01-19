#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: 函数装饰函数无入参.py
@time: 2020/12/23 
"""

def decorator(fun):
    """
    :param fun: 被装饰的函数
    :return: 嵌套函数
    """
    def wraap(*args, **kwargs):
        """
        :param args:被装饰函数的入参，元组
        :param kwargs: 被装饰函数的入参，字典
        :return:
        """
        print("进入装饰函数的嵌套函数")
        print("开始调用被装饰函数")
        fun(*args, **kwargs)
        print("结束调用被装饰函数")
    print("进入封闭函数")
    return wraap

# @decorator相当于work = decorator(work)即work = wraap
@decorator
def work(name, age):
    # print(kwargs)
    # name = kwargs["name"]
    # age = kwargs["age"]
    print(f"{name}的年龄是{age}")

# work(name="doulihang", age="28")相当于decorator(work)(name="doulihang", age="28")
work(name="doulihang", age="28")
