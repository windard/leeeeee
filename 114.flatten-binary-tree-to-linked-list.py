# coding=utf-8
#
# @lc app=leetcode id=114 lang=python
#
# [114] Flatten Binary Tree to Linked List
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (43.58%)
# Likes:    1689
# Dislikes: 217
# Total Accepted:    256.6K
# Total Submissions: 587.3K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# Given a binary tree, flatten it to a linked list in-place.
# 
# For example, given the following tree:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
# 
# 
# The flattened tree should look like:
# 
# 
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
# 
# 
#
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return '{} << {} >> {}'.format(self.left, self.val, self.right)


class Solution(object):
    def _flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 需要 O(n) 的空间复杂度
        if not root:
            return
        # 中序遍历，节点往右
        tree = root
        link = TreeNode(1)
        start = link
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
                if root:
                    link.right = TreeNode(root.val)
                    link = link.right
            else:
                root = stack.pop()
                root = root.right
                if root:
                    link.right = TreeNode(root.val)
                    link = link.right
        tree.left = None
        tree.right = start.right
        return tree

    def __flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 不完全的后序遍历，右左中
        self.link = None

        def postorder(node):
            if not node:
                return
            postorder(node.right)
            postorder(node.left)

            node.right = self.link
            self.link = node
            self.link.left = None
        postorder(root)
        return root

    def ___flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 这可以是一道遍历题
        # 也可以不是一道遍历题
        # 只需要将每一个节点的右子树，拼到左子树的最右边即可
        # 递归来拼

        def move_right(node):
            if not node:
                return
            # 先左后右，或者先右后左，都不影响
            move_right(node.right)
            move_right(node.left)
            left = node.left
            if not left:
                return
            while left.right:
                left = left.right

            left.right = node.right
            node.right = node.left
            node.left = None
        move_right(root)

    def ____flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 这可以是一道遍历题
        # 也可以不是一道遍历题
        # 只需要将每一个节点的右子树，拼到左子树的最右边即可
        # 循环来拼
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if root.left:
                    left = root.left
                    while left.right:
                        left = left.right
                    left.right = root.right
                    root.right = root.left
                    root.left = None

                root = root.right

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 这可以是一道遍历题
        # 也可以不是一道遍历题
        # 只需要将每一个节点的右子树，拼到左子树的最右边即可
        # 其实连栈都不需要
        while root:
            if root.left:
                left = root.left
                while left.right:
                    left = left.right

                left.right = root.right
                root.right = root.left
                root.left = None

            else:
                root = root.right


# if __name__ == '__main__':
#     s = Solution()
#     head = TreeNode(1)
#     head.left = TreeNode(2)
#     head.right = TreeNode(5)
#     head.left.left = TreeNode(3)
#     head.left.right = TreeNode(4)
#     head.right.right = TreeNode(6)
#     print head
#     s.flatten(head)
#     print head
