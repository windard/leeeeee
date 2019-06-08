#
# @lc app=leetcode id=342 lang=python
#
# [342] Power of Four
#
# https://leetcode.com/problems/power-of-four/description/
#
# algorithms
# Easy (39.98%)
# Likes:    315
# Dislikes: 141
# Total Accepted:    114.1K
# Total Submissions: 283.1K
# Testcase Example:  '16'
#
# Given an integer (signed 32 bits), write a function to check whether it is a
# power of 4.
# 
# Example 1:
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
# Input: 5
# Output: false
# 
# 
# Follow up: Could you solve it without loops/recursion?
#
class Solution(object):
    def _isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        while num != 1:
            left, right = divmod(num, 4)
            if right != 0:
                return False
            num = left
        return True

    def __isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        length = len(format(num, 'b'))
        return num & num - 1 == 0 and length % 2 == 1

    def ___isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and num & num - 1 == 0 and num % 3 == 1

    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 0x55555555 = 0b1010101010101010101010101010101
        return num > 0 and num & num - 1 == 0 and num & 0x55555555 == num
