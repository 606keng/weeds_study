#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: 二叉树的最大深度.py
@time: 2020/11/24 
"""
"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnd69e/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
from idlelib.tree import TreeNode


class Solution:
    """
    解题思路：
        使用递归处理此问题，当root为none时，二叉树深度为0，否则深度等于1+左右分支中较大的深度值
    """
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.right),self.maxDepth(root.left))