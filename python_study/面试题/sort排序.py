#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: sort排序.py
@time: 2020/12/21
@remark：
"""
"""
已知一个队列[1, 3, 6, 9, 7, 3, 4, 6]

按从小到大排序
按从大大小排序
去除重复数字
"""
a = [1, 3, 6, 9, 7, 3, 4, 6]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
print(set(a))