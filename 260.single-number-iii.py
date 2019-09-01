# coding=utf-8
#
# @lc app=leetcode id=260 lang=python
#
# [260] Single Number III
#
# https://leetcode.com/problems/single-number-iii/description/
#
# algorithms
# Medium (57.80%)
# Likes:    970
# Dislikes: 80
# Total Accepted:    114.1K
# Total Submissions: 196.7K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# Given an array of numbers nums, in which exactly two elements appear only
# once and all the other elements appear exactly twice. Find the two elements
# that appear only once.
# 
# Example:
# 
# 
# Input:  [1,2,1,3,2,5]
# Output: [3,5]
# 
# Note:
# 
# 
# The order of the result is not important. So in the above example, [5, 3] is
# also correct.
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant space complexity?
# 
#


class Solution(object):
    def _singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        two = reduce(lambda x, y: x ^ y, nums)
        diff = two & (~two + 1)
        result = [0,0]
        for num in nums:
            if not num & diff:
                result[0] ^= num
            else:
                result[1] ^= num
        return result

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        data = set()
        for num in nums:
            if num not in data:
                data.add(num)
            else:
                data.remove(num)
        return data
