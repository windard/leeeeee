#
# @lc app=leetcode id=563 lang=python
#
# [563] Binary Tree Tilt
#
# https://leetcode.com/problems/binary-tree-tilt/description/
#
# algorithms
# Easy (46.88%)
# Likes:    328
# Dislikes: 739
# Total Accepted:    52.2K
# Total Submissions: 110.9K
# Testcase Example:  '[1,2,3]'
#
# Given a binary tree, return the tilt of the whole tree.
# 
# The tilt of a tree node is defined as the absolute difference between the sum
# of all left subtree node values and the sum of all right subtree node values.
# Null node has tilt 0.
# 
# The tilt of the whole tree is defined as the sum of all nodes' tilt.
# 
# Example:
# 
# Input: 
# ⁠        1
# ⁠      /   \
# ⁠     2     3
# Output: 1
# Explanation: 
# Tilt of node 2 : 0
# Tilt of node 3 : 0
# Tilt of node 1 : |2-3| = 1
# Tilt of binary tree : 0 + 0 + 1 = 1
# 
# 
# 
# Note:
# 
# The sum of node values in any subtree won't exceed the range of 32-bit
# integer. 
# All the tilt values won't exceed the range of 32-bit integer.
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
    def _findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.total_count = 0
        left_count = self.count_tilt(root.left)
        right_count = self.count_tilt(root.right)
        self.total_count += abs(left_count - right_count)
        return self.total_count
    
    def count_tilt(self, root):
        if not root:
            return 0
        left_count = self.count_tilt(root.left)
        right_count = self.count_tilt(root.right)
        self.total_count += abs(left_count - right_count)
        return left_count + right_count + root.val

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.total_count = 0
        self.count_tilt(root)
        return self.total_count
