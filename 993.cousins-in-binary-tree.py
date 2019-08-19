# coding=utf-8
#
# @lc app=leetcode id=993 lang=python
#
# [993] Cousins in Binary Tree
#
# https://leetcode.com/problems/cousins-in-binary-tree/description/
#
# algorithms
# Easy (52.22%)
# Likes:    244
# Dislikes: 19
# Total Accepted:    23.4K
# Total Submissions: 44.9K
# Testcase Example:  '[1,2,3,4]\n4\n3'
#
# In a binary tree, the root node is at depth 0, and children of each depth k
# node are at depth k+1.
# 
# Two nodes of a binary tree are cousins if they have the same depth, but have
# different parents.
# 
# We are given the root of a binary tree with unique values, and the values x
# and y of two different nodes in the tree.
# 
# Return true if and only if the nodes corresponding to the values x and y are
# cousins.
# 
# 
# 
# Example 1:
# 
# 
# 
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
# 
# 
# 
# Example 2:
# 
# 
# 
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
# 
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the tree will be between 2 and 100.
# Each node has a unique integer value from 1 to 100.
# 
# 
# 
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
    def _isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        # Wrong Answer
        # 必须是不同的父节点
        length_a = self.find_length(root, x, 0)
        if length_a < 0:
            return False
        length_b = self.find_length(root, y, 0)
        if length_b < 0:
            return False
        return length_b == length_a

    def find_length(self, root, x, length):
        if not root:
            return -1
        if root.val == x:
            return length
        left = self.find_length(root.left, x, length+1)
        if left > 0:
            return left
        right = self.find_length(root.right, x, length+1)
        if right > 0:
            return right
        return -1

    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if not root:
            return False
        if x == y:
            return False
        nodes = [[root]]
        position_x = []
        position_y = []
        length = 0
        while nodes:
            length += 1
            level = nodes.pop()
            current = []
            for node in level:
                if node:
                    for child in [node.left, node.right]:
                        if child and child.val == x:
                            position_x.append(node.val)
                            position_x.append(length)
                        if child and child.val == y:
                            position_y.append(node.val)
                            position_y.append(length)
                    current.append(node.left)
                    current.append(node.right)
            if current:
                nodes.append(current)
        if not position_x or not position_y:
            return False
        return position_x[0] != position_y[0] and position_y[1] == position_x[1]


