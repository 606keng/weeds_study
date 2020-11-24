#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: 反转字符串.py
@time: 2020/11/23 
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s = list(s)
        lens = len(s)
        for i in range(int(lens/2)):
            a = s[i]
            s[i] = s[lens-i-1]
            s[lens-i-1] = a

        return s
if __name__ == '__main__':
    print(Solution().reverseString("hello"))