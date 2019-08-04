#
# @lc app=leetcode id=701 lang=python
#
# [701] Insert into a Binary Search Tree
#
# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
#
# algorithms
# Medium (73.81%)
# Likes:    381
# Dislikes: 47
# Total Accepted:    52.6K
# Total Submissions: 68.8K
# Testcase Example:  '[4,2,7,1,3]\n5'
#
# Given the root node of a binary search tree (BST) and a value to be inserted
# into the tree, insert the value into the BST. Return the root node of the BST
# after the insertion. It is guaranteed that the new value does not exist in
# the original BST.
# 
# Note that there may exist multiple valid ways for the insertion, as long as
# the tree remains a BST after insertion. You can return any of them.
# 
# For example, 
# 
# 
# Given the tree:
# ⁠       4
# ⁠      / \
# ⁠     2   7
# ⁠    / \
# ⁠   1   3
# And the value to insert: 5
# 
# 
# You can return this binary search tree:
# 
# 
# ⁠        4
# ⁠      /   \
# ⁠     2     7
# ⁠    / \   /
# ⁠   1   3 5
# 
# 
# This tree is also valid:
# 
# 
# ⁠        5
# ⁠      /   \
# ⁠     2     7
# ⁠    / \   
# ⁠   1   3
# ⁠        \
# ⁠         4
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
    def _insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # recursion
        if root.val >= val:
            if root.left:
                self.insertIntoBST(root.left, val)
            else:
                node = TreeNode(val)
                root.left = node
        else:
            if root.right:
                self.insertIntoBST(root.right, val)
            else:
                node = TreeNode(val)
                root.right = node
        return root

    def __insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # better recursion
        if not root:
            return TreeNode(val)
        if root.val >= val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

    def ___insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # iteration
        if not root:
            return TreeNode(val)

        head = root
        nodes = [root, root.left, root.right]
        while nodes:
            root = nodes.pop(0)
            left = nodes.pop(0)
            right = nodes.pop(0)

            if root.val >= val:
                if left:
                    nodes.append(left)
                    nodes.append(left.left)
                    nodes.append(left.right)
                else:
                    root.left = TreeNode(val)
            else:
                if right:
                    nodes.append(right)
                    nodes.append(right.left)
                    nodes.append(right.right)
                else:
                    root.right = TreeNode(val)
        return head


    def ____insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # iteration
        if not root:
            return TreeNode(val)

        head = root
        nodes = [root]
        while nodes:
            root = nodes.pop(0)

            if root.val >= val:
                if root.left:
                    nodes.append(root.left)
                else:
                    root.left = TreeNode(val)
            else:
                if root.right:
                    nodes.append(root.right)
                else:
                    root.right = TreeNode(val)
        return head

    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        if not root:
            return TreeNode(val)

        head = root
        while root:
            if root.val >= val:
                if not root.left:
                    root.left = TreeNode(val)
                    break
                else:
                    root = root.left
            else:
                if not root.right:
                    root.right = TreeNode(val)
                    break
                else:
                    root = root.right
        return head
