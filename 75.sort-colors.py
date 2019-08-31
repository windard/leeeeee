# coding=utf-8
#
# @lc app=leetcode id=75 lang=python
#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (41.10%)
# Total Accepted:    290.3K
# Total Submissions: 703.4K
# Testcase Example:  '[2,0,2,1,1,0]'
#
# Given an array with n objects colored red, white or blue, sort them in-place
# so that objects of the same color are adjacent, with the colors in the order
# red, white and blue.
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white,
# and blue respectively.
# 
# Note: You are not suppose to use the library's sort function for this
# problem.
# 
# Example:
# 
# 
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# 
# Follow up:
# 
# 
# A rather straight forward solution is a two-pass algorithm using counting
# sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
# array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?
# 
# 
#


class Solution(object):
    def _sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red = white = blue = 0
        for num in nums:
            if num == 0:
                red += 1
            elif num == 1:
                white += 1
            else:
                blue += 1

        for i in range(len(nums)):
            if red:
                red -= 1
                nums[i] = 0
            elif white:
                white -= 1
                nums[i] = 1
            elif blue:
                blue -= 1
                nums[i] = 2

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 双指针，双头夹击 - 不可以
        # 快慢指针 其实还是两次遍历
        # 一次遍历，常数级空间占用
        # 答案
        # 三指针，还是双头夹击
        start = 0
        end = len(nums) - 1
        index = start
        while index <= end:
            if nums[index] == 0:
                nums[index], nums[start] = nums[start], nums[index]
                start += 1
                if start > index:
                    index = start
            elif nums[index] == 2:
                nums[index], nums[end] = nums[end], nums[index]
                end -= 1
            else:
                index += 1

#
# if __name__ == '__main__':
#     s = Solution()
#     a = [2,0,2,1,1,0]
#     b = [2,0,1]
#     c = [0,2,1]
#     d = [2,1,0]
#     s.sortColors(b)
#     s.sortColors(a)
#     s.sortColors(c)
#     s.sortColors(d)
#     print a
#     print b
#     print c
#     print d
