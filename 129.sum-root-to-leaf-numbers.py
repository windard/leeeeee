# coding=utf-8
#
# @lc app=leetcode id=129 lang=python
#
# [129] Sum Root to Leaf Numbers
#
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
#
# algorithms
# Medium (41.44%)
# Likes:    670
# Dislikes: 24
# Total Accepted:    186.5K
# Total Submissions: 437.8K
# Testcase Example:  '[1,2,3]'
#
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path
# could represent a number.
# 
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# 
# Find the total sum of all root-to-leaf numbers.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# 
# Input: [1,2,3]
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
# 
# Example 2:
# 
# 
# Input: [4,9,0,5,1]
# ⁠   4
# ⁠  / \
# ⁠ 9   0
# / \
# 5   1
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
# 
#
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def _sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        pathes = self.getPath(root, [])
        nums = []
        for path in pathes:
            nums.append(int(''.join(map(str, path))))
        return sum(nums)

    def getPath(self, root, path):
        if not root:
            return [path]
        current = path[:]
        current.append(root.val)
        if not root.left and not root.right:
            return [current]
        if not root.left:
            return self.getPath(root.right, current)
        if not root.right:
            return self.getPath(root.left, current)
        return self.getPath(root.left, current) + self.getPath(root.right, current)

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.getPathSum(root, [])
    
    def getPathSum(self, root, path):
        current = path[:]
        current.append(root.val)
        if not root.left and not root.right:
            return int(''.join(map(str, current)))
        if not root.left:
            return self.getPathSum(root.right, current)
        if not root.right:
            return self.getPathSum(root.left, current)
        return self.getPathSum(root.left, current) + self.getPathSum(root.right, current)

# if __name__ == '__main__':
#     s = Solution()
#     head = TreeNode(4)
#     head.left = TreeNode(9)
#     head.right = TreeNode(0)
#     head.left.left = TreeNode(5)
#     head.left.right = TreeNode(1)
#     print s.sumNumbers(head)
