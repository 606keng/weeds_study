#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: 实例引用.py
@time: 2020/07/12
@remark：
"""


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print(f"{self.name} {self.age} {self.gender},我在吃")

    def run(self):
        print(f"{self.name} {self.age} {self.gender},我在跑")

    def set_att(self):
        self.value = "fit"

#实例化两个类
xiaoming = Person("xiaoming", 12, "male")
xiaohong = Person("xiaohong", 10, "female")
#输出xiaoming的实例属性name
print(xiaoming.name)
#调用实例的方法
xiaoming.run()
#调用方法，给xiaoming添加self.value属性
xiaoming.set_att()
print(xiaoming.value)
try:
    print(xiaohong.value)
except AttributeError:
    print("xiaohong没有value属性")