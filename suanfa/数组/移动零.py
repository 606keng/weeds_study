#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: 移动零.py
@time: 2020/11/30 
"""
from typing import List

"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2ba4i/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        首先统计列表中0的数量n，然后删除n个0，再列表后面添加n个0
        """
        count = nums.count(0)
        for i in range(count):
            nums.remove(0)
            nums.append(0)
        return nums


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        使用双指针法：
            定义两个指针slow_index and fast_index,使用fast_index为下标遍历列表nums
            如果fast_index指向的元素不为0，令slow_index等于fast_index指向的元素，
            slow_index向前移动一位，
            最后将为0的元素添加到列表后面
        """
        slow_index = 0

        for fast_index in range(len(nums)):
            if nums[fast_index] != 0:
                nums[slow_index] = nums[fast_index]
                slow_index += 1
        for i in range(0, fast_index + 1 - slow_index):
            nums[slow_index + i] = 0