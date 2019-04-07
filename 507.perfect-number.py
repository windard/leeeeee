#
# @lc app=leetcode id=507 lang=python
#
# [507] Perfect Number
#
# https://leetcode.com/problems/perfect-number/description/
#
# algorithms
# Easy (33.56%)
# Total Accepted:    38K
# Total Submissions: 111.8K
# Testcase Example:  '28'
#
# We define the Perfect Number is a positive integer that is equal to the sum
# of all its positive divisors except itself. 
# 
# Now, given an integer n, write a function that returns true when it is a
# perfect number and false when it is not.
# 
# 
# Example:
# 
# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 
# 
# 
# Note:
# The input number n will not exceed 100,000,000. (1e8)
# 
#
import math

class Solution(object):
    def _checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        return sum(self.sqrt_drive_num(num)) == num

    def drive_num(self, num):
        # Timi Limited 
        # 20996011
        si = 2
        bi = num
        res = [1]
        while si < bi:
            if num % si == 0:
                bi = num / si
                res.extend([si, bi])
            si += 1
        return res

    def sqrt_drive_num(self, num):
        si = 2
        bi = math.sqrt(num)
        res = [1]
        if int(bi) == bi:
            res.append(bi)
        while si <= int(bi):
            if num % si == 0:
                res.extend([si, num / si])
            si += 1
        return res

    def division_drive_num(self, num):
        si = 2
        res = [1]
        last = num / si
        while si <= last:
            if num % si == 0:
                if si != last:
                    res.extend([si, last])
                else:
                    res.append(si)
            si += 1
            last = num / si
        return res

    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Euclid_Euler_Theorem
        # Euclid proved that 2^(p-1) * (2^p - 1) is an even perfect number 
        # whenever 2 ^ p - 1 is prime, where p is prime.
        ps = (2, 3, 5, 7, 13, 17, 19, 31)
        pn = [2**(p-1) * (2**p - 1) for p in ps]
        # [6, 28, 496, 8128, 33550336, 8589869056, 137438691328, 2305843008139952128]
        return num in pn

