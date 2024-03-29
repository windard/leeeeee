#
# @lc app=leetcode id=116 lang=python
#
# [116] Populating Next Right Pointers in Each Node
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
#
# algorithms
# Medium (36.78%)
# Likes:    1013
# Dislikes: 87
# Total Accepted:    246.7K
# Total Submissions: 648.8K
# Testcase Example:  '{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}'
#
# You are given a perfect binary tree where all leaves are on the same level,
# and every parent has two children. The binary tree has the following
# definition:
# 
# 
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
# 
# 
# Populate each next pointer to point to its next right node. If there is no
# next right node, the next pointer should be set to NULL.
# 
# Initially, all next pointers are set to NULL.
# 
# 
# 
# Example:
# 
# 
# 
# 
# Input:
# {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}
# 
# Output:
# {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}
# 
# Explanation: Given the above perfect binary tree (Figure A), your function
# should populate each next pointer to point to its next right node, just like
# in Figure B.
# 
# 
# 
# 
# Note:
# 
# 
# You may only use constant extra space.
# Recursive approach is fine, implicit stack space does not count as extra
# space for this problem.
# 
# 
#
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def _connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        head = root
        nodes = [[root]]
        while nodes:
            roots = nodes.pop()
            level = []
            last = None
            for root in roots:
                if last:
                    last.next = root
                last = root
                if root.left:
                    level.append(root.left)
                if root.right:
                    level.append(root.right)
            if not level:
                break
            nodes.append(level)
        return head

    def __connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        self.connectLast(root, None)
        return root
    
    def connectLast(self, head, last):
        if not head.left:
            return
        head.left.next = head.right
        if last:
            last.right.next = head.left
            last = last.right
        self.connectLast(head.left, last)
        self.connectLast(head.right, head.left)

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.leftAndRight(root)
        return root

    def leftAndRight(self, root):
        if not root or not root.left:
            return
        root.left.next = root.right
        self.leftAndRight(root.left)
        self.leftAndRight(root.right)
        left = root.left
        right = root.right
        while left.right:
            left.right.next = right.left
            left = left.right
            right = right.left
