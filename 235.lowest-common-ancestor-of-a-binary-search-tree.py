#
# @lc app=leetcode id=235 lang=python
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
#
# algorithms
# Easy (43.47%)
# Likes:    973
# Dislikes: 78
# Total Accepted:    275.4K
# Total Submissions: 620.8K
# Testcase Example:  '[6,2,8,0,4,7,9,null,null,3,5]\n2\n8'
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of
# two given nodes in the BST.
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of itself).”
# 
# Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# 
# 
# Example 2:
# 
# 
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant
# of itself according to the LCA definition.
# 
# 
# 
# 
# Note:
# 
# 
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the BST.
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
    def _lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if self.isCommonSonOfRoot(root.left, p, q):
            return self.lowestCommonAncestor(root.left, p ,q)
        if self.isCommonSonOfRoot(root.right, p, q):
            return self.lowestCommonAncestor(root.right, p, q)

        return root

    def isCommonSonOfRoot(self, root, p, q):
        return self.isSonOfRoot(root, p) and self.isSonOfRoot(root, q)

    def isSonOfRoot(self, root, son):
        if not root:
            return False
        if root.val == son.val:
            return True
        return self.isSonOfRoot(root.left, son) or self.isSonOfRoot(root.right, son)

    def lowestCommonAncestor(self, root, p, q):
        # copy one
        # 二叉搜索树的特性
        # 1. 父节点的值在左右子节点中间
        # 2. 左节点的值小于右节点
        while (root.val - p.val) * (root.val - q.val) > 0: root = (root.left, root.right)[p.val > root.val]
        return root

    def ____lowestCommonAncestor(self, root, p, q):
        # 二叉搜索树的特性
        # 父节点的值在两节点的值中间
        # Total Wrong
        if not root:
            return 
        lr = self.lowestCommonAncestor(root.left, p, q)
        if lr:
            return lr
        rr = self.lowestCommonAncestor(root.right, p, q)
        if rr:
            return rr
        if p.val < root.val < q.val or q.val < root.val < p.val:
            return root
