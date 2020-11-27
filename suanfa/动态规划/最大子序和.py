#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: 最大子序和.py
@time: 2020/11/27 
"""
from typing import List

"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

相关标签

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn3cg3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
class Solution:
    """
    解题思路：
        初始化tmp等于nums[0]、max_等于tmp，tmp为当前子序列之和、max_为所有子序列和的最大值
        判断tmp+nums[i]与nums[i]的关系，
            如果tmp+nums[i]大于nums[i]，max_= max(tmp+nums[i], max_),tmp = tmp + nums[i]
            否则：max_ = max(tmp + nums[i],max_,tmp,nums[i])，tmp = nums[i]
    """
    def maxSubArray(self, nums: List[int]) -> int:
        tmp = nums[0]
        max_ = tmp
        n = len(nums)
        for i in range(1,n):
            #当当前序列加上此时的元素的值大于此时元素的值，说明最大序列和可能出现在后续序列中，记录此时的最大值
            if tmp + nums[i] > nums[i]:
                max_ = max(tmp+nums[i], max_)
                tmp = tmp + nums[i]
            #当tmp(当前和)小于此时元素时，当前最长序列到此为止。以该元素为起点继续找最大子序列,
            # 并记录此时的最大值
            else:
                max_ = max(tmp + nums[i],max_,tmp,nums[i])
                tmp = nums[i]
        return max_