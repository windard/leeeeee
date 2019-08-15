# coding=utf-8
#
# @lc app=leetcode id=590 lang=python
#
# [590] N-ary Tree Postorder Traversal
#
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/
#
# algorithms
# Easy (66.15%)
# Likes:    285
# Dislikes: 37
# Total Accepted:    39.9K
# Total Submissions: 59.1K
# Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
#
# Given an n-ary tree, return the postorder traversal of its nodes' values.
# 
# For example, given a 3-ary tree:
# 
# 
# 
# 
# 
# 
# 
# Return its postorder traversal as: [5,6,3,2,4,1].
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
    def _postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # 先子节点，再中节点

        if not root:
            return []
        result = []
        for child in root.children:
            result.extend(self.postorder(child))
        result.extend([root.val])
        return result

    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # 使用循环做后续遍历
        # 1. 逆序
        # 2. 存储已访问过节点
        nodes = []
        result = []
        touch = set()
        while root or nodes:
            if root:
                if root in touch:
                    result.append(root.val)
                    root = None
                    continue
                touch.add(root)
                children = root.children
                if children:
                    nodes.append(root)
                    root = children[0]
                    nodes.extend(children[::-1][:-1])
                else:
                    result.append(root.val)
                    root = None
            else:
                root = nodes.pop()

        return result
