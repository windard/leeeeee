# coding=utf-8
#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (51.54%)
# Total Accepted:    366.9K
# Total Submissions: 704.3K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always
# exist in the array.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: 3
# 
# Example 2:
# 
# 
# Input: [2,2,1,1,1,2,2]
# Output: 2
# 
# 
#

from collections import Counter


class Solution(object):
    def _majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return Counter(nums).most_common()[0][0]

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Boyer-Moore
        # 和众数相等加一
        # 和众数不等减一
        # 为零的时候再取新值
        count = 0
        majority = 0
        for num in nums:
            if not count:
                majority = num
                count += 1
            elif num == majority:
                count += 1
            else:
                count -= 1
        return majority


# if __name__ == '__main__':
#     s = Solution()
#     print s.majorityElement([3,3,4])
