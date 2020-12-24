#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: __init__.py.py
@time: 2020/06/24 
"""


class Person:
    def __init__(self):
        self.a = 123
        self.b = 567

    def add(self):
        print(self.a + self.b)


if __name__ == '__main__':
    a1 = Person()
    print(getattr(a1, "a"))
    print(getattr(a1, "b"))
    print(getattr(a1, "add"))
    setattr(a1,"c",14)
    print(a1.c)
