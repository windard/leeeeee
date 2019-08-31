# coding=utf-8
#
# @lc app=leetcode id=80 lang=python
#
# [80] Remove Duplicates from Sorted Array II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
#
# algorithms
# Medium (41.01%)
# Likes:    745
# Dislikes: 573
# Total Accepted:    215.9K
# Total Submissions: 524.7K
# Testcase Example:  '[1,1,1,2,2,3]'
#
# Given a sorted array nums, remove the duplicates in-place such that
# duplicates appeared at most twice and return the new length.
# 
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
# 
# Example 1:
# 
# 
# Given nums = [1,1,1,2,2,3],
# 
# Your function should return length = 5, with the first five elements of nums
# being 1, 1, 2, 2 and 3 respectively.
# 
# It doesn't matter what you leave beyond the returned length.
# 
# Example 2:
# 
# 
# Given nums = [0,0,1,1,1,1,2,3,3],
# 
# Your function should return length = 7, with the first seven elements of nums
# being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.
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
#


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        slow = 0
        fast = 1
        count = 0
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                if not count:
                    slow += 1
                    nums[slow] = nums[fast]
                    fast += 1
                    count = 2
                else:
                    fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
                count = 0

        return slow + 1


# if __name__ == '__main__':
#     s = Solution()
#     print s.removeDuplicates([0,1])
#     print s.removeDuplicates([0,0])
#     print s.removeDuplicates([0,0,0,1])
#     print s.removeDuplicates([0,0,0])
#     print s.removeDuplicates([1,1,1,2,2,3])
#     print s.removeDuplicates([0,0,1,1,1,1,2,3,3])
