# coding=utf-8
#
# @lc app=leetcode id=81 lang=python
#
# [81] Search in Rotated Sorted Array II
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (32.74%)
# Likes:    768
# Dislikes: 345
# Total Accepted:    185.5K
# Total Submissions: 566.3K
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
# 
# You are given a target value to search. If found in the array return true,
# otherwise return false.
# 
# Example 1:
# 
# 
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
# 
# Follow up:
# 
# 
# This is a follow up problem to Search in Rotated Sorted Array, where nums may
# contain duplicates.
# Would this affect the run-time complexity? How and why?
# 
# 
#


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        return target in nums

    def gap(self, nums):
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


    def __search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # 如果遇到特殊情况
        # 就按线性处理 O(n)
        # 否则就两边都要处理 O(logn)
        # Same with @154
        if not nums:
            return False

        gap = self.gap(nums)

        if nums[0] <= target <= nums[gap]:
            start = 0
            end = gap
        else:
            start = gap + 1
            end = len(nums) - 1

        while start <= end:
            mid = (start+end) / 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False


# if __name__ == '__main__':
#     s = Solution()
#     print s.search([1,3,1,1,1], 3)
#     print s.search([2,2,2,0,1], 0)
#     print s.search([2,5,6,0,0,1,2], 0)
#     print s.search([2,5,6,0,0,1,2], 3)
#     print s.search([4,5,6,7,0,1,2,3], 0)
#     print s.search([4,5,6,6,7,0,1,2,3], 0)
#     print s.search([4,5,6,7,0,1,1,2,3], 0)
#     print s.search([4,4,4,5,6,7,0,1,2,3], 3)
#     print s.search([5,6,7,0,1,1,1,2,4], 3)
