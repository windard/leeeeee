# coding=utf-8
#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
#
# algorithms
# Easy (39.35%)
# Total Accepted:    512.3K
# Total Submissions: 1.3M
# Testcase Example:  '[1,1,2]'
#
# Given a sorted array nums, remove the duplicates in-place such that each
# element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
#
# Example 1:
#
#
# Given nums = [1,1,2],
#
# Your function should return length = 2, with the first two elements of nums
# being 1 and 2 respectively.
#
# It doesn't matter what you leave beyond the returned length.
#
# Example 2:
#
#
# Given nums = [0,0,1,1,1,2,2,3,3,4],
#
# Your function should return length = 5, with the first five elements of nums
# being modified to 0, 1, 2, 3, and 4 respectively.
#
# It doesn't matter what values are set beyond the returned length.
#
#
# Clarification:
#
# Confused why the returned value is an integer but your answer is an array?
#
# Note that the input array is passed in by reference, which means modification
# to the input array will be known to the caller as well.
#
# Internally you can think of this:
#
#
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeDuplicates(nums);
#
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len
# elements.
# for (int i = 0; i < len; i++) {
# print(nums[i]);
# }
#
#


class Solution(object):
    def _removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        star = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[star]:
                star += 1
                nums[star] = nums[i]
        return star + 1

    def __removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 快慢指针 +
        # 定位指针
        # Total Wrong
        # I don't know how to solve
        if not nums:
            return 0
        if len(nums) < 2:
            return 1
        lower = index = 0
        fast = 1
        while fast < len(nums):
            if nums[fast] != nums[lower]:
                nums[index] = nums[lower]
                index += 1
                lower = fast
                fast += 1
            else:
                fast += 1
        if fast - lower == 1:
            nums[index] = nums[lower]
            index += 1
        return index

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 快慢指针
        if len(nums) < 2:
            return len(nums)
        lower = 0
        fast = 1
        while fast < len(nums):
            if nums[fast] != nums[lower]:
                lower += 1
                nums[lower] = nums[fast]
            fast += 1
        return lower + 1


# if __name__ == '__main__':
#     s = Solution()
#     print s.removeDuplicates([0,0])
#     print s.removeDuplicates([0,1])
#     print s.removeDuplicates([0,1,1])
#     print s.removeDuplicates([0,0,1,1])
#     print s.removeDuplicates([0,0,1,1,1])
#     print s.removeDuplicates([1,2,3,4,5])

