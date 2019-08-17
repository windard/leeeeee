# coding=utf-8
#
# @lc app=leetcode id=687 lang=python
#
# [687] Longest Univalue Path
#
# https://leetcode.com/problems/longest-univalue-path/description/
#
# algorithms
# Easy (33.36%)
# Likes:    1059
# Dislikes: 270
# Total Accepted:    64.6K
# Total Submissions: 188.4K
# Testcase Example:  '[5,4,5,1,1,5]'
#
# Given a binary tree, find the length of the longest path where each node in
# the path has the same value. This path may or may not pass through the root.
# 
# The length of path between two nodes is represented by the number of edges
# between them.
# 
# 
# 
# Example 1:
# 
# Input:
# 
# 
# ⁠             5
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         1   1   5
# 
# 
# Output: 2
# 
# 
# 
# Example 2:
# 
# Input:
# 
# 
# ⁠             1
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         4   4   5
# 
# 
# Output: 2
# 
# 
# 
# Note: The given binary tree has not more than 10000 nodes. The height of the
# tree is not more than 1000.
# 
#
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def _longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Wrong Answer
        # 路径只算边，不算高度
        # 根节点加两个子节点也可以，不一定都在一条边上
        self.max_length = 0
        self.find_max_length(root, None, 0)
        return self.max_length

    def find_max_length(self, root, value, length):
        if not root:
            return
        if root.val == value:
            length += 1
        else:
            length = 1
        self.max_length = max(self.max_length, length)
        self.find_max_length(root.left, root.val, length)
        self.find_max_length(root.right, root.val, length)

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_length = 0
        self.get_side_depth(root)
        return self.max_length

    def get_side_depth(self, root):
        if not root:
            return None, 0
        if not root.left and not root.right:
            return root.val, 0
        left_value, left_length = right_value, right_length = None, 0
        length = 0
        if root.left:
            left_value, left_length = self.get_side_depth(root.left)
            if left_value == root.val:
                left_length += 1
                self.max_length = max(left_length, self.max_length)
                length = left_length

        if root.right:
            right_value, right_length = self.get_side_depth(root.right)
            if right_value == root.val:
                right_length += 1
                self.max_length = max(self.max_length, right_length)
                length = max(length, right_length)

        if left_value == root.val == right_value:
            self.max_length = max(self.max_length, left_length + right_length)
        return root.val, length


# if __name__ == '__main__':
#     s = Solution()
#     head = TreeNode(5)
#     head.left = TreeNode(4)
#     head.right = TreeNode(5)
#     head.left.left = TreeNode(1)
#     head.left.right = TreeNode(1)
#     head.right.left = TreeNode(5)

    # head = TreeNode(1)
    # head.left = TreeNode(4)
    # head.right = TreeNode(5)
    # head.left.left = TreeNode(4)
    # head.left.right = TreeNode(4)
    # head.right.right = TreeNode(5)
    # print s.longestUnivaluePath(head)
