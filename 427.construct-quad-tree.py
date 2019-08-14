# coding=utf-8
#
# @lc app=leetcode id=427 lang=python
#
# [427] Construct Quad Tree
#
# https://leetcode.com/problems/construct-quad-tree/description/
#
# algorithms
# Easy (54.28%)
# Total Accepted:    9.1K
# Total Submissions: 16.3K
# Testcase Example:  '[[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]'
#
# We want to use quad trees to store an N x N boolean grid. Each cell in the
# grid can only be true or false. The root node represents the whole grid. For
# each node, it will be subdivided into four children nodes until the values in
# the region it represents are all the same.
# 
# Each node has another two boolean attributes : isLeaf and val. isLeaf is true
# if and only if the node is a leaf node. The val attribute for a leaf node
# contains the value of the region it represents.
# 
# Your task is to use a quad tree to represent a given grid. The following
# example may help you understand the problem better:
# 
# Given the 8 x 8 grid below, we want to construct the corresponding quad
# tree:
# 
# 
# 
# It can be divided according to the definition above:
# 
# 
# 
# 
# 
# The corresponding quad tree should be as following, where each node is
# represented as a (isLeaf, val) pair.
# 
# For the non-leaf nodes, val can be arbitrary, so it is represented as *.
# 
# 
# 
# Note:
# 
# 
# N is less than 1000 and guaranteened to be a power of 2.
# If you want to know more about the quad tree, you can refer to its wiki.
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
    def _construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        # maximum recursion depth exceeded
        # 递归超限，使用循环
        return self.generate(grid, 0, len(grid)-1, 0, len(grid[0])-1)

    def generate(self, grid, left, right, top, down):
        if left == right:
            return Node(grid[left][top], True, None, None, None, None)
        topLeft = grid[(left+right)/2][(top+down)/2]
        topRight = grid[(left+right)/2][(top+down)/2+1]
        downLeft = grid[(left+right)/2+1][(top+down)/2]
        downRight = grid[(left+right)/2+1][(top+down)/2+1]
        if sum([topLeft, topRight, downLeft, downRight]) == 4:
            return Node(True, True, None, None, None, None)
        elif sum([topLeft, topRight, downLeft, downRight]) == 0:
            return Node(False, True, None, None, None, None)

        topLeftNode = self.generate(grid, left, (left+right)/2, top, (top+down)/2)
        topRightNode = self.generate(grid, left, (left+right)/2, (top+down)/2, down)
        downLeftNode = self.generate(grid, (left+right)/2, right, top, (top+down)/2)
        downRightNode = self.generate(grid, (left+right)/2, right, (top+down)/2, down)
        return Node(True, False, topLeftNode, topRightNode, downLeftNode, downRightNode)

    def __construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        # Wrong Answer
        if not grid:
            return None
        left, right, top, down = 0, len(grid)-1, 0, len(grid[0])-1
        blocks = [[left, right, top, down]]
        nodes = []
        posi = None
        pos = {
            0: 'topLeft',
            1: 'topRight',
            2: 'bottomLeft',
            3: 'bottomRight',
        }
        root = None
        while blocks:
            left, right, top, down = blocks.pop(0)
            topLeft = grid[(left + right) / 2][(top + down) / 2]
            topRight = grid[(left + right) / 2][(top + down) / 2 + 1]
            downLeft = grid[(left + right) / 2 + 1][(top + down) / 2]
            downRight = grid[(left + right) / 2 + 1][(top + down) / 2 + 1]
            if sum([topLeft, topRight, downLeft, downRight]) == 4:
                node = Node(True, True, None, None, None, None)
                if nodes:
                    head = nodes.pop(0)
                    setattr(head, pos.get(posi), node)
                    posi = (posi + 1) % 4
                else:
                    root = node
            elif sum([topLeft, topRight, downLeft, downRight]) == 0:
                node = Node(False, True, None, None, None, None)
                if nodes:
                    head = nodes.pop(0)
                    setattr(head, pos.get(posi), node)
                    posi = (posi + 1) % 4
                else:
                    root = node
            else:
                node = Node(True, False, None, None, None, None)
                if nodes:
                    head = nodes.pop(0)
                    setattr(head, pos.get(posi), node)
                    posi = (posi + 1) % 4
                else:
                    root = node
                    posi = 0
                blocks.append([left, (left+right)/2, top, (top+down)/2])
                blocks.append([left, (left+right)/2, (top+down)/2, down])
                blocks.append([(left+right)/2, right, top, (top+down)/2])
                blocks.append([(left+right)/2, right, (top+down)/2, down])
                nodes.append(node)
                nodes.append(node)
                nodes.append(node)
                nodes.append(node)
        return root

    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        if not grid:
            return None
        top, bottom, left, right = 0, len(grid)-1, 0, len(grid[0])-1
        return self.create(grid, top, bottom, left, right)

    def create(self, grid, top, bottom, left, right):
        if top == bottom:
            return Node(grid[top][left], True, None, None, None, None)
        topLeft = self.create(grid, top, (top+bottom)/2, left, (left+right)/2)
        topRight = self.create(grid, top, (top+bottom)/2, (left+right)/2+1, right)
        bottomLeft = self.create(grid, (top+bottom)/2+1, bottom, left, (left+right)/2)
        bottomRight = self.create(grid, (top+bottom)/2+1, bottom, (left+right)/2+1, right)
        if all([topLeft.isLeaf, topRight.isLeaf, bottomLeft.isLeaf, bottomRight.isLeaf]):
            if topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
                return Node(topLeft.val, True, None, None, None, None)
        return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)


# if __name__ == "__main__":
#     s = Solution()
#     print s.construct([[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]])
#     print s.construct([[1,1,0,0,0,0,0,0],[1,1,0,0,0,0,0,0],[1,1,0,0,0,0,1,1],[1,1,0,0,0,0,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,1,1],[1,1,1,1,1,1,0,0],[1,1,1,1,1,1,0,0]])
