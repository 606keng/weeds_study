#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: 合并两个有序数组.py
@time: 2020/11/24 
"""
from typing import List

"""
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

 

说明：

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
 

示例：

输入：
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出：[1,2,2,3,5,6]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        解题思路：
            1.初始化下标p1/p2，nums1_copy = nums1[:m]
            2.利用双指针，将num2与nums1_copy中各元素进行对比，将较小的元素插入到p1+p2的位置
            3.将p1、p2分别与m、n进行比较，如果小于时，将剩余的元素插入到p1+p2位置处
        """

        p1 = 0
        p2 = 0
        nums1_copy = nums1[:m]

        while p1<m and p2<n:
            if nums1_copy[p1] < nums2[p2]:
                nums1[p1+p2] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p1+p2] = nums2[p2]
                p2 += 1
        if p1<m:
            nums1[p1+p2:] = nums1_copy[p1:]
        if p2<n:
            nums1[p1+p2:] = nums2[p2:]
        return nums1[:m+n]
