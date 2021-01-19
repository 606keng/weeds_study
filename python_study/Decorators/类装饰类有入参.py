#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: 类装饰类无入参.py
@time: 2020/12/24 
"""


class decorateClass:
    def __init__(self, type):
        print("进入装饰类的构造函数")
        self.type = type
        print(f"车辆为{self.type}")

    def __call__(self, wrapedClass):
        print("进入__call__函数")
        self.wrapedClassObj = wrapedClass

        def wraped(*args, **kwargs):
            return self.wrapedClassObj(*args, **kwargs)

        return wraped


# 对类进行装饰，相当于Car=decorateClass("汽车").__call__(Car),即Car=wraped
@decorateClass("汽车")
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

if __name__ == '__main__':

    # 相当于fute = decorateClass("汽车").__call__(Car)("福特", "1.3吨", "15万")
    fute = Car("福特", "1.3吨", "15万")
    fute.driver(200)
    fute.driver(100)

class Person:
    def __init__(self,name):
        print(name)

    def __call__(self, cls):
        print("进入call函数")
        self.clsobj = cls
        def wraap(*args,**kwargs):
            print("进入装饰函数")
            return self.clsobj(*args,**kwargs)
        return wraap
@Person("doulihang")
class Student:
    def __init__(self,age):
        print(age)
    def run(self):
        print("跑起来")


if __name__ == '__main__':
    xiaohong = Student(28)
    xiaohong.run()