#
# @lc app=leetcode id=700 lang=python
#
# [700] Search in a Binary Search Tree
#
# https://leetcode.com/problems/search-in-a-binary-search-tree/description/
#
# algorithms
# Easy (66.82%)
# Likes:    353
# Dislikes: 95
# Total Accepted:    70.7K
# Total Submissions: 102.6K
# Testcase Example:  '[4,2,7,1,3]\n2'
#
# Given the root node of a binary search tree (BST) and a value. You need to
# find the node in the BST that the node's value equals the given value. Return
# the subtree rooted with that node. If such node doesn't exist, you should
# return NULL.
# 
# For example, 
# 
# 
# Given the tree:
# ⁠       4
# ⁠      / \
# ⁠     2   7
# ⁠    / \
# ⁠   1   3
# 
# And the value to search: 2
# 
# 
# You should return this subtree:
# 
# 
# ⁠     2     
# ⁠    / \   
# ⁠   1   3
# 
# 
# In the example above, if we want to search the value 5, since there is no
# node with value 5, we should return NULL.
# 
# Note that an empty tree is represented by NULL, therefore you would see the
# expected output (serialized tree format) as [], not null.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
