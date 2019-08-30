# coding=utf-8
#
# @lc app=leetcode id=50 lang=python
#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (27.55%)
# Likes:    857
# Dislikes: 2090
# Total Accepted:    324.2K
# Total Submissions: 1.2M
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n), which calculates x raised to the power n (x^n).
# 
# Example 1:
# 
# 
# Input: 2.00000, 10
# Output: 1024.00000
# 
# 
# Example 2:
# 
# 
# Input: 2.10000, 3
# Output: 9.26100
# 
# 
# Example 3:
# 
# 
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 
# Note:
# 
# 
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
# 
# 
#


class Solution(object):
    def _myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Time Limit
        if n == 0:
            return 1
        elif n < 0:
            x = 1.0 / x
            n = -n

        s = 1
        while n:
            s *= x
            n -= 1

        return s

    def __myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 1 or n == 0:
            return 1
        elif n < 0:
            x = 1.0 / x
            n = -n

        s = 1
        step = 1
        o = x
        while n:
            s *= x
            n -= step
            if n >= step * 2:
                x = x*x
                step *= 2
            else:
                x = o
                step = 1

        return s

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 1 or n == 0:
            return 1
        elif n < 0:
            x = 1.0 / x
            n = -n

        # 9 次方
        # 9 = 1001
        s = 1
        while n:
            if n & 1:
                s *= x
            n = n >> 1
            x = x * x
        return s

#
# if __name__ == '__main__':
#     s = Solution()
#     print s.myPow(2,10)
#     print s.myPow(2.1,3)
#     print s.myPow(2,-2)
#     print s.myPow(0.00001,2147483647)
