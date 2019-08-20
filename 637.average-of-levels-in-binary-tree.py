# coding=utf-8
#
# @lc app=leetcode id=637 lang=python
#
# [637] Average of Levels in Binary Tree
#
# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
#
# algorithms
# Easy (59.43%)
# Likes:    858
# Dislikes: 128
# Total Accepted:    86.3K
# Total Submissions: 145.2K
# Testcase Example:  '[3,9,20,15,7]'
#
# Given a non-empty binary tree, return the average value of the nodes on each
# level in the form of an array.
# 
# Example 1:
# 
# Input:
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level
# 2 is 11. Hence return [3, 14.5, 11].
# 
# 
# 
# Note:
# 
# The range of node's value is in the range of 32-bit signed integer.
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
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        nodes = [[root]]
        result = []
        while nodes:
            level = nodes.pop()
            values = []
            current = []
            for node in level:
                if node:
                    values.append(node.val)
                    current.append(node.left)
                    current.append(node.right)
            if values:
                result.append(sum(values) / float(len(values)))

            if current:
                nodes.append(current)

        return result
