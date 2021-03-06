#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: 完全数.py
@time: 2020/12/21
@remark：
"""
"""
如果一个数恰好等于它的因子之和，则称该数为“完全数”，又称完美数或完备数。 
例如：第一个完全数是6，它有约数1、2、3、6，除去它本身6外，其余3个数相加，
1+2+3=6。第二个完全数是28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。
那么问题来了，求1000以内的完全数有哪些？
"""
a = []
for i in range(1, 1000):
    s = 0
    for j in range(1, i):
        if i % j == 0:
            s += j
    if s == i:
        a.append(i)
print(a)
