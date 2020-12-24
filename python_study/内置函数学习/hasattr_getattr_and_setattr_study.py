#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: hasattr_getattr_and_setattr_study.py
@time: 2020/12/23 
"""
"""
学习hasattr、getattr、setattr
1.hasattr判断一个对象是否拥有某属性，返回一个布尔值
2.getattr获取对象属性值，如果不存在该属性，抛出异常
3.setattr设置属性的值，当属性不存在时，自动创建
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(f"{self.name} 跑步")


def song(name):
    print(f"{name} 唱歌")


if __name__ == '__main__':
    doulihang = Person("doulihang", 28)
    # 判断豆立航是否有name属性
    print(hasattr(doulihang, "name"))
    # 判断豆立航是否有run1属性
    print(hasattr(doulihang, "run1"))
    # 获取豆立航的run属性，并执行该属性。如果属性为方法，调用该方法时，属性名后添加括号
    getattr(doulihang, "run")()
    # 判断豆立航是否有song属性
    if not hasattr(doulihang, "song"):
        #给豆立航添加song方法
        setattr(doulihang, "song", song)
    doulihang.song(doulihang.name)
