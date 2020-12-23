#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: __init__.py.py
@time: 2020/07/28 
"""
nums = [(1, 2), (4, 3), (5, 6)]
print(len(nums))
for i in range(2):
    for j in range(i+1,3):
        print(nums[i][0],nums[i][1])
        print(nums[j][0], nums[j][1])