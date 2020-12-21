#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: 水仙花.py
@time: 2020/12/21
@remark：
"""
# 打印出100-999所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
for i in range(100, 1000):
    x = i // 100
    y = (i % 100) // 10
    z = i % 10
    if x ** 3 + y ** 3 + z ** 3 == i:
        print(i)
