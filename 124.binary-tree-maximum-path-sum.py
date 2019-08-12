# coding=utf-8
#
# @lc app=leetcode id=124 lang=python
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (29.32%)
# Likes:    1606
# Dislikes: 118
# Total Accepted:    194.9K
# Total Submissions: 647.3K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty binary tree, find the maximum path sum.
# 
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the
# root.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# Output: 6
# 
# 
# Example 2:
# 
# 
# Input: [-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# Output: 42
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
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_num = -float("inf")
        self.findMaxPath(root)
        return self.max_num

    def findMaxPath(self, root):
        left_num = 0
        right_num = 0
        if root.left:
            left_num = self.findMaxPath(root.left)
        if root.right:
            right_num = self.findMaxPath(root.right)
        self.max_num = max(root.val, root.val+left_num, root.val+right_num, root.val+left_num+right_num, self.max_num)
        return max(root.val, root.val+left_num, root.val+right_num)

# if __name__ == "__main__":
#     s = Solution()
#     head = TreeNode(2)
#     head.left = TreeNode(-1)
#     print s.maxPathSum(head)
