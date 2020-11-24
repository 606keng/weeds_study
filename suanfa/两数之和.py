#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: 两数之和.py
@time: 2020/11/23 
"""
"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

def twoSum1(nums,target):
    """
    解题思路：
    1.求出num2 = target - num[i]
    2.判断num2是否在nums中
    :param nums:
    :param target:
    :return:
    """
    j = -1
    lens = len(nums)
    for i in range(lens):
        # 如果num2在num1之后，则跳转循环
        if target-nums[i] in nums[i+1:]:
            # 在i+1之后，获取num2的值
            j = nums.index(target-nums[i],i+1)
            break
    if j >0:
        return i,j

def twoSum2(nums,target):
    """
    解题思路：
    1.定义空字典，判断字典中是否存在target-num，如果不存在，将num，i存在在字典中
    :param nums:
    :param target:
    :return:
    """
    dict = {}
    for i,num in enumerate(nums):
        if dict.get(target-num) is not None:
            j = dict.get(target-num)
            return i,j
        dict[num] = i