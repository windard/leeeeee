# coding=utf-8
#
# @lc app=leetcode id=300 lang=python
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (41.21%)
# Likes:    2905
# Dislikes: 68
# Total Accepted:    254.6K
# Total Submissions: 615.9K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
# 
# Example:
# 
# 
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4. 
# 
# Note: 
# 
# 
# There may be more than one LIS combination, it is only necessary for you to
# return the length.
# Your algorithm should run in O(n^2) complexity.
# 
# 
# Follow up: Could you improve it to O(n log n) time complexity?
# 
#


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划，可以达到 n^2 的时间复杂度
        counts = [0] * len(nums)
        for index, num in enumerate(nums):
            max_count = 0
            for j in range(index):
                if nums[j] < num:
                    max_count = max(max_count, counts[j])
            counts[index] = max_count + 1
        return max(counts) if counts else 0

#
# if __name__ == '__main__':
#     s = Solution()
#     print s.lengthOfLIS([4,4,4,4])
#     print s.lengthOfLIS([10,9,2,5,3,7,101,18])
