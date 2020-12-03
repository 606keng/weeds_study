#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: 验证回文串.py
@time: 2020/12/01 
"""
"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xne8id/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = s.lower()
        left = 0
        right = len(s) -1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            else:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
        return True