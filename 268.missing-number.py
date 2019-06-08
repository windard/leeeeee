#
# @lc app=leetcode id=268 lang=python
#
# [268] Missing Number
#
# https://leetcode.com/problems/missing-number/description/
#
# algorithms
# Easy (47.56%)
# Likes:    855
# Dislikes: 1291
# Total Accepted:    268.6K
# Total Submissions: 557.8K
# Testcase Example:  '[3,0,1]'
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
# the one that is missing from the array.
# 
# Example 1:
# 
# 
# Input: [3,0,1]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# 
# 
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant extra space complexity?
#
class Solution(object):
    def _missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        for i in range(len(nums)+1):
            if i not in nums:
                return i

    def __missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        nums.append(0)
        for i in range(len(nums)):
            if nums[i] != i:
                return i

    def ___missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 求和
        total = sum(range(len(nums)+1))
        return total - sum(nums)

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 异或
        res = len(nums)
        for i in range(len(nums)):
            res ^= nums[i]
            res ^= i
        return res
