# coding=utf-8
#
# @lc app=leetcode id=236 lang=python
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (38.83%)
# Likes:    2223
# Dislikes: 143
# Total Accepted:    310.1K
# Total Submissions: 795.5K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
# in the tree.
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of itself).”
# 
# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# 
# 
# Example 2:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
# of itself according to the LCA definition.
# 
# 
# 
# 
# Note:
# 
# 
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the binary tree.
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
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 必须没有重复的出现
        self.father = None
        self.getNodeDepth(root, p, q)
        return self.father

    def getNodeDepth(self, root, p, q):
        if not root:
            return
        one = root.val in [p.val, q.val]
        left = self.getNodeDepth(root.left, p, q)
        right = self.getNodeDepth(root.right, p, q)
        if (one and left) or (one and right) or (left and right):
            self.father = root
        return one or left or right


# if __name__ == '__main__':
#     s = Solution()
#     head = TreeNode(3)
#     head.left = TreeNode(5)
#     head.right = TreeNode(1)
#     head.left.left = TreeNode(6)
#     head.left.right = TreeNode(2)
#     head.left.right.left = TreeNode(7)
#     head.left.right.right = TreeNode(4)
#     head.right.left = TreeNode(0)
#     head.right.right = TreeNode(8)
#     print s.lowestCommonAncestor(head, 5, 1)
