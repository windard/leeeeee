# coding=utf-8
#
# @lc app=leetcode id=106 lang=python
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (37.98%)
# Likes:    862
# Dislikes: 18
# Total Accepted:    154.9K
# Total Submissions: 392.4K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# Given inorder and postorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# For example, given
# 
# 
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# 
# Return the following binary tree:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return
        root_val = postorder[-1]
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)

        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index+1:]

        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder):-1]
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        return root


# if __name__ == '__main__':
#     s = Solution()
#     print s.buildTree([9,3,15,20,7], [9,15,7,20,3])
