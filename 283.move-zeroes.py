#
# @lc app=leetcode id=283 lang=python
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (53.64%)
# Likes:    2040
# Dislikes: 74
# Total Accepted:    470.2K
# Total Submissions: 864.6K
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# 
# Example:
# 
# 
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# 
# Note:
# 
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# 
#
class Solution(object):
    def _moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = 0
        index = 0
        length_nums = len(nums)
        while index < length_nums:
            if nums[index] == 0:
                # faster
                # nums.pop(index)
                # solwer
                nums.remove(0)
                length_nums -= 1
                length += 1
            else:
                index += 1
        for _ in range(length):
            nums.append(0)

    def __moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 一边加一边减
        # 永远不会结束
        index = 0
        while index < len(nums):
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
            else:
                index += 1

    def ___moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for _ in nums:
            try:
                nums.remove(0)
                nums.append(0)
            except:
                break

    def ____moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Copy One
        nums.sort(key=bool, reverse=True)

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 双指针
        index = 0
        count = 0
        while index < len(nums):
            if nums[index] != 0:
                nums[count] = nums[index]
                index += 1
                count += 1
            else:
                index += 1
        for i in range(count, index):
            nums[i] = 0
