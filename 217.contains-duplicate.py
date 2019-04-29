#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (50.84%)
# Total Accepted:    322.5K
# Total Submissions: 626.1K
# Testcase Example:  '[1,2,3,1]'
#
# Given an array of integers, find if the array contains any duplicates.
# 
# Your function should return true if any value appears at least twice in the
# array, and it should return false if every element is distinct.
# 
# Example 1:
# 
# 
# Input: [1,2,3,1]
# Output: true
# 
# Example 2:
# 
# 
# Input: [1,2,3,4]
# Output: false
# 
# Example 3:
# 
# 
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true
# 
#
class Solution(object):
    def __containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)

    def _containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Time Limited
        return any(map(lambda i:nums.count(i) > 1, list(nums)))

    def ___containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Time Limited
        n = []
        for i in nums:
            if i in n:
                return True
            else:
                n.append(i)
        return False

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False
