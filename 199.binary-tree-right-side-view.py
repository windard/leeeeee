# coding=utf-8
#
# @lc app=leetcode id=199 lang=python
#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (48.97%)
# Likes:    1212
# Dislikes: 58
# Total Accepted:    185.3K
# Total Submissions: 377.9K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
# 
# Example:
# 
# 
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
# 
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
# 
#
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def _rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodes = [[root]]
        result = []
        while nodes:
            level = nodes.pop()
            current = []
            down = []
            for node in level:
                if node:
                    down.append(node.val)
                    if node.left:
                        current.append(node.left)
                    if node.right:
                        current.append(node.right)
                
            if down:
                result.append(down)
            if current:
                nodes.append(current)

        return [l[-1] for l in result]        

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodes = [[root]]
        result = []
        while nodes:
            level = nodes.pop()
            current = []
            down = None
            for node in level:
                if node:
                    down = node.val
                    if node.left:
                        current.append(node.left)
                    if node.right:
                        current.append(node.right)
            # down might be 0
            if down != None:
                result.append(down)
            if current:
                nodes.append(current)

        return result
