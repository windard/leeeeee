# coding=utf-8
#
# @lc app=leetcode id=540 lang=python
#
# [540] Single Element in a Sorted Array
#
# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
#
# algorithms
# Medium (57.46%)
# Likes:    836
# Dislikes: 64
# Total Accepted:    62.4K
# Total Submissions: 108.7K
# Testcase Example:  '[1,1,2,3,3,4,4,8,8]'
#
# Given a sorted array consisting of only integers where every element appears
# exactly twice except for one element which appears exactly once. Find this
# single element that appears only once.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [3,3,7,7,10,11,11]
# Output: 10
# 
# 
# 
# 
# Note: Your solution should run in O(log n) time and O(1) space.
# 
#


class Solution(object):
    def _singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 规律找错
        # 无明显联系
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            if nums[mid-1] != nums[mid] != nums[mid+1]:
                return nums[mid]
            elif nums[mid-1] == nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return nums[0]
        start = 0
        end = len(nums) - 1
        while start <= end:
            if start == end:
                return nums[start]
            mid = (start + end) / 2
            if nums[mid-1] != nums[mid] != nums[mid+1]:
                return nums[mid]
            elif (mid % 2 and nums[mid] == nums[mid-1]) or (not mid % 2 and nums[mid] == nums[mid+1]):
                start = mid + 1
            else:
                end = mid - 1


# if __name__ == '__main__':
#     s = Solution()
#     print s.singleNonDuplicate([1,1,2])
#     print s.singleNonDuplicate([1,1,2,3,3,4,4,8,8])
#     print s.singleNonDuplicate([3,3,7,7,10,11,11])
