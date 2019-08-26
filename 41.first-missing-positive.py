# coding=utf-8
#
# @lc app=leetcode id=41 lang=python
#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (29.46%)
# Likes:    1957
# Dislikes: 625
# Total Accepted:    234.9K
# Total Submissions: 795.2K
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array, find the smallest missing positive integer.
# 
# Example 1:
# 
# 
# Input: [1,2,0]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: [3,4,-1,1]
# Output: 2
# 
# 
# Example 3:
# 
# 
# Input: [7,8,9,11,12]
# Output: 1
# 
# 
# Note:
# 
# Your algorithm should run in O(n) time and uses constant extra space.
# 
#


class Solution(object):
    def _firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # MemoryError
        # [2147483647]
        if not nums:
            return 1

        zeros = [0] * (max(nums)+2)
        for num in nums:
            if num > 0:
                zeros[num] = 1
        for i in range(1, len(zeros)):
            if zeros[i] != 1:
                return i

    def __firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        for i in range(1, len(nums)+2):
            if i not in nums:
                return i

    def ___firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zeros = [0] * (len(nums)+2)
        for num in nums:
            if num < 0 or num > len(nums):
                continue
            zeros[num] = 1
        for i in range(1, len(zeros)):
            if zeros[i] != 1:
                return i

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1

        for i in nums:
            if i == 1:
                break
        else:
            return 1

        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 1

        for i in range(len(nums)):
            nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])

        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return i+2


# if __name__ == '__main__':
#     s = Solution()
#     print s.firstMissingPositive([])
#     print s.firstMissingPositive([0])
#     print s.firstMissingPositive([1])
#     print s.firstMissingPositive([5])
#     print s.firstMissingPositive([1,2,0])
#     print s.firstMissingPositive([3,4,-1,1])
#     print s.firstMissingPositive([7,8,9,11,12])
