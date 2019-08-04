# coding=utf-8
#
# @lc app=leetcode id=145 lang=python
#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (46.93%)
# Total Accepted:    241.5K
# Total Submissions: 511.3K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the postorder traversal of its nodes' values.
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
# Output: [3,2,1]
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
    def _postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 后序遍历
        # 左右中

        res = []
        if root:
            res.extend(self.postorderTraversal(root.left))
            res.extend(self.postorderTraversal(root.right))
            res.append(root.val)

        return res

    def __postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 前序遍历的变种 中右左
        # 然后逆序
        nodes = [root]
        res = []
        while nodes:
            root = nodes.pop()
            if root:
                res.append(root.val)
                nodes.append(root.left)
                nodes.append(root.right)
        return res[::-1]

    def ___postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Morris Traversal
        # revered insert
        res = []
        current_node = pre_node = root
        while current_node:
            if not current_node.right:
                res.insert(0, current_node.val)
                current_node = current_node.left
            else:
                pre_node = current_node.right
                while pre_node.left and pre_node.left != current_node:
                    pre_node = pre_node.left
                if pre_node.left == current_node:
                    pre_node.left = None
                    current_node = current_node.left
                else:
                    res.insert(0, current_node.val)
                    pre_node.left = current_node
                    current_node = current_node.right
        return res

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodes = [root]
        res = []
        touched = set()

        while nodes:
            root = nodes.pop()
            if root:
                if root in touched:
                    res.append(root.val)
                else:
                    touched.add(root)
                    nodes.append(root)
                    nodes.append(root.right)
                    nodes.append(root.left)
        return res

# if __name__ == "__main__":
#     s = Solution()
#     head = TreeNode(3)
#     head.left = TreeNode(1)
#     head.right = TreeNode(2)
#     print s.postorderTraversal(head)
