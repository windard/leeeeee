# coding=utf-8
#
# @lc app=leetcode id=965 lang=python
#
# [965] Univalued Binary Tree
#
# https://leetcode.com/problems/univalued-binary-tree/description/
#
# algorithms
# Easy (66.96%)
# Likes:    222
# Dislikes: 36
# Total Accepted:    43.7K
# Total Submissions: 65.3K
# Testcase Example:  '[1,1,1,1,1,null,1]'
#
# A binary tree is univalued if every node in the tree has the same value.
# 
# Return true if and only if the given tree is univalued.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,1,1,1,1,null,1]
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: [2,2,2,5,2]
# Output: false
# 
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the given tree will be in the range [1, 100].
# Each node's value will be an integer in the range [0, 99].
# 
# 
#
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.checkSame(root, root.val)

    def checkSame(self, root, value):
        if not root:
            return True
        if not root.val == value:
            return False
        return self.checkSame(root.left, value) and self.checkSame(root.right, value)
