#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: kaoshi4.py
@time: 2020/12/29 
"""


def remove_num( nums):
    if len(nums) < 2:
        return len(nums)
    left = 0
    for num in nums:
        if nums[left] != num:
            left += 1
            nums[left] = num
    return left + 1


if __name__ == '__main__':
    print(remove_num(nums=[1,1,2.2,4,5,8,8]))