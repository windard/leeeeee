# coding=utf-8
#
# @lc app=leetcode id=530 lang=python
#
# [530] Minimum Absolute Difference in BST
#
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (49.81%)
# Likes:    527
# Dislikes: 35
# Total Accepted:    60K
# Total Submissions: 118.6K
# Testcase Example:  '[1,null,3,2]'
#
# Given a binary search tree with non-negative values, find the minimum
# absolute difference between values of any two nodes.
# 
# Example:
# 
# 
# Input:
# 
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   /
# ⁠  2
# 
# Output:
# 1
# 
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1
# (or between 2 and 3).
# 
# 
# 
# 
# Note: There are at least two nodes in this BST.
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def _getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.min_num = float('inf')
        self.find_min_num_between(root, [])
        return self.min_num
    
    def find_min_num_between(self, root, values):
        if not root:
            return
        for value in values:
            self.min_num = min(self.min_num, abs(root.val - value))
        values.append(root.val)
        self.find_min_num_between(root.left, values)
        self.find_min_num_between(root.right, values)

    def __getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # inorder traversal
        nodes = self.inorderTraversal(root)
        min_diff = float("inf")
        for i in range(len(nodes)-1):
            if nodes[i+1] - nodes[i] < min_diff:
                min_diff = nodes[i+1] - nodes[i]
        return min_diff
    
    def inorderTraversal(self, root):
        result = []
        if not root:
            return result
        result.extend(self.inorderTraversal(root.left))
        result.extend([root.val])
        result.extend(self.inorderTraversal(root.right))
        return result

    def ___getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Wrong Answer
        # 虽然不会有 [1,null,5,null,3]
        # 但是 [236,104,701,null,227,null,911] 还是会有问题
        if not root:
            return float("inf")
        result = []
        if root.left:
            result.append(root.val - root.left.val)
        if root.right:
            result.append(root.right.val - root.val)
        result.append(self.getMinimumDifference(root.left))
        result.append(self.getMinimumDifference(root.right))

        return min(result)

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = []
        res = []
        last = -float("inf")
        min_diff = float("inf")

        while root or nodes:
            if root:
                nodes.append(root)
                root = root.left
            else:
                root = nodes.pop()
                if root.val - last < min_diff:
                    min_diff = root.val - last
                last = root.val
                root = root.right

        return min_diff

# if __name__ == "__main__":
#     s = Solution()
#     head = TreeNode(1)
#     head.left = TreeNode(2)
#     head.right = TreeNode(5)
#     head.right.left = TreeNode(3)
#     print s.getMinimumDifference(head)

#     head = TreeNode(1)
#     head.right = TreeNode(3)
#     head.right.left = TreeNode(2)
#     print s.getMinimumDifference(head)
