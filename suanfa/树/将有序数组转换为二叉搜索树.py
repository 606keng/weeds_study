#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: 将有序数组转换为二叉搜索树.py
@time: 2020/12/03
@remark：
"""
from idlelib.tree import TreeNode
from typing import List

"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xninbt/
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
        拿到题先分析，我们不难发现，要生成二叉搜索树，且左右子树的深度差的绝对值不大于1，
        所谓的二叉搜索树指的是节点的值大于左子树，小于右子树。
        通过上面条件的分析不难发现，我们需要使用列表nums的中位数为根节点，即mid=len(nums)//2，root = TreeNode(nums[mid])
        令left等于mid左边的列表，right等于mid右边的列表
        如果left不为空，则令root.left等于self.sortedArrayToBST(left)
        如果right不为空，则令root.right等于self.sortedArrayToBST(right)
        最后返回根节点root即可

    """
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        left = nums[:mid]
        right = nums[mid + 1:]
        if left:
            root.left = self.sortedArrayToBST(left)
        if right:
            root.right = self.sortedArrayToBST(right)
        return root
