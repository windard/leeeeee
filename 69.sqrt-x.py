#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (30.69%)
# Total Accepted:    337.7K
# Total Submissions: 1.1M
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
# 
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
# 
# Example 1:
# 
# 
# Input: 4
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
# the decimal part is truncated, 2 is returned.
# 
# 
#
import math
class Solution(object):

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Newton
        r = x
        while r * r > x:
            r = (r + x / r) / 2
        return r

    def ___mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x:
            return 0
        return int(math.e**(math.log(x+0.5)/2))

    def __mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(math.sqrt(x))

    def _mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0
        while i <= x:
            j = i * i
            if j == x:
                return i
            elif j > x:
                return i - 1
            i += 1
