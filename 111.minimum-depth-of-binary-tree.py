#
# @lc app=leetcode id=111 lang=python
#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (34.86%)
# Total Accepted:    279K
# Total Submissions: 798.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given binary tree [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its minimum depth = 2.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    def __minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left or not root.right:
            return self.minDepth(root.left) + self.minDepth(root.right) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    def _minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 到最近子节点的距离
        # 子节点是指没有两片叶子的节点
        # 有一片叶子就不算
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left_depth = float("INF")
        if root.left:
            left_depth = self.minDepth(root.left)
        right_depth = float("INF")
        if root.right:
            right_depth = self.minDepth(root.right)
        return min(left_depth, right_depth) + 1

# if __name__ == "__main__":
#     s = Solution()
#     t = TreeNode(3)
#     t.left = TreeNode(2)
#     # t.right = TreeNode(4)
#     # t.right.left = TreeNode(6)
#     print s.minDepth(t)
