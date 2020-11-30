#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: 加一.py
@time: 2020/11/30 
"""
from typing import List

"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

 

示例 1：

输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
示例 2：

输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。
示例 3：

输入：digits = [0]
输出：[1]
 

提示：

1 <= digits.length <= 100
0 <= digits[i] <= 9

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2cv1c/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution1:
    """
    方法二略优于方法一
    解法一：
        先将列表转换为字符串，
        将转换后的字符串转换为整数 + 1
        再将转换后的整数转换为列表
        如果+1后的列表长度小于之前的列表
            将+1后的列表前几位的0进行补全
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = ""
        for i in digits:
            sum += str(i)
        sum = int(sum) + 1
        result = []
        for i in str(sum):
            result.append(int(i))
        count = len(digits) - len(result)

        return [0] * count + result

class Solution2:
    """
    解法二：
        定义新列表，判断当前列表的最后一位是否为9，如果是，删除列表最后一位，新列表添加元素0
            如果删除后，旧列表为空，返回[1] + newlst
            否则令旧列表的最后一位+1，返回旧列表  + newlst
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        newlst = []
        while digits and digits[-1] == 9:
            digits.pop()
            newlst.append(0)
        if not digits:
            return [1] + newlst
        else:
            digits[-1] += 1
            return digits + newlst
