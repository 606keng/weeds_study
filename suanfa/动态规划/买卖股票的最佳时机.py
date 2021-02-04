#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: 买卖股票的最佳时机.py
@time: 2020/11/27 
"""
from typing import List

"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。

 

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn8fsh/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
class Solution:
    """
    解题思路：
        要想一次买入卖出获利最大，需要在历史最低点买入，对比当前卖出与之前卖出获利
            历史最低点买入：minprice = min(price,minprice)
            当前卖出获利与之前卖出获利：maxprofit = max(price-minprice,maxprofix)
    """
    def maxProfit(self, prices: List[int]) -> int:
        minprice = 2**32 -1
        maxproft = 0
        for price in prices:
            maxproft = max(price-minprice,maxproft)
            minprice = min(price,minprice)
        return maxproft
