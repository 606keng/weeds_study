#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: kaoshi3.py
@time: 2020/12/08
@remark：
"""
import sys


def count_num():
    n = input().split(" ")
    x = int(n[0])
    y = int(n[1])
    nums = [0] * x
    for i in range(x):
        nums[i] = input().strip().split("\t")
    result = []
    for i in range(x):
        for j in range(y):
            if nums[i][j] == "5":
                result.append((i, j))
    count = len(result)
    if count < 2:
        return count
    for i in range(count):
        for j in range(i, count):
            if abs(result[i][0] - result[j][0]) > 4 or abs(result[i][1] - result[j][1]) > 4:
                pass
            else:
                count -= 1
    return count


if __name__ == "__main__":
    print(count_num())
