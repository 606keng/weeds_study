#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: 反转链表.py
@time: 2020/11/30
@remark：
"""
"""

反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnnhm6/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from suanfa.链表.list_node import ListNode


class Solution:
    """
    解题思路：
        使用双指针法解决此问题，首先定义left=right=head
        如果链表为一个节点，则直接返回head。否则令右指针right移向下一个节点，left的下一个节点为None
        接下来进行反转，当右指针不为None时，head等于right，右指针移向下一个节点，head.next等于左指针，
        左指针left向右移向下一个节点，如此反复
    """
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        left = right = head
        if not head.next:
            return head
        else:
            right = right.next
            left.next = None
        while right:
            head = right
            right = right.next
            head.next = left
            left = head
        return head
