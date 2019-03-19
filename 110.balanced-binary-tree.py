#
# @lc app=leetcode id=110 lang=python
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (40.38%)
# Total Accepted:    300.1K
# Total Submissions: 741.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as:
# 
# 
# a binary tree in which the depth of the two subtrees of every node never
# differ by more than 1.
# 
# 
# Example 1:
# 
# Given the following tree [3,9,20,null,null,15,7]:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# Return true.
# 
# Example 2:
# 
# Given the following tree [1,2,2,3,3,null,null,4,4]:
# 
# 
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
# 
# 
# Return false.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):


    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 其实是回溯算法
        return bool(self.checkDepth(root))

    def checkDepth(self, root):
        if not root:
            return 1

        left_depth = self.checkDepth(root.left)
        right_depth = self.checkDepth(root.right)

        if (left_depth and right_depth and abs(left_depth - right_depth) < 2):
            return max([left_depth, right_depth]) + 1
        return False

    def __isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 递归是在空递归
        # 可以一边递归一边判断
        # 最好是把递归结果和判断结果放一起
        if root:
            left_depth = max(self.getDepth(root.left, 0, []))
            right_depth = max(self.getDepth(root.right, 0, []))
            if abs(left_depth - right_depth) >= 2:
                return False
            if self.isBalanced(root.left):
                return self.isBalanced(root.right)
            return False
        return True

    def _isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 每个节点左右两个子树的深度必须相同，或者相差不能大于1
        # 不是总的最深和最浅相差不能大于1
        # [1,2,2,3,3,3,3,4,4,4,4,4,4,null,null,5,5] 挂了
        res = self.getDepth(root, 0, [])
        print res
        return max(res) - min(res) <= 1
    
    def getDepth(self, root, index, res):
        if root:
            res = self.getDepth(root.left, index+1, res)
            res = self.getDepth(root.right, index+1, res)
        else:
            res.append(index+1)        
        return res
