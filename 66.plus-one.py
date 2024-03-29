#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (40.55%)
# Total Accepted:    346.2K
# Total Submissions: 853.4K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
#
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
#
# Example 1:
#
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
#
#
# Example 2:
#
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
#
#
#
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        digits = digits[::-1]
        left = 0
        r = []
        if not digits:
            return [1]
        digits[0] += 1
        for digit in digits:
            a = left + digit
            r.append(a % 10)
            left = a / 10
        if left:
            r.append(left)
        return r[::-1]

