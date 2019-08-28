# coding=utf-8
#
# @lc app=leetcode id=654 lang=python
#
# [654] Maximum Binary Tree
#
# https://leetcode.com/problems/maximum-binary-tree/description/
#
# algorithms
# Medium (76.80%)
# Likes:    1213
# Dislikes: 154
# Total Accepted:    94.6K
# Total Submissions: 123.1K
# Testcase Example:  '[3,2,1,6,0,5]'
#
# 
# Given an integer array with no duplicates. A maximum tree building on this
# array is defined as follow:
# 
# The root is the maximum number in the array. 
# The left subtree is the maximum tree constructed from left part subarray
# divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray
# divided by the maximum number. 
# 
# 
# 
# 
# Construct the maximum tree by the given array and output the root node of
# this tree.
# 
# 
# Example 1:
# 
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:
# 
# ⁠     6
# ⁠   /   \
# ⁠  3     5
# ⁠   \    / 
# ⁠    2  0   
# ⁠      \
# ⁠       1
# 
# 
# 
# Note:
# 
# The size of the given array will be in the range [1,1000].
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
        return '{} < {} > {}'.format(self.left, self.val, self.right)


class Solution(object):
    def _constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        max_num = max(nums)
        max_index = nums.index(max_num)
        root = TreeNode(max_num)
        root.left = self.constructMaximumBinaryTree(nums[:max_index])
        root.right = self.constructMaximumBinaryTree(nums[max_index+1:])
        return root

    def __constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # 构建一个单调递减栈
        # 我的是向左偏移，答案是向右偏移
        # Wrong Answer
        stack = []
        left = None
        root = None
        nums.append(float("inf"))
        for num in nums:
            while stack and stack[-1] < num:
                top = stack.pop()
                new_left = TreeNode(top)
                new_left.left = left
                left = new_left
                if not stack:
                    if not root:
                        root = left
                        left = None
                    else:
                        left.right = left.left
                        left.left = root
                        root = left
            stack.append(num)

        return root

    def ___constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # 单调栈
        # 根据题目要求
        # 最大值左边的是 left
        # 最大值右边的是 right
        # 最大值  是 root

        stack = []
        node = TreeNode(1)
        nums.append(float("inf"))
        top = None
        for num in nums:
            node = TreeNode(num)
            while stack and stack[-1].val < node.val:
                top = stack.pop()
            else:
                node.left = top
                top = None

            if stack:
                stack[-1].right = node
            stack.append(node)

        return node.left

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # copy one
        stack = []
        for num in nums:
            node = TreeNode(num)
            while stack and stack[-1].val < node.val:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack and stack[0]


# if __name__ == '__main__':
#     s = Solution()
#     print s.constructMaximumBinaryTree([3,2,1,6,0,5])
#     print s.constructMaximumBinaryTree([6,0,5,3,5,9])
