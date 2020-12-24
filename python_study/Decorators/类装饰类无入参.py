#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: 类装饰类无入参.py
@time: 2020/12/24 
"""


class decorateClass:
    def __init__(self, wrapedClass):
        print("进入装饰类的构造函数")
        self.wrapedClass = wrapedClass

    def __call__(self, *args, **kwargs):
        print("进入__call__函数")
        return self.wrapedClass(*args, **kwargs)


# 对类进行装饰，相当于Car=decorateClass(Car)
@decorateClass
class Car:
    def __init__(self, name, weight, cost):
        print("class car __init__ start...")
        self.name = name
        self.weight = weight
        self.cost = cost
        self.distance = 0
        print("class car __init__ end...")

    def driver(self, distance):
        self.distance += distance
        print(f"{self.name}已经累计行驶了{self.distance}公里")


# 相当于Car = decorateClass(Car).__call__("福特", "1.3吨", "15万")
fute = Car("福特", "1.3吨", "15万")
# fute.driver(200)
# fute.driver(100)
