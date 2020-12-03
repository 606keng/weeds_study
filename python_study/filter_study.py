#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: filter_study.py
@time: 2020/12/01 
"""
"""
序列:一块可存放多个值的连续内存空间，这些值按一定顺序排列，可通过每个值所在位置的编号（称为索引）访问它们，
    在 Python 中，序列类型包括字符串、列表、元组、集合和字典
迭代器对象：
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，
最后将返回 True 的元素放到新列表中。
"""


def select_even(num):
    return num % 2 == 0


a = [1, 2, 46, 3, 5, 58, 7, 9]
b = list(filter(select_even, a))
print(b)
