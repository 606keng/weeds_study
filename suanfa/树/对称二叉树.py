#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: 对称二叉树.py
@time: 2020/12/03 
"""
from idlelib.tree import TreeNode

"""
给定一个二叉树，检查它是否是镜像对称的。

 

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
 

进阶：

你可以运用递归和迭代两种方法解决这个问题吗？

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn7ihv/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    解题思路：
        首先判断root是否为空，如果为空，返回True，否则返回self.que(root.left, root.right)
        定义函数self.que，传入参数left_node，right_node。
            如果两个参数都为None，则返回True，
                如果两个参数都不为空，判断两个节点的值是否不等，如果不等，返回false，
                否则判断left_node.left, right_node.right是否相等，并且left_node.right, right_node.left是否相等
    """
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            return self.que(root.left, root.right)

    def que(self, left_node, right_node):
        if not left_node and not right_node:
            return True
        elif left_node and right_node:
            if left_node.val != right_node.val:
                return False
            else:
                return self.que(left_node.left, right_node.right) and self.que(left_node.right, right_node.left)
