#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: lianxi.py
@time: 2020/07/13 
"""


def str_reduce(str1):
    str2 = ""
    str_mark = False
    k = 0
    for i in str1:
        if str_mark and i != ")" and i != "(":
            continue
        if i == "(":
            str_mark = True
            k += 1
            continue
        if i == ")":
            k -= 1
            if k == 0:
                str_mark = False
            continue
        if i == "<":
            str2 = str2[:-1]
            continue
        str2 = str2 + i
    return str2

if __name__ == '__main__':

    str1 = input()
    print(str_reduce(str1))