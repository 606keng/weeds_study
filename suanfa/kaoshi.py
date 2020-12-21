#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: kaoshi.py
@time: 2020/12/08
@remark：
"""


def delete_min():
    s = input()
    dict_ = {}
    s = list(s)
    for i in s:
        if i in dict_:
            dict_[i] += 1
        else:
            dict_[i] = 1
    min_ = min(dict_.values())
    for k, v in dict_.items():
        if v == min_:
            while v > 0:
                s.remove(k)
                v -= 1
    t = ""
    for i in s:
        t += i
    return t


if __name__ == '__main__':
    print(delete_min())
