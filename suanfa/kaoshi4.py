#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: kaoshi4.py
@time: 2021/01/23
@remark：
"""


def add_scr(st):
    s = "abcdefghijklmnopqrstuvwxyz"
    st1 = ""
    for i in st:
        if i in s or i == " ":
            if i == " ":
                st1 += i
            else:
                st1 += s[(s.index(i) + 3) % 26]
    return st1


if __name__ == '__main__':
    st = input()
    print(add_scr(st))
