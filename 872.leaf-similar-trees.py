# coding=utf-8
#
# @lc app=leetcode id=872 lang=python
#
# [872] Leaf-Similar Trees
#
# https://leetcode.com/problems/leaf-similar-trees/description/
#
# algorithms
# Easy (62.19%)
# Likes:    427
# Dislikes: 25
# Total Accepted:    52.5K
# Total Submissions: 82.3K
# Testcase Example:  '[3,5,1,6,2,9,8,null,null,7,4]\n' +
#  '[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]'
#
# Consider all the leaves of a binary tree.  From left to right order, the
# values of those leaves form a leaf value sequence.
# 
# 
# 
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9,
# 8).
# 
# Two binary trees are considered leaf-similar if their leaf value sequence is
# the same.
# 
# Return true if and only if the two given trees with head nodes root1 and
# root2 are leaf-similar.
# 
# 
# 
# Note:
# 
# 
# Both of the given trees will have between 1 and 100 nodes.
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
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        nodes = [root1]
        leaf_a = []
        while nodes:
            node = nodes.pop()
            if not node:
                continue
            if not node.left and not node.right:
                leaf_a.append(node.val)
            nodes.append(node.left)
            nodes.append(node.right)

        nodes = [root2]
        leaf_b = []
        while nodes:
            node = nodes.pop()
            if not node:
                continue
            if not node.left and not node.right:
                leaf_b.append(node.val)
            nodes.append(node.left)
            nodes.append(node.right)

        return leaf_a == leaf_b
