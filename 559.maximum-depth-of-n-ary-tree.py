#
# @lc app=leetcode id=559 lang=python
#
# [559] Maximum Depth of N-ary Tree
#
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/
#
# algorithms
# Easy (64.53%)
# Likes:    353
# Dislikes: 20
# Total Accepted:    48.3K
# Total Submissions: 73.7K
# Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
#
# Given a n-ary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
# 
# For example, given a 3-ary tree:
# 
# 
# 
# 
# 
# 
# We should return its max depth, which is 3.
# 
# 
# 
# Note:
# 
# 
# The depth of the tree is at most 1000.
# The total number of nodes is at most 5000.
# 
# 
#
# Definition for a Node.
class Node(object):
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        nodes = []
        nodes.append(root)
        index = 0
        while nodes:
            for _ in range(len(nodes)):
                node = nodes.pop(0)
                nodes.extend(node.children)
            index += 1
        return index


# if __name__ == "__main__":
#     s = Solution()
#     head = Node(4, [])
#     head = Node(5, [head])
#     head = Node(6, [head, Node(5, [])])
#     head = Node(7, [head, Node(6, [])])
#     head = Node(5, [head, Node(1, [])])
    # head = Node(5, [head, Node(5, [])])
    # head = Node(5, [head, Node(6, [])])
    # head = Node(5, [head, Node(7, [])])
    # head = Node(5, [head, Node(4, [])])
    # head = Node(5, [head, head, head])
    # head = Node(5, [head, head])
    # head = Node(5, [head])
    # head = Node(5, [head])
    # print s.maxDepth(head)
