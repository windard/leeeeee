# coding=utf-8
#
# @lc app=leetcode id=589 lang=python
#
# [589] N-ary Tree Preorder Traversal
#
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/
#
# algorithms
# Easy (66.23%)
# Likes:    226
# Dislikes: 35
# Total Accepted:    43.8K
# Total Submissions: 64.8K
# Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
#
# Given an n-ary tree, return the preorder traversal of its nodes' values.
# 
# For example, given a 3-ary tree:
# 
# 
# 
# 
# 
# 
# 
# Return its preorder traversal as: [1,3,5,6,2,4].
# 
# 
# 
# Note:
# 
# Recursive solution is trivial, could you do it iteratively?
# 
#
# Definition for a Node.


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def _preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # 先中间，再子节点
        if not root:
            return []
        result = []
        result.extend([root.val])
        for child in root.children:
            result.extend(self.preorder(child))
        return result

    def __preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # Wrong Answer
        # 分层读取，不是按父子顺序
        nodes = [root]
        result = []
        while nodes:
            node = nodes.pop(0)
            if node:
                result.append(node.val)
                nodes.extend(node.children)
        return result

    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        nodes = []
        result = []
        while root or nodes:
            if root:
                result.append(root.val)
                children = root.children
                if children:
                    root = children[0]
                    nodes.extend(children[::-1][:-1])
                else:
                    root = None
            else:
                root = nodes.pop()

        return result
