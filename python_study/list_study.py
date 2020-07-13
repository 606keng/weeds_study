#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: list_study.py
@time: 2020/07/13
@remark：
"""
# 列表推导式,求列表中能被3整除的数
a = [i for i in range(100) if i % 3 == 0]
print(a)

# 获取列表中出现次数最多的元素
nums = [1, 2, 2, 3, 3, 3, 4, 5]


def add_five(n):
    return n + 5


b = [12, 67, 8]
# 对b中每个元素都加5，
c = map(add_five, b)  # 将可迭代对象的每个元素都传入函数中，
print(list(c))

# 将list1/list2对应位置的元素进行组合，形成新的二维列表,
# 如果两个列表不一样长，二维列表的长度同较短列表
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6]
list3 = zip(list1, list2)
print(list(list3))

# 将list1进行颠倒
print(list1[::-1])

# 检查列表中是否存在某个元素
print(list1.count(6))

# 找出列表中出现次数最多的元素。max(iter,key)，当max中同时传入可迭代对象和key时，key为一个函数。
# 这种情况下，需要将可迭代对象中的元素传入key函数中，取函数返回最大的元素
a = [1, 2, 3, 5, 2, 2, 3, 4]
b = set(a)
# 将列表b中的元素传入函数a.count()中，取返回值最大的元素
print(max(b, key=a.count))

# 找出字典中值最大的key
a = {
    "k1": 37,
    "k2": 36,
    "k3": 1
}
print(max(a.keys(), key=a.get))