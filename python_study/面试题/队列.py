#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: 队列.py
@time: 2020/12/21
@remark：
"""
# 已知一个队列,如： [1, 3, 5, 7], 如何把第一个数字，放到第三个位置，得到：[3, 5, 1, 7]
a = [1, 3, 5, 7]
a.insert(3,1)
print(a[1:])