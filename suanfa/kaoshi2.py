#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: kaoshi2.py
@time: 2020/12/08
@remark：
"""


def switch_min():
    s = input()
    str_ = "abcdefghijklmnopqrstuvwxyz"
    if len(s) < 2:
        return s
    dict_ = {}
    for index, value in enumerate(str_):
        dict_[value] = index
    min_index = 0
    min_pro = 26
    for i in range(1,len(s)):
        if dict_[s[i]] - dict_[s[0]] < min_pro:
            min_pro = dict_[s[i]] - dict_[s[0]]
            min_index = i
    list_s = list(s)
    list_s[min_index],list_s[0] = list_s[0],list_s[min_index]
    s = ""
    for i in list_s:
        s += i
    return s


if __name__ == '__main__':
    print(switch_min())
