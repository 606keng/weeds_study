#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: object.py
@time: 2020/07/12
@remark：面向对象，
类属性修改后，调用实例属性，实例属性与修改后的类属性相同。
类属性修改后，修改实例属性，再次修改类属性，实例属性为修改后的实例属性。重新定义新的实例，新实例的属性同类属性
"""


class Person:
    name = "weeds"
    def __init__(self,age,gender):
        self.age = age
        self.gender =gender

    def get_name(self):
        return self.name


# 不进行实例化，调用类的属性
print(Person.name)
# 对类进行实例化
p = Person()
# 调用类的方法
print(p.get_name())
# 调用类的属性
print(p.name)
# 修改类的属性
Person.name = "kele"
print(Person.name)
# 实例属性与类属性相同
print("修改类属性后，打印实例属性%s" % p.name)
# 修改实例的属性
p.name = "gaogao"
# 修改实例属性后，再次修改类的属性
print("修改类属性后，修改实例属性，打印实例属性%s" % p.name)

# 重新定义实例，打印实例属性
p1 = Person()
print("修改类属性后，重新定义实例，打印实例属性%s" % p1.name)
