#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: 删除排序数组中的重复项.py
@time: 2020/11/23 
"""
from typing import List

"""
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

 

示例 1:

给定数组 nums = [1,1,2], 

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        解题思路：
            使用二分法，i记录不重复列表的最后一个下标
            j记录未去重元素的第一个下标
        :param nums:
        :return:
        """
        i = 0
        j = 0
        if len(nums) == 0:
            return 0
        for j in range(len(nums)):
            # 如果nums[i] != nums[j]，i递增
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1