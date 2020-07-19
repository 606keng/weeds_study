#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: show.py
@time: 2020/07/16
@remark：
"""
import gril


def send():
    print(f"show has_gril id is {id(gril.has_gril)}")
    if gril.has_gril:
        print("发女朋友了")
    else:
        print("单身贵族")
