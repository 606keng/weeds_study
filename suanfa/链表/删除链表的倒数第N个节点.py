#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: 删除链表的倒数第N个节点.py
@time: 2020/11/26 
"""
from suanfa.链表.list_node import ListNode

"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn2925/
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
        定义dump节点，dump=ListNode(0)，令dump.next = head，
        使用双指针解决此问题，令slow = dump，fast等于slow的第n个next节点
        当fast与fast.next都不为空时，继续往下走，否则使用slow.next = slow.next.next删除倒数第n个节点

    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dump = ListNode(0)
        dump.next = head
        slow = dump
        fast = dump
        for i in range(n):
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dump.next