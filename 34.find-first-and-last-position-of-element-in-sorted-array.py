# coding=utf-8
#
# @lc app=leetcode id=34 lang=python
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (32.99%)
# Likes:    1590
# Dislikes: 87
# Total Accepted:    305.4K
# Total Submissions: 908.2K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# Example 1:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# 
# Example 2:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# 
#


class Solution(object):
    def _searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # O(n)
        start = end = -1

        for index, value in enumerate(nums):
            if target == value:
                if start == -1:
                    start = index
            else:
                if start != -1:
                    end = index - 1
                    return start, end
        
        if start != -1:
            end = index
        return start, end

    def __searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.midSearch(nums, target, True)
        if left < 0:
            return -1, -1
        start = end = left
        for i in range(left, -1, -1):
            if nums[i] == target:
                start = i
            else:
                break
        
        for i in range(left, len(nums)):
            if nums[i] == target:
                end = i
            else:
                break
        return start, end

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = right = -1
        # 先查左边
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                if mid and nums[mid-1] == target:
                    end = mid - 1
                else:
                    left = mid
                    break
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        # 再查右边
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                if mid < len(nums) - 1 and nums[mid+1] == target:
                    start = mid + 1
                else:
                    right = mid
                    break
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return left, right


    def binary_search(self, nums, target):
        # 传统写法，二分查找
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def midSearch(self, nums, target, flag=True):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1


# if __name__ == "__main__":
#     s = Solution()
#     print s.searchRange([2, 2], 3)
#     print s.searchRange([1], 1)
#     print s.searchRange([1,1], 1)
#     print s.searchRange([5,7,7,8,8,10], 6)
#     print s.searchRange([5,7,7,8,8,10], 10)
#     print s.searchRange([5,7,7,8,8,10,10], 10)
#     print s.searchRange([5,7,7,8,10], 8)
#     print s.searchRange([8,8,10], 8)
#     print s.searchRange([8,10], 8)
#
#     print s.midSearch([2, 2], 3)
#     print s.midSearch([],1)
#     print s.midSearch([1,2,3,4,5], 3)
#     print s.midSearch([1,2,3,4,5], 4)
#     print s.midSearch([1,2,3,5], 3)
#     print s.midSearch([1,2,4,5], 4)
#     print s.midSearch([1,2,3,5], 4)
#
#     print s.midSearch([1,2,3,3,3,4,5], 3)
#     print s.midSearch([1,2,3,3,3,4,5], 3, False)
#     print s.midSearch([1,2,3,4,4,5], 4)
#     print s.midSearch([1,2,3,4,4,5], 4, False)
