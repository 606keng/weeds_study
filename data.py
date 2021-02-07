#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: data.py
@time: 2021/01/19
@remark：
"""


def data(num1, num2):
    num1_list = []
    num2_list = []
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            num1_list.append(i)
    for i in num1_list:
        if num2 % i == 0:
            num2_list.append(i)
    return max(num2_list)


if __name__ == '__main__':
    print(data(15, 12))
