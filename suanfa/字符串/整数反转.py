#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: 整数反转.py
@time: 2020/11/25 
"""
"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnx13t/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
class Solution:
    """
    解题思路：
        将整数转换为字符串后，利用列表进行反转。最后判断是否溢出
    """
    def reverse(self, x: int) -> int:
        x = str(x)
        if "-" in x:
            x = x[::-1]
            x = -int(x[:-1])
        else:
            x = int(x[::-1])
        if x<-2**31 or x > 2**31 -1:
            return 0
        return x