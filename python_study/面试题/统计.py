#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: 统计.py
@time: 2020/12/21
@remark：
"""
# 统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
list_ = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
b = [i for i in list_ if i > 0]
c = [i for i in list_ if i < 0]
print(f"正数个数为{len(b)}")
print(f"负数个数为{len(c)}")