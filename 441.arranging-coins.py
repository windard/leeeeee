#
# @lc app=leetcode id=441 lang=python
#
# [441] Arranging Coins
#
# https://leetcode.com/problems/arranging-coins/description/
#
# algorithms
# Easy (37.33%)
# Total Accepted:    63K
# Total Submissions: 168.5K
# Testcase Example:  '5'
#
# You have a total of n coins that you want to form in a staircase shape, where
# every k-th row must have exactly k coins.
# ⁠
# Given n, find the total number of full staircase rows that can be formed.
#
# n is a non-negative integer and fits within the range of a 32-bit signed
# integer.
#
# Example 1:
#
# n = 5
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
#
# Because the 3rd row is incomplete, we return 2.
#
#
#
# Example 2:
#
# n = 8
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
#
# Because the 4th row is incomplete, we return 3.
#
#
#
import math
class Solution(object):
    def _arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.floor(math.sqrt(2 * n + 0.25) - 0.5))

    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        i = 1
        while True:
            a += i
            if a > n:
                return i - 1
            i += 1
