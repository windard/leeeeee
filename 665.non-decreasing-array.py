# coding=utf-8
#
# @lc app=leetcode id=665 lang=python
#
# [665] Non-decreasing Array
#
# https://leetcode.com/problems/non-decreasing-array/description/
#
# algorithms
# Easy (19.52%)
# Likes:    1160
# Dislikes: 254
# Total Accepted:    59.5K
# Total Submissions: 305.9K
# Testcase Example:  '[4,2,3]'
#
# 
# Given an array with n integers, your task is to check if it could become
# non-decreasing by modifying at most 1 element.
# 
# 
# 
# We define an array is non-decreasing if array[i]  holds for every i (1 
# 
# Example 1:
# 
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing
# array.
# 
# 
# 
# Example 2:
# 
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one
# element.
# 
# 
# 
# Note:
# The n belongs to [1, 10,000].
# 
#


class Solution(object):
    def _checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Wrong Answer
        if len(nums) < 2:
            return True
        one_chance = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if not one_chance:
                    one_chance = True
                else:
                    return False
        return True

    def __checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 改掉一个元素后，数组依次递增
        # Wrong Answer
        if len(nums) < 2:
            return True
        last = nums[0]
        index = 1
        one_chance = False
        while index < len(nums):
            if nums[index] < last:
                if not one_chance:
                    one_chance = True
                    last = min(nums[index], last)
                else:
                    return False
            else:
                last = nums[index]
            index += 1
        return True

    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True
        last = nums[0]
        index = 1
        one_chance = False
        while index < len(nums):
            if nums[index] < last:
                if not one_chance:
                    one_chance = True
                    if index > 1:
                        if min(nums[index], last) > nums[index-2]:
                            last = min(nums[index], last)
                    else:
                        last = min(nums[index], last)
                else:
                    return False
            else:
                last = nums[index]
            index += 1
        return True


# if __name__ == "__main__":
#     s = Solution()
#     print s.checkPossibility([4, 2, 3])
#     print s.checkPossibility([4, 2, 1])
#     print s.checkPossibility([3, 4, 2, 3])
#     print s.checkPossibility([-1, 4, 2, 3])     # True
#     print s.checkPossibility([1, 5, 9, 3, 14])  # True
#     print s.checkPossibility([1, 5, 9, 3, 8])   # False
