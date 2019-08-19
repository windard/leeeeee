# coding=utf-8
#
# @lc app=leetcode id=674 lang=python
#
# [674] Longest Continuous Increasing Subsequence
#
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
#
# algorithms
# Easy (44.67%)
# Likes:    476
# Dislikes: 98
# Total Accepted:    73.9K
# Total Submissions: 165.4K
# Testcase Example:  '[1,3,5,4,7]'
#
# 
# Given an unsorted array of integers, find the length of longest continuous
# increasing subsequence (subarray).
# 
# 
# Example 1:
# 
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its
# length is 3. 
# Even though [1,3,5,7] is also an increasing subsequence, it's not a
# continuous one where 5 and 7 are separated by 4. 
# 
# 
# 
# Example 2:
# 
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length
# is 1. 
# 
# 
# 
# Note:
# Length of the array will not exceed 10,000.
# 
#


class Solution(object):
    def _findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_length = 1
        index = 0
        last = None
        length = 1
        while index < len(nums):
            if last != None:
                if nums[index] > last:
                    length += 1
                else:
                    length = 1
                max_length = max(max_length, length)
            last = nums[index]
            index += 1     
        return max_length           

    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 滑动窗口
        max_index = index = 0
        for i in range(len(nums)):
            if i and nums[i] <= nums[i-1]:
                index = i
            max_index = max(max_index, i - index + 1)
        return max_index


# if __name__ == "__main__":
#     s = Solution()
#     print s.findLengthOfLCIS([1,3,5,4,7])
#     print s.findLengthOfLCIS([1,0,0,8,6])
