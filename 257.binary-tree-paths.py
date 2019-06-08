#
# @lc app=leetcode id=257 lang=python
#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (45.03%)
# Likes:    835
# Dislikes: 65
# Total Accepted:    221.4K
# Total Submissions: 484.4K
# Testcase Example:  '[1,2,3,null,5]'
#
# Given a binary tree, return all root-to-leaf paths.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# 
# Input:
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# Output: ["1->2->5", "1->3"]
# 
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        return self.findPath(root, "{}".format(root.val))

    def findPath(self, root, path):
        if not root.left and not root.right:
            return [path]
        elif not root.right:
            return self.findPath(root.left, path+"->{}".format(root.left.val))
        elif not root.left:
            return self.findPath(root.right, path+"->{}".format(root.right.val))
        else:
            lp = self.findPath(root.left, path+"->{}".format(root.left.val))
            rp = self.findPath(root.right, path+"->{}".format(root.right.val))
            return lp + rp

