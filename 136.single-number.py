# coding=utf-8
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

from functools import reduce


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 数组中只出现一次的数字
        return reduce(lambda x, y: x ^ y, nums)

    def _singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Miss [1]
        while 1:
            for key, value in enumerate(nums):
                if key == 0:
                    continue
                if value == nums[0]:
                    nums.pop(key)
                    nums.pop(0)
                    break
            else:
                return nums[0]

    def isAllSingleNumber(self, nums):
        # 数组中是否都只出现一次
        # newcoder CD103
        return len(nums) == len(set(nums))
        # 使用 bitmap
        # 但是 42亿 的数字，就需要 500M 大小，😂
        # 正解应该是使用 堆排序


if __name__ == '__main__':
    s = Solution()
    print(s.isAllSingleNumber([1, 2, 3]))
    print(s.isAllSingleNumber([1, 2, 1]))
