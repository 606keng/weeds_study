#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: 只出现一次的数字.py
@time: 2020/11/30 
"""
from typing import List

"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x21ib6/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:
    """
    解题思路：
        将列表nums转换为字典，k为列表的元素，v为该元素在列表中出现的次数
        遍历字典，如果k对应的v为1时，返回k
    """
    def singleNumber(self, nums: List[int]) -> int:
        dict_ = {}
        for i in nums:
            if i in dict_:
                dict_[i] += 1
            else:
                dict_[i] = 1
        for k, v in dict_.items():
            if v == 1:
                return k
