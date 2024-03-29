# coding=utf-8
#
# @lc app=leetcode id=102 lang=python
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (47.06%)
# Total Accepted:    345.5K
# Total Submissions: 729.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
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

    def ___levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 迭代
        # 列表就是队列也是栈
        q = []
        res = []
        if root:
            q.append(root)
        while q:
            lower = []
            i = len(q)
            while i:
                r = q.pop(0)
                lower.append(r.val)
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
                i -= 1
            res.append(lower)
        return res

    def __levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 迭代
        # 队列先进先出
        import Queue
        q = Queue.Queue()
        res = []
        if root:
            q.put(root)
        while q.qsize():
            lower = []
            i = q.qsize()
            while i:
                r = q.get()
                lower.append(r.val)
                if r.left:
                    q.put(r.left)
                if r.right:
                    q.put(r.right)
                i -= 1
            res.append(lower)
        return res

    def _levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 递归
        return self.mining(root, 0, [])

    def mining(self, root, index, res):
        if root:
            if len(res) < index + 1:
                res.append([])
            res[index].append(root.val)
            if root.left:
                res = self.mining(root.left, index+1, res)
            if root.right:
                res = self.mining(root.right, index+1, res)
        return res

    def ____levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 层次遍历的两种写法
        # 队列
        # 是错误的 [3,9,20,15,7]
        # 正确答案 [[3],[9,20],[15,7]]
        queue = [root]
        result = []
        while queue:
            root = queue.pop(0)
            result.append(root.val)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        return result

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = [[root]]
        result = []
        while stack:
            level = stack.pop()
            current = []
            next_level = []
            for root in level:
                current.append(root.val)
                if root.left:
                    next_level.append(root.left)
                if root.right:
                    next_level.append(root.right)
            result.append(current)
            if next_level:
                stack.append(next_level)
        return result

# if __name__ == "__main__":
#     t = TreeNode(3)
#     t.left = TreeNode(9)
#     t.right = TreeNode(20)
#     t.right.left = TreeNode(15)
#     t.right.right = TreeNode(7)
#     s = Solution()
#     print s.levelOrder(t)
