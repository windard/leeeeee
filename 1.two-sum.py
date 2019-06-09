#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (40.20%)
# Total Accepted:    1.4M
# Total Submissions: 3.5M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# Example:
#
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
#
#
#
#

import itertools

class Solution(object):
    def _twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,j in itertools.permutations(range(len(nums)), 2):
            if nums[i] + nums[j] == target:
                return [i, j]

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tm = {}
        for key, num in enumerate(nums):
            if target - num in tm:
                return [tm[target-num], key]
            else:
                tm[num] = key
