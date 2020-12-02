#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: 回文链表.py
@time: 2020/12/02
@remark：
"""
from suanfa.链表.list_node import ListNode

"""
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnv1oc/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    解题思路
        首先将链表转换为列表，然后判断列表是否为回文列表
    """
    def isPalindrome(self, head: ListNode) -> bool:
        list_ = []
        while head:
            list_.append(head.val)
            head = head.next
        return list_ == list_[::-1]
