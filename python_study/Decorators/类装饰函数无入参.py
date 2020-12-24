#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: 类装饰函数无入参.py
@time: 2020/12/24 
"""


class Person:
    # 类的构造函数，对类进行实例化时，执行该方法
    def __init__(self, fun, *args, **kwargs):
        print("初始化装饰类")
        self.fun = fun

    # 实例化后的对象，将对象变为可调用的，调用该实例对象时，调用该方法
    # xiaoming = Person()，xiaoming()等同于xiaoming.__call__
    def __call__(self, *args, **kwargs):
        print("调用call方法")
        return self.fun(*args, **kwargs)


# 使用类对函数进行装饰，相当于student=Person(fun)
@Person
def student(name, age):
    print(f"{name} 年龄是{age}")


# 相当于student=Person(fun).__call__()
student("豆立航", 28)
