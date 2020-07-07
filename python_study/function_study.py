#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: function_study.py
@time: 2020/07/07
@remark：函数学习
"""


# 定义简单的函数
def method():
    print("a")


# 如果函数无return，默认返回None
print(method())


# 函数的入参为默认值，且该值为可变的时，只能执行一次
def add(a, b=[]):
    b.append(a)
    return b


# 结果为[1]
print(add(1))
# 结果为[1, 2]，因为b是可变的默认值，只能执行一次，所以第二次调用add函数时，不会对b进行重新赋值，是在第一次列表b的基础上添加元素a的
print(add(2))


# 关键字参数*args，以元组形式接受除了data参数以外的所有传入的参数，
def args(data, *args):
    # 打印元组，输出结果为：(1, 3, 4, 5)
    print(args)
    # 对元组进行解包，输出结果为：1 3 4 5
    print(*args)


b = 123
a = 1
args(b, a, 3, 4, 5)


# 关键字参数**kwargs，以字典形式接受除了a参数以外的所有传入的参数，
def kwargs(a, **kwargs):
    # 打印字典
    print(kwargs)
    # 打印所有的key
    print(kwargs.keys())
    # 打印所有的value
    print(kwargs.values())


a = 2
kwargs(a, b=1, c=2)


# 仅限关键字传参
def num(*, a):
    print(a)


num(a=2)

# 对列表或元组进行解包
a = [1, 2, 3]
# 输出结果：1 2 3
print(*a)


def kw(q, w):
    print(q, w)


a = {"q": 1, "w": 2}
# 对字典进行解包
kw(**a)

# lambda表达式，冒号左侧为入参，右侧为return
b = lambda x, y, z: x + y + z
print(b(1, 2, 3))
