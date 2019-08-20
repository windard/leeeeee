#
# @lc app=leetcode id=633 lang=python
#
# [633] Sum of Square Numbers
#
# https://leetcode.com/problems/sum-of-square-numbers/description/
#
# algorithms
# Easy (32.68%)
# Likes:    362
# Dislikes: 243
# Total Accepted:    48.9K
# Total Submissions: 149.7K
# Testcase Example:  '5'
#
# Given a non-negative integer c, your task is to decide whether there're two
# integers a and b such that a^2 + b^2 = c.
# 
# Example 1:
# 
# 
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 3
# Output: False
# 
# 
# 
# 
#

import math


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        index = 0
        while index <= math.sqrt(c):
            l = math.sqrt(c - index*index)
            if int(l) == l:
                return True
            index += 1
        return False
