#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: 函数装饰函数无入参.py
@time: 2020/12/23 
"""


def decorator(type1):
    """

    :param type1: 封闭函数入参
    :return: 返回装饰函数func
    """
    print("进入封闭函数")
    def func(fun):
        """

        :param fun: 被装饰的函数
        :return: 返回封闭函数wraap
        """
        print("进入嵌套函数func")
        def wraap(*args, **kwargs):
            """
            :param args:被装饰函数的入参
            :param kwargs: 被装饰函数的入参
            :return:
            """
            print("进入嵌套函数wraap")
            if type1:
                print("进入装饰函数的嵌套函数")
                print("开始调用被装饰函数")
                fun(*args, **kwargs)
                print("结束调用被装饰函数")
            else:
                print(f"type1 is {type1}")
        return wraap
    return func

# 相当于work=decorator(type1)(work)，即work=func(work),即work=wraap
@decorator(type1=False)
def work(name, age):
    print(f"{name}的年龄是{age}")

work(name="doulihang", age="28")
