#
# @lc app=leetcode id=231 lang=python
#
# [231] Power of Two
#
# https://leetcode.com/problems/power-of-two/description/
#
# algorithms
# Easy (41.55%)
# Total Accepted:    212K
# Total Submissions: 509.8K
# Testcase Example:  '1'
#
# Given an integer, write a function to determine if it is a power of two.
#
# Example 1:
#
#
# Input: 1
# Output: true
# Explanation: 20 = 1
#
#
# Example 2:
#
#
# Input: 16
# Output: true
# Explanation: 24 = 16
#
# Example 3:
#
#
# Input: 218
# Output: false
#
#
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return (n & n - 1) == 0

    def _isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1 or n == 2:
            return True
        elif n == 0:
            return False
        left = n % 2
        if left:
            return False
        n = n / 2
        while n:
            if n == 2:
                return True
            left = n % 2
            if left:
                return False
            n = n / 2
        return True
