#
# @lc app=leetcode id=509 lang=python
#
# [509] Fibonacci Number
#
# https://leetcode.com/problems/fibonacci-number/description/
#
# algorithms
# Easy (66.37%)
# Total Accepted:    20.5K
# Total Submissions: 30.8K
# Testcase Example:  '2'
#
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
# Fibonacci sequence, such that each number is the sum of the two preceding
# ones, starting from 0 and 1. That is,
#
#
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.
#
#
# Given N, calculate F(N).
#
#
#
# Example 1:
#
#
# Input: 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
#
#
# Example 2:
#
#
# Input: 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
#
#
# Example 3:
#
#
# Input: 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
#
#
#
#
# Note:
#
# 0 ≤ N ≤ 30.
#
#
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        result = 0
        last_one = 0
        last_two = 0
        for i in range(N+1):
            if i == 0:
                result = 0
            elif i == 1:
                result = 1
            else:
                result = last_one + last_two
            if last_one:
                last_two = last_one
            last_one = result
        return result


    def _fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            return self._fib(N - 1) + self._fib(N - 2)
