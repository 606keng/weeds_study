#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: 二叉树的层序遍历.py
@time: 2020/12/03 
"""
from idlelib.tree import TreeNode
from typing import List

"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

 

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnldjj/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    """
    解题思路：
        本题采用深度优先的方式进行求解
        首先定义列表levels=[]，如果树为空，返回levels
        定义helper函数，传递两个参数，node与level，node为当前节点，level为当前深度
        由于level从0开始计算，当level等于levels的长度时，证明深度为level的节点不在列表中，需要levels.append([])
        然后将当前node的值，追加在levels[level]后
        如果 node.left存在，递归执行helper(node.left, level + 1)
        如果 node.right存在，递归执行helper(node.right, level + 1)
        入口函数为helper(root, 0)
        levels为要求的列表，返回levels
    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels

        def helper(node, level):
            if level == len(levels):
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels
