#
# @lc app=leetcode id=558 lang=python
#
# [558] Quad Tree Intersection
#
# https://leetcode.com/problems/quad-tree-intersection/description/
#
# algorithms
# Easy (39.60%)
# Likes:    43
# Dislikes: 203
# Total Accepted:    4.6K
# Total Submissions: 11.2K
# Testcase Example:  '{"$id":"1","bottomLeft":{"$id":"4","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":false},"bottomRight":{"$id":"5","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":false},"isLeaf":false,"topLeft":{"$id":"2","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":true},"topRight":{"$id":"3","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":true},"val":true}\n' +
#  '{"$id":"1","bottomLeft":{"$id":"8","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":true},"bottomRight":{"$id":"9","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":false},"isLeaf":false,"topLeft":{"$id":"2","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":true},"topRight":{"$id":"3","bottomLeft":{"$id":"6","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":true},"bottomRight":{"$id":"7","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":true},"isLeaf":false,"topLeft":{"$id":"4","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":false},"topRight":{"$id":"5","bottomLeft":null,"bottomRight":null,"isLeaf":true,"topLeft":null,"topRight":null,"val":false},"val":true},"val":true}'
#
# A quadtree is a tree data in which each internal node has exactly four
# children: topLeft, topRight, bottomLeft and bottomRight. Quad trees are often
# used to partition a two-dimensional space by recursively subdividing it into
# four quadrants or regions.
# 
# We want to store True/False information in our quad tree. The quad tree is
# used to represent a N * N boolean grid. For each node, it will be subdivided
# into four children nodes until the values in the region it represents are all
# the same. Each node has another two boolean attributes : isLeaf and val.
# isLeaf is true if and only if the node is a leaf node. The val attribute for
# a leaf node contains the value of the region it represents.
# 
# For example, below are two quad trees A and B:
# 
# 
# A:
# +-------+-------+   T: true
# |       |       |   F: false
# |   T   |   T   |
# |       |       |
# +-------+-------+
# |       |       |
# |   F   |   F   |
# |       |       |
# +-------+-------+
# topLeft: T
# topRight: T
# bottomLeft: F
# bottomRight: F
# 
# B:               
# +-------+---+---+
# |       | F | F |
# |   T   +---+---+
# |       | T | T |
# +-------+---+---+
# |       |       |
# |   T   |   F   |
# |       |       |
# +-------+-------+
# topLeft: T
# topRight:
# ⁠    topLeft: F
# ⁠    topRight: F
# ⁠    bottomLeft: T
# ⁠    bottomRight: T
# bottomLeft: T
# bottomRight: F
# 
# 
# 
# 
# Your task is to implement a function that will take two quadtrees and return
# a quadtree that represents the logical OR (or union) of the two trees.
# 
# 
# A:                 B:                 C (A or B):
# +-------+-------+  +-------+---+---+  +-------+-------+
# |       |       |  |       | F | F |  |       |       |
# |   T   |   T   |  |   T   +---+---+  |   T   |   T   |
# |       |       |  |       | T | T |  |       |       |
# +-------+-------+  +-------+---+---+  +-------+-------+
# |       |       |  |       |       |  |       |       |
# |   F   |   F   |  |   T   |   F   |  |   T   |   F   |
# |       |       |  |       |       |  |       |       |
# +-------+-------+  +-------+-------+  +-------+-------+
# 
# 
# Note:
# 
# 
# Both A and B represent grids of size N * N.
# N is guaranteed to be a power of 2.
# If you want to know more about the quad tree, you can refer to its wiki.
# The logic OR operation is defined as this: "A or B" is true if A is true, or
# if B is true, or if both A and B are true.
# 
# 
#
# Definition for a QuadTree node.


class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        if not quadTree2:
            return quadTree1
        if not quadTree1:
            return quadTree2
        if not quadTree1 and not quadTree2:
            return
        if (quadTree1.isLeaf and quadTree1.val) or (quadTree2.isLeaf and quadTree2.val):
            quadTree1.isLeaf = True
            quadTree1.val = True
        elif (quadTree1.isLeaf and quadTree2.isLeaf):
            quadTree1.isLeaf = True
            quadTree1.val = False
        else:
            quadTree1.isLeaf = False
            quadTree1.val = False
            topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
            topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
            bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
            bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

            if (topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf) and \
                    (topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
                quadTree1.isLeaf = True
                quadTree1.val = topLeft.val
                return quadTree1
            quadTree1.topLeft = topLeft
            quadTree1.topRight = topRight
            quadTree1.bottomLeft = bottomLeft
            quadTree1.bottomRight = bottomRight
        return quadTree1
