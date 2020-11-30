#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: 两个数组的交集 II.py
@time: 2020/11/30 
"""
from collections import defaultdict
from typing import List

"""
给定两个数组，编写一个函数来计算它们的交集。

 

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
 

说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
我们可以不考虑输出结果的顺序。
进阶：

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2y0c2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

class Solution1:
    """
    解法2优于解法1
    解法一：
        将列表转换为字典，key为列表的元素，value为该元素出现的次数
        遍历字典1与字典2的合集，令dict3 key为字典1与2的交集，value为两个字典中value较小的值
        令字典3的key为列表的元素，value为该元素出现的次数
    """
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        for i in nums1:
            dict1[i] += 1
        for i in nums2:
            dict2[i] += 1
        dict3 = {i:min(dict1[i], dict2[i]) for i in set(dict1)&set(dict2)}
        return sum([[i]*dict3[i] for i in dict3.keys()],[])


class Solution2:
    """
    解法2：
        首先将两个列表进行排序
        使用双指针，如果两个指针都未超过对应列表的长度，则判断两个指针对应列表元素的大小，将较小的指针向前移动，
            如果两个元素相等，将该元素添加到新增列表中，两个指针同时向前移动
    """
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        nums3 = []
        left = 0
        right = 0
        while left < len(nums1) and right < len(nums2):
            if nums1[left] < nums2[right]:
                left += 1
            elif nums1[left] > nums2[right]:
                right += 1
            else:
                nums3.append(nums1[left])
                left += 1
                right += 1
        return nums3
