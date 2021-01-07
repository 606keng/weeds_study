#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: python运算符重载.py
@time: 2021/01/07
@remark：
"""

"""
    运算符重载:
        什么是运算符重载
            让自定义的类生成的对象(实例)能够使用运算符进行操作
        作用:
            让自定义的实例像内建对象一样进行运算符操作
            让程序简洁易读
            对自定义对象将运算符赋予新的规则
        算术运算符的重载:
            方法名                  运算符和表达式      说明
            __add__(self,rhs)        self + rhs        加法
            __sub__(self,rhs)        self - rhs         减法
            __mul__(self,rhs)        self * rhs         乘法
            __truediv__(self,rhs)   self / rhs          除法
            __floordiv__(self,rhs)  self //rhs          地板除
            __mod__(self,rhs)       self % rhs       取模(求余)
            __pow__(self,rhs)       self **rhs         幂运算
"""


class Mynumber:
    def __init__(self, v):
        self.data = v

    def __repr__(self):  # 消除两边的尖括号
        return "Mynumber(%d)" % self.data

    def __add__(self, other):
        '''此方法用来制定self + other的规则'''

        v = self.data + other.data
        return Mynumber(v)  # 用v创建一个新的对象返回给调用者

    def __sub__(self, other):
        '''此方法用来制定self - other的规则'''
        v = self.data - other.data
        return Mynumber(v)


n1 = Mynumber(100)
n2 = Mynumber(200)
# n3 = n1 + n2
n3 = n1 + n2  # n3 = n1.__add__(n2)
print(n3)  # Mynumber(300)
n4 = n3 - n2  # 等同于n4 = n3.__sub__(n2)
print("n4 = ", n4)
