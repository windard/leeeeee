# coding=utf-8
#
# @lc app=leetcode id=617 lang=python
#
# [617] Merge Two Binary Trees
#
# https://leetcode.com/problems/merge-two-binary-trees/description/
#
# algorithms
# Easy (70.89%)
# Likes:    1984
# Dislikes: 137
# Total Accepted:    198.8K
# Total Submissions: 280.3K
# Testcase Example:  '[1,3,2,5]\n[2,1,3,null,4,null,7]'
#
# Given two binary trees and imagine that when you put one of them to cover the
# other, some nodes of the two trees are overlapped while the others are not.
# 
# You need to merge them into a new binary tree. The merge rule is that if two
# nodes overlap, then sum node values up as the new value of the merged node.
# Otherwise, the NOT null node will be used as the node of new tree.
# 
# Example 1:
# 
# 
# Input: 
# Tree 1                     Tree 2                  
# ⁠         1                         2                             
# ⁠        / \                       / \                            
# ⁠       3   2                     1   3                        
# ⁠      /                           \   \                      
# ⁠     5                             4   7                  
# Output: 
# Merged tree:
# 3
# / \
# 4   5
# / \   \ 
# 5   4   7
# 
# 
# 
# 
# Note: The merging process must start from the root nodes of both trees.
# 
#
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val = t1.val + t2.val
        if not t1.left:
            t1.left = t2.left
        else:
            self.mergeTrees(t1.left, t2.left)
        if not t1.right:
            t1.right = t2.right
        else:
            self.mergeTrees(t1.right, t2.right)
        return t1
