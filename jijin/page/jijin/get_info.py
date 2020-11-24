#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: get_info.py
@time: 2020/11/22
@remark：
"""


def get_money_info(info="基金规模：10.16元（2020-09-30）"):
    info1 = info.split("：")[1]
    account_meony = info1.split("（")[0]
    return account_meony


def get_rask_info(info="  |  豆立航"):
    return info.split("  |  ")[-1]


def get_craete_time(info="：2015-04-29"):
    return info.split("：")[-1]


if __name__ == '__main__':
    print(get_craete_time())
