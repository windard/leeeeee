# coding=utf-8
#
# @lc app=leetcode id=29 lang=python
#
# [29] Divide Two Integers
#
# https://leetcode.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (16.08%)
# Likes:    680
# Dislikes: 3224
# Total Accepted:    198K
# Total Submissions: 1.2M
# Testcase Example:  '10\n3'
#
# Given two integers dividend and divisor, divide two integers without using
# multiplication, division and mod operator.
# 
# Return the quotient after dividing dividend by divisor.
# 
# The integer division should truncate toward zero.
# 
# Example 1:
# 
# 
# Input: dividend = 10, divisor = 3
# Output: 3
# 
# Example 2:
# 
# 
# Input: dividend = 7, divisor = -3
# Output: -2
# 
# Note:
# 
# 
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 2^31 − 1 when the division
# result overflows.
# 
# 
#

import time


def api_deco(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print time.time() - start
        return result
    return wrapper


class Solution(object):
    def _divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # 7/-3
        # Wrong Answer
        return divmod(dividend, divisor)[0]

    def ___divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Time Limit
        # minus with multi
        if dividend == 0 or divisor == 0:
            return 0
        flag = True
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            flag = False
        # flag = divisor * dividend > 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        while dividend > 0:
            dividend = dividend - divisor
            count += 1
        return count-1 if flag else - (count-1)

    def ____divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # minus with multi
        if dividend == 0 or divisor == 0:
            return 0
        flag = True
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            flag = False

        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        while dividend > 0:
            rank = 1
            step = divisor * rank
            dividend = dividend - step
            count += rank
            while step <= dividend:
                dividend = dividend - step
                count += rank
                rank += rank
                step = divisor * rank
            # 不能翻倍增长，只能成倍增长
            # 成倍增长还是太慢，Time Limit
            # 最好还是要成倍增长，但是增长完了回不来了。
            # 但是还是无法成倍增长
            # 还是成倍增长，增长至顶之后再从1开始

        if dividend:
            count -= 1
        count = count if flag else -count
        if count >= 2**31-1 or count < -2**31:
            return 2**31-1
        return count

    def __divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        from operator import div, truediv
        a = int(truediv(dividend, divisor))
        if a >= 2**31-1 or a < -2**31:
            return 2**31-1
        return a

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # 转为二进制容易对比
        if dividend == 0 or divisor == 0:
            return 0
        flag = True
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            flag = False

        dividend = abs(dividend)
        divisor = abs(divisor)

        length = len(bin(dividend)) - len(bin(divisor))
        res = []
        while length >= 0:
            if divisor << length <= dividend:
                dividend -= divisor << length
                res.append('1')
            else:
                res.append('0')
            length -= 1

        if not res:
            return 0
        count = int(''.join(res), 2)
        count = count if flag else -count
        if count >= 2**31-1 or count < -2**31:
            return 2**31-1
        return count


# if __name__ == '__main__':
#     s = Solution()
#     print s.divide(9, 3)
#     print s.divide(100, 3)
#     print s.divide(1000, 5)
#     print s.divide(10, 3)
#     print s.divide(7, -3)
#     print s.divide(-2147483648, 1)
