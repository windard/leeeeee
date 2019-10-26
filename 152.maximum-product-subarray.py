# coding=utf-8
#
# @lc app=leetcode id=152 lang=python
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (29.78%)
# Likes:    2408
# Dislikes: 111
# Total Accepted:    234.2K
# Total Submissions: 784.2K
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
# 
# Example 1:
# 
# 
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# 
# 
# Example 2:
# 
# 
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
#


class Solution(object):
    def _maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n^2)
        # Time Limit
        max_mul = -float("inf")
        for i in range(len(nums)):
            mul = 1
            for j in range(i, len(nums)):
                mul *= nums[j]
                max_mul = max(max_mul, mul)
        return max_mul

    def __maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划
        # 保持最大值一行
        # 保持最小值一行
        if not nums:
            return
        max_num = [0 for _ in range(len(nums))]
        min_num = [0 for _ in range(len(nums))]
        max_val = -float("inf")
        for key, num in enumerate(nums):
            if not key:
                max_num[key] = num
                min_num[key] = num
            else:
                max_num[key] = max(num, num * max_num[key-1], num * min_num[key-1])
                min_num[key] = min(num, num * max_num[key-1], num * min_num[key-1])
            max_val = max(max_num[key], max_val)
        return max_val

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 还有一个 O(n) 的解法
        # 计算总共有负数的个数
        from operator import mul
        mul_add = reduce(mul, nums)
        if mul_add > 0:
            return mul_add
        # 算了，不行，还用考虑以零分界
