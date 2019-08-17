# coding=utf-8
#
# @lc app=leetcode id=1022 lang=python
#
# [1022] Sum of Root To Leaf Binary Numbers
#
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/
#
# algorithms
# Easy (58.70%)
# Likes:    144
# Dislikes: 55
# Total Accepted:    16.3K
# Total Submissions: 27.7K
# Testcase Example:  '[1,0,1,0,1,0,1]'
#
# Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path
# represents a binary number starting with the most significant bit.  For
# example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent
# 01101 in binary, which is 13.
# 
# For all leaves in the tree, consider the numbers represented by the path from
# the root to that leaf.
# 
# Return the sum of these numbers.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the tree is between 1 and 1000.
# node.val is 0 or 1.
# The answer will not exceed 2^31 - 1.
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
    def _sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = 0
        path = self.rootToLeaf(root, [])
        for p in path:
            count += int(''.join(map(str, p)), 2)
        return count

    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = [root]
        path = []
        count = 0
        while nodes:
            node = nodes.pop(0)
            if not node:
                continue
            if path:
                p = path.pop(0)
                p.append(node.val)
            else:
                p = [node.val]

            if node.left:
                nodes.append(node.left)
                path.append(p[:])
            if node.right:
                nodes.append(node.right)
                path.append(p)
            if not node.left and not node.right:
                count += int(''.join(map(str, p)), 2)
        return count

    def rootToLeaf(self, root, path):
        if not root:
            return path
        current = path[:]
        current.append(root.val)
        result = []
        if root.right:
            result += self.rootToLeaf(root.right, current)
        if root.left:
            result += self.rootToLeaf(root.left, current)
        if not root.left and not root.right:
            result.append(current)
        return result


# if __name__ == '__main__':
#     s = Solution()
#     head = TreeNode(1)
#     head.left = TreeNode(0)
#     head.right = TreeNode(1)
#     head.left.left = TreeNode(0)
#     head.left.right = TreeNode(1)
#     head.right.left = TreeNode(0)
#     head.right.right = TreeNode(1)
#     print s.sumRootToLeaf(head)
