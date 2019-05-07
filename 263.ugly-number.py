#
# @lc app=leetcode id=263 lang=python
#
# [263] Ugly Number
#
# https://leetcode.com/problems/ugly-number/description/
#
# algorithms
# Easy (40.35%)
# Likes:    220
# Dislikes: 410
# Total Accepted:    154.7K
# Total Submissions: 381.6K
# Testcase Example:  '6'
#
# Write a program to check whether a given number is an ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# 
# Example 1:
# 
# 
# Input: 6
# Output: true
# Explanation: 6 = 2 × 3
# 
# Example 2:
# 
# 
# Input: 8
# Output: true
# Explanation: 8 = 2 × 2 × 2
# 
# 
# Example 3:
# 
# 
# Input: 14
# Output: false 
# Explanation: 14 is not ugly since it includes another prime factor 7.
# 
# 
# Note:
# 
# 
# 1 is typically treated as an ugly number.
# Input is within the 32-bit signed integer range: [−2^31,  2^31 − 1].
# 
#
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        
        while num:
            if num % 2 != 0:
                break
            num = num / 2 
    
        while num:
            if num % 3 != 0:
                break
            num = num / 3 
        
        while num:
            if num % 5 != 0:
                break
            num = num / 5 

        if num == 1:
            return True
        else:
            return False
