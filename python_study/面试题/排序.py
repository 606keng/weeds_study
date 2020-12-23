#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: 排序.py
@time: 2020/12/21
@remark：
"""
# 用python写个冒泡排序
a = [1, 3, 10, 9, 21, 35, 4, 6]
len_ = len(a)
for i in range(len_):
    for j in range(i+1,len_):
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]
print(a)

# 用python写个快速排序
a = [1, 3, 10, 9, 21, 35, 4, 6]
