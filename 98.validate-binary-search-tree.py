#
# @lc app=leetcode id=98 lang=python
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (25.24%)
# Likes:    2161
# Dislikes: 325
# Total Accepted:    438.9K
# Total Submissions: 1.7M
# Testcase Example:  '[2,1,3]'
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
# 
# Assume a BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# 
# Example 1:
# 
# 
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 
# Input: [2,1,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# 
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 不止要和上一级比较
        # 还要和所有的上级比较
        # Wrong Answer
        # [10,5,15,null,null,6,20]
        if not root:
            return True
        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False
        return all([self.isValidBST(root.left), self.isValidBST(root.right)])

    def _isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # less than or more than , no equal
        return self.between(root, float("inf"), -float("inf"))

    def between(self, root, upper, lower):
        if not root:
            return True
        
        if root.left and not lower < root.left.val < root.val:
            return False
        if root.right and not root.val < root.right.val < upper:
            return False
        return all([self.between(root.left, root.val, lower),
                    self.between(root.right, upper, root.val)])

    def ___isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.middle(root, float("inf"), -float("inf"))

    def middle(self, root, upper, lower):
        if not root:
            return True
        
        if root.val <= lower or root.val >= upper:
            return False
        
        return all([self.middle(root.left, root.val, lower),
                    self.middle(root.right, upper, root.val)])

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nodes = []
        last = -float("inf")

        while root or nodes:
            if root:
                nodes.append(root)
                root = root.left
            else:
                root = nodes.pop()
                if root.val <= last:
                    return False
                last = root.val
                root = root.right

        return True
