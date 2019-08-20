# coding=utf-8
#
# @lc app=leetcode id=653 lang=python
#
# [653] Two Sum IV - Input is a BST
#
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
#
# algorithms
# Easy (53.05%)
# Likes:    941
# Dislikes: 112
# Total Accepted:    98.1K
# Total Submissions: 184.8K
# Testcase Example:  '[5,3,6,2,4,null,7]\n9'
#
# Given a Binary Search Tree and a target number, return true if there exist
# two elements in the BST such that their sum is equal to the given target.
# 
# Example 1:
# 
# 
# Input: 
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
# 
# Target = 9
# 
# Output: True
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
# 
# Target = 28
# 
# Output: False
# 
# 
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
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        nodes = []
        values = []
        while root or nodes:
            if root:
                nodes.append(root)
                root = root.left
            else:
                root = nodes.pop()
                values.append(root.val)
                root = root.right

        v_set = set(values)
        for v in values:
            if k - v == v:
                if values.count(v) >= 2:
                    return True
            else:
                if k - v in v_set:
                    return True

        return False


# if __name__ == '__main__':
#     s = Solution()
#     head = TreeNode(1)
#     print s.findTarget(head, 2)
