# coding=utf-8
#
# @lc app=leetcode id=33 lang=python
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (32.65%)
# Likes:    2445
# Dislikes: 314
# Total Accepted:    421.1K
# Total Submissions: 1.3M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# 
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# Example 1:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# 
#


class Solution(object):
    def _search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return nums.index(target) if target in nums else -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # O(logN) 就是二分
        # 先二分找到 旋转点
        # 再左右二分找到定位点
        # 两次二分，时间复杂度还是二分
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start+end) / 2
            if nums[mid] > nums[start]:
                if nums[mid] < nums[end]:
                    break
                start = mid
            else:
                end = mid

        # gap = end
        gap = self.gap(nums, target)

        if nums[0] <= target <= nums[gap]:
            start = 0
            end = gap
        else:
            start = gap + 1
            end = len(nums) - 1

        while start <= end:
            mid = (start+end) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    def gap(self, nums, v):
        if len(nums) < 3:
            return 0
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] >= nums[start]:
                if mid+1 >= len(nums) or nums[mid-1] <= nums[mid] >= nums[mid+1]:
                    return mid
                start = mid + 1
            elif nums[mid] < nums[start]:
                if mid-1 < 0 or nums[mid-1] >= nums[mid] <= nums[mid+1]:
                    return mid - 1
                end = mid - 1


# if __name__ == '__main__':
#     s = Solution()
#     print s.search([1], 0)
#     print s.search([], 1)
#     print s.search([1,3],0)
#     print s.search([1,3,5], 0)
#     print s.search([4,5,6,7,0,1,2,3], 0)
#     print s.search([4,5,6,7,0,1,2,3], 3)
#     print s.search([5,6,7,0,1,2,4], 3)
#     # print s.gap([4,5,6,7,0,1,2,3], 0)
#     # print s.gap([4,5,6,7,0,1,2,3], 3)
#     # print s.gap([5,6,7,0,1,2,4], 3)
