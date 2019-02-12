#
# @lc app=leetcode id=504 lang=python
#
# [504] Base 7
#
# https://leetcode.com/problems/base-7/description/
#
# algorithms
# Easy (44.48%)
# Total Accepted:    37.6K
# Total Submissions: 84.6K
# Testcase Example:  '100'
#
# Given an integer, return its base 7 string representation.
#
# Example 1:
#
# Input: 100
# Output: "202"
#
#
#
# Example 2:
#
# Input: -7
# Output: "-10"
#
#
#
# Note:
# The input will be in range of [-1e7, 1e7].
#
#
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        flag = True
        if num < 0:
            flag = False
            num = abs(num)

        if num == 0:
            return "0"

        right = ''
        step = 7

        while num:
            left = num % step
            right = str(left) + right
            num /= step

        return right if flag else '-' + right
