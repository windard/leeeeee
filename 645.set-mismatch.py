#
# @lc app=leetcode id=645 lang=python
#
# [645] Set Mismatch
#
# https://leetcode.com/problems/set-mismatch/description/
#
# algorithms
# Easy (40.42%)
# Likes:    442
# Dislikes: 243
# Total Accepted:    52.1K
# Total Submissions: 127K
# Testcase Example:  '[1,2,2,4]'
#
# 
# The set S originally contains numbers from 1 to n. But unfortunately, due to
# the data error, one of the numbers in the set got duplicated to another
# number in the set, which results in repetition of one number and loss of
# another number. 
# 
# 
# 
# Given an array nums representing the data status of this set after the error.
# Your task is to firstly find the number occurs twice and then find the number
# that is missing. Return them in the form of an array.
# 
# 
# 
# Example 1:
# 
# Input: nums = [1,2,2,4]
# Output: [2,3]
# 
# 
# 
# Note:
# 
# The given array size will in the range [2, 10000].
# The given array's numbers won't have any order.
# 
# 
#


class Solution(object):
    def _findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Accept But
        # Too Slow
        d = {}
        for n in nums:
            v = d.get(n)
            if not v:
                d[n] = 1
            else:
                d = n
                break

        l = sum(range(len(nums)+1)) - sum(nums) + d
        return [d, l]

    def __findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Set
        total = sum(range(len(nums)+1))
        l = total - sum(set(nums))
        d = sum(nums) + l - total
        return [d, l]

    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # BitMap
        bitmap = [0] * 10001
        for n in nums:
            if not bitmap[n]:
                bitmap[n] = 1
            else:
                d = n
                break
        l = sum(range(len(nums)+1)) - sum(nums) + d
        return [d, l]
