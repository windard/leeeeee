# coding=utf-8
#
# @lc app=leetcode id=94 lang=python
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (54.61%)
# Total Accepted:    407.7K
# Total Submissions: 742.3K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,3,2]
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def _inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 中序遍历
        # 左中右
        res = []
        if root:
            res.extend(self._inorderTraversal(root.left))
            res.append(root.val)
            res.extend(self._inorderTraversal(root.right))
        return res

    def __inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Morris Traversal
        res = []
        current_node = pre_node = root
        while current_node:
            if not current_node.left:
                res.append(current_node.val)
                current_node = current_node.right
            else:
                pre_node = current_node.left
                while pre_node.right and pre_node.right != current_node:
                    pre_node = pre_node.right
                if not pre_node.right:
                    pre_node.right = current_node
                    current_node = current_node.left
                else:
                    pre_node.right = None
                    res.append(current_node.val)
                    current_node = current_node.right
        return res

    def ___inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        nodes = []

        while root or nodes:
            if not root:
                root = nodes.pop()
                res.append(root.val)
                root = root.right
            else:
                nodes.append(root)
                root = root.left
        return res

    def ____inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        nodes = []

        while root or nodes:
            while root:
                nodes.append(root)
                root = root.left
            root = nodes.pop()
            res.append(root.val)
            root = root.right
        return res


    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        nodes = []

        while root or nodes:
            if not root:
                root = nodes.pop()
                res.append(root.val)
                root = root.right
            else:
                if root.left:
                    nodes.append(root)
                    root = root.left
                else:
                    res.append(root.val)
                    root = root.right
        return res


# if __name__ == "__main__":
#     s = Solution()
#     head = TreeNode(1)
#     head.left = TreeNode(5)
#     head.left.left = TreeNode(1)
#     head.left.right = TreeNode(2)
#     head.right = TreeNode(4)
#     head.right.left = TreeNode(1)
#     print s.inorderTraversal(head)
#     print s._inorderTraversal(head)
