#
# @lc app=leetcode id=326 lang=python
#
# [326] Power of Three
#
# https://leetcode.com/problems/power-of-three/description/
#
# algorithms
# Easy (41.40%)
# Total Accepted:    179.2K
# Total Submissions: 431.2K
# Testcase Example:  '27'
#
# Given an integer, write a function to determine if it is a power of three.
# 
# Example 1:
# 
# 
# Input: 27
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: 0
# Output: false
# 
# Example 3:
# 
# 
# Input: 9
# Output: true
# 
# Example 4:
# 
# 
# Input: 45
# Output: false
# 
# Follow up:
# Could you do it without using any loop / recursion?
#
n3 = [3**i for i in range(21)]

class Solution(object):
    def _isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if not n:
            return False
        while n != 1:
            if n % 3 == 0:
                n = n / 3
            else:
                return False
        return True

    def __isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n in n3

    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 3 ** 21 % n == 0
