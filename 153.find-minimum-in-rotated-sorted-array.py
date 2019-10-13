# coding=utf-8
#
# @lc app=leetcode id=153 lang=python
#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (43.39%)
# Likes:    1169
# Dislikes: 173
# Total Accepted:    313.5K
# Total Submissions: 721.2K
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.
# 
# Example 1:
# 
# 
# Input: [3,4,5,1,2] 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,5,6,7,0,1,2]
# Output: 0
# 
# 
#


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        gap = self.gap(nums)
        return min(nums[(gap+1) % len(nums)], nums[0])

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


# if __name__ == '__main__':
#     s = Solution()
#     print s.findMin([3,4,5,1,2])
#     print s.findMin([4,5,6,7,0,1,2])
