#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: 有效的字母异位词.py
@time: 2020/11/28
@remark：
"""

"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？



作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn96us/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""


class Solution1:
    """
    解法一：
        将字符串s转换成字典dict_s
        遍历字符串t，如果t中的字符在dict_s中，并且dict_s[v] > 0，dict_s[v]减一，否则返回False
        判断dict_s值的和是否等于0，如果是返回True，否则返回False
    """
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        for v in s:
            if not dict_s.get(v):
                dict_s[v] = 1
            else:
                dict_s[v] += 1

        for v in t:
            if dict_s.get(v) and dict_s[v] > 0:
                dict_s[v] -= 1
            else:
                return False
        return False if sum(dict_s.values()) else True


class Solution:
    """
    解法二：
        将s转为集合并定义为set_tmp
        判断set_tmp是否等于set(t)，如果不是返回false，如果是
        遍历set_tmp，如果s.count(i) != t.count(i)返回false，否则pass
        遍历完之后，说明是有效的字母异位词
    """
    def isAnagram(self, s: str, t: str) -> bool:
        set_tmp = set(s)
        if set_tmp == set(t):
            for i in set_tmp:
                if s.count(i) != t.count(i):
                    return False
        else:
            return False
        return True