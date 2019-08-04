# coding=utf-8
#
# @lc app=leetcode id=144 lang=python
#
# [144] Binary Tree Preorder Traversal
#
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (50.28%)
# Total Accepted:    312.5K
# Total Submissions: 618.9K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the preorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,2,3]
# 
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

    def _preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 前序遍历
        # 中左右
        # 迭代
        # 迭代用栈保存根节点
        # DFS
        res = []
        if root:
            res.append(root.val)
            res.extend(self._preorderTraversal(root.left))
            res.extend(self._preorderTraversal(root.right))
        return res

    def __preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # BFS
        res = []
        nodes = [root]
        while nodes:
            node = nodes.pop()
            if node:
                res.append(node.val)
                nodes.append(node.right)
                nodes.append(node.left)

        return res

    def ___preorderTraversal(self, root):
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
                if pre_node.right == current_node:
                    pre_node.right = None
                    current_node = current_node.right
                else:
                    res.append(current_node.val)
                    pre_node.right = current_node
                    current_node = current_node.left
        return res

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # An Other Morris Traversal
        res = []
        current_node = pre_node = root
        while current_node:
            res.append(current_node.val)
            if not current_node.left:
                current_node = current_node.right
            else:
                pre_node = current_node.left
                while pre_node.right and pre_node.right != current_node:
                    pre_node = pre_node.right
                if pre_node.right == current_node:
                    res.pop()
                    pre_node.right = None
                    current_node = current_node.right
                else:
                    pre_node.right = current_node
                    current_node = current_node.left
        return res

# if __name__ == "__main__":
#     s = Solution()
#     head = TreeNode(1)
#     head.left = TreeNode(5)
#     head.left.left = TreeNode(1)
#     head.left.right = TreeNode(2)
#     head.right = TreeNode(4)
#     head.right.left = TreeNode(1)
#     print s._preorderTraversal(head)
#     print s.preorderTraversal(head)
