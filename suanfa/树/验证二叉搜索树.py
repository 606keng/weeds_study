#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:DOULIHANG
@file: 验证二叉搜索树.py
@time: 2020/11/27 
"""
from idlelib.tree import TreeNode

"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn08xg/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:
    """
    解题思路
        确定递归的两个终止条件
            当当前节点为空时，表明这个节点是叶子节点，这个节点没有子节点，返回True
            当当前节点不在[min_,max_]区间内，证明这个节点不符合二叉搜索树的两个特征，返回False
        递归方程：
            定义递归方程为dg(root,min_,max_)
            当为左节点时，左节点必须要比根节点小，dg(root,min_,root.val)
            当为右节点时，右节点必须要比根节点大，dg(root,min_,root.val)
    """
    def isValidBST(self, root: TreeNode) -> bool:
        return self.dg(root, -(2 ** 32), 2 ** 32)

    def dg(self, root, min_, max_):
        if not root:
            return True
        if root.val > min_ and root.val < max_:
            pass
        else:
            return False

        if self.dg(root.left, min_, root.val) == False:
            return False
        if self.dg(root.right, root.val, max_) == False:
            return False
        return True
