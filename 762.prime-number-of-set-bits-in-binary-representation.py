#
# @lc app=leetcode id=762 lang=python
#
# [762] Prime Number of Set Bits in Binary Representation
#
# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/
#
# algorithms
# Easy (60.11%)
# Likes:    164
# Dislikes: 252
# Total Accepted:    31.7K
# Total Submissions: 52.7K
# Testcase Example:  '842\n888'
#
# 
# Given two integers L and R, find the count of numbers in the range [L, R]
# (inclusive) having a prime number of set bits in their binary
# representation.
# 
# (Recall that the number of set bits an integer has is the number of 1s
# present when written in binary.  For example, 21 written in binary is 10101
# which has 3 set bits.  Also, 1 is not a prime.)
# 
# 
# Example 1:
# Input: L = 6, R = 10
# Output: 4
# Explanation:
# 6 -> 110 (2 set bits, 2 is prime)
# 7 -> 111 (3 set bits, 3 is prime)
# 9 -> 1001 (2 set bits , 2 is prime)
# 10->1010 (2 set bits , 2 is prime)
# 
# 
# Example 2:
# Input: L = 10, R = 15
# Output: 5
# Explanation:
# 10 -> 1010 (2 set bits, 2 is prime)
# 11 -> 1011 (3 set bits, 3 is prime)
# 12 -> 1100 (2 set bits, 2 is prime)
# 13 -> 1101 (3 set bits, 3 is prime)
# 14 -> 1110 (3 set bits, 3 is prime)
# 15 -> 1111 (4 set bits, 4 is not prime)
# 
# 
# Note:
# L, R will be integers L  in the range [1, 10^6].
# R - L will be at most 10000.
# 
#

import math


class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        index = L
        count = 0
        while index <= R:
            num = bin(index).count("1")
            if self.isPrime(num):
                count += 1
            index += 1
        return count

    def isPrime(self, x):
        if x < 2:
            return False
        if x < 4:
            return True
        index = 2
        while index <= math.sqrt(x):
            if not x % index:
                return False
            index += 1
        return True
