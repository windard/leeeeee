#
# @lc app=leetcode id=136 lang=python
#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (58.67%)
# Total Accepted:    414.7K
# Total Submissions: 704.1K
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
#
# Example 1:
#
#
# Input: [2,2,1]
# Output: 1
#
#
# Example 2:
#
#
# Input: [4,1,2,1,2]
# Output: 4
#
#
#
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x,y: x ^ y, nums)

    def _singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Miss [1]
        while 1:
            for key,value in enumerate(nums):
                if key == 0:
                    continue
                if value == nums[0]:
                    nums.pop(key)
                    nums.pop(0)
                    break
            else:
                return nums[0]


