#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: 合并两个有序链表.py
@time: 2020/12/02
@remark：
"""
from suanfa.链表.list_node import ListNode

"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnnbp2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    解题思路：
        本题使用递归的方法求解
        首先如果l1是空，直接返回l2，如果l2是空，直接返回l1
        如果l1.val小于l2.val，令l1.next等于self.mergeTwoLists(l1.next, l2)，进行递归，然后返回l1
        如果l1.val不小于l2.val，令l2.next等于self.mergeTwoLists(l1, l2.next)，进行递归，然后返回l2
        相当于先把合并好的链表生成，然后从后到前一级一级的返回每个节点
    """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
