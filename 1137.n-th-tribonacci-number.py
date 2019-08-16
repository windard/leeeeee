# coding=utf-8
#
# @lc app=leetcode id=1137 lang=python
#
# [1137] N-th Tribonacci Number
#
# https://leetcode.com/problems/n-th-tribonacci-number/description/
#
# algorithms
# Easy (60.72%)
# Likes:    47
# Dislikes: 8
# Total Accepted:    9.4K
# Total Submissions: 15.4K
# Testcase Example:  '4'
#
# The Tribonacci sequence Tn is defined as follows: 
# 
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# 
# Given n, return the value of Tn.
# 
# 
# Example 1:
# 
# 
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
# 
# 
# Example 2:
# 
# 
# Input: n = 25
# Output: 1389537
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 -
# 1.
# 
#


class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 0
        second = 1
        third = 1
        if n == 0:
            return first
        elif n == 1:
            return second
        elif n == 2:
            return third
        index = 2
        while index < n:
            third, second, first = third+second+first, third, second
            index += 1
        return third


# if __name__ == '__main__':
#     s = Solution()
#     print s.tribonacci(3)
#     print s.tribonacci(4)
#     print s.tribonacci(5)
#     print s.tribonacci(6)
#     print s.tribonacci(10)  # 149
#     print s.tribonacci(25)  # 1389537

