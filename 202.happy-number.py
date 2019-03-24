#
# @lc app=leetcode id=202 lang=python
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (44.30%)
# Total Accepted:    218.5K
# Total Submissions: 491K
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number is "happy".
# 
# A happy number is a number defined by the following process: Starting with
# any positive integer, replace the number by the sum of the squares of its
# digits, and repeat the process until the number equals 1 (where it will
# stay), or it loops endlessly in a cycle which does not include 1. Those
# numbers for which this process ends in 1 are happy numbers.
# 
# Example: 
# 
# 
# Input: 19
# Output: true
# Explanation: 
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 
#
class Solution(object):

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 42 is answer of everything
        while n != 42:
            prev, n = n, sum(map(lambda i: int(i)**2, str(n)))
            if prev == n:
                return True
        return False

    def _isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 循环可以，递归也可以
        num_sum = n
        repeat_num = []
        repeat_num.append(n)
        while num_sum != 1:
            num_sum = 0
            for i in str(n):
                num_sum += int(i)**2
            if num_sum in repeat_num:
                return False
            repeat_num.append(num_sum)
            n = num_sum
        return True
