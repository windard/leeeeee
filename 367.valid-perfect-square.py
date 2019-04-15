#
# @lc app=leetcode id=367 lang=python
#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (39.40%)
# Total Accepted:    105.1K
# Total Submissions: 265.3K
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
# 
# Note: Do not use any built-in library function such as sqrt.
# 
# Example 1:
# 
# 
# 
# Input: 16
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: 14
# Output: false
# 
# 
# 
#
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 即完全平方数肯定是前n个连续奇数的和
        s = i = 1
        while True:
            if s < num:
                i += 2
                s += i
            elif s == num:
                return True
            else:
                return False

    def _isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while True:
            s = i * i
            if s < num:
                i += 1
            elif s == num:
                return True
            else:
                return False
