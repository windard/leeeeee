# coding=utf-8
#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (42.82%)
# Total Accepted:    470.1K
# Total Submissions: 1.1M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# Example:
# 
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = -float("inf")
        count = 0
        for n in nums:
            count = max(n, count + n)
            max_count = max(count, max_count)
        return max_count

    def _maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        last = nums[0]
        maxn = last
        for i in nums[1:]:
            if last + i < i:
                last = i
            else:
                last = last + i
            maxn = maxn if maxn > last else last
        return maxn

    def __maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # greedy algorithm
        if not nums:
            return

        count = 0
        max_count = -float("inf")
        for n in nums:
            if n + count < n:
                count = n
            else:
                count += n
            max_count = max(max_count, count)
        return max_count

    def maxSubArray(self, A):
        max_sum = -float("inf")
        this_sum = 0
        for x in A:
            this_sum += x
            if this_sum > max_sum:
                max_sum = this_sum
            if this_sum < 0:
                this_sum = 0
        return max_sum


# if __name__ == '__main__':
#     s = Solution()
#     print s.maxSubArray([-2,1])
#     print s.maxSubArray([7, -5, 3, 5])
#     print s.maxSubArray([-2, 11, -4, 13, -5, -2])
#     print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
