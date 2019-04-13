#
# @lc app=leetcode id=404 lang=python
#
# [404] Sum of Left Leaves
#
# https://leetcode.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (48.72%)
# Total Accepted:    121K
# Total Submissions: 247.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Find the sum of all left leaves in a given binary tree.
# 
# Example:
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# There are two left leaves in the binary tree, with values 9 and 15
# respectively. Return 24.
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
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # but slower
        if not root:
            return 0
        return self.getLeavesVal(root.left, True) + self.getLeavesVal(root.right, False) 

    def getLeavesVal(self, root, flag):
        # check is left
        if not root:
            return 0
        if not root.left and not root.right:
            if flag:
                return root.val
            else:
                return 0
        return self.getLeavesVal(root.left, True) + self.getLeavesVal(root.right, False) 

    def _sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left:
            if root.left.left or root.left.right:
                return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
            else:
                return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.right)
