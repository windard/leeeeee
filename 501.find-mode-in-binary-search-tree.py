# coding=utf-8
#
# @lc app=leetcode id=501 lang=python
#
# [501] Find Mode in Binary Search Tree
#
# https://leetcode.com/problems/find-mode-in-binary-search-tree/description/
#
# algorithms
# Easy (38.90%)
# Likes:    555
# Dislikes: 217
# Total Accepted:    56.8K
# Total Submissions: 143.6K
# Testcase Example:  '[1,null,2,2]'
#
# Given a binary search tree (BST) with duplicates, find all the mode(s) (the
# most frequently occurred element) in the given BST.
# 
# Assume a BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than or equal
# to the node's key.
# The right subtree of a node contains only nodes with keys greater than or
# equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# 
# For example:
# Given BST [1,null,2,2],
# 
# 
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  2
# 
# 
# 
# 
# return [2].
# 
# Note: If a tree has more than one mode, you can return them in any order.
# 
# Follow up: Could you do that without using any extra space? (Assume that the
# implicit stack space incurred due to recursion does not count).
# 
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def _findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Time Limit Exceeded
        self.counter = {}
        self.depth(root)
        return [key for key, value in self.counter.items() if value == max(self.counter.values())]

    def depth(self, root):
        if not root:
            return
        self.counter[root.val] = self.counter.get(root.val, 0) + 1
        self.depth(root.left)
        self.depth(root.right)

    def __findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 按照完全搜索树来做🌲
        # 根据中序遍历结果找频次最高的数
        if not root:
            return []
        nodes = []
        last = None
        index = 0
        max_index = 0
        max_root = []
        while root or nodes:
            if root:
                nodes.append(root)
                root = root.left
            else:
                root = nodes.pop()
                if last == root.val:
                    index += 1
                else:
                    if index == max_index:
                        max_root.append(last)
                    elif index > max_index:
                        max_root = [last]
                        max_index = index
                    index = 1
                last = root.val
                root = root.right
        if index == max_index:
            max_root.append(last)
        elif index > max_index:
            max_root = [last]
        return max_root

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.pre = None
        self.current = 0
        self.max_index = 0
        self.max_root = []
        self.inorder(root)
        return self.max_root
    
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if root.val == self.pre:
            self.current += 1
        else:
            self.current = 1
        if self.current == self.max_index:
            self.max_root.append(root.val)
        elif self.current > self.max_index:
            self.max_root = [root.val]
            self.max_index = self.current

        self.pre = root.val
        self.inorder(root.right)

# if __name__ == "__main__":
#     s = Solution()
#     head = TreeNode(1)
#     head.right = TreeNode(2)
#     head.right.left = TreeNode(2)
#     print s.findMode(head)
