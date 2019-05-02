#
# @lc app=leetcode id=371 lang=python
#
# [371] Sum of Two Integers
#
# https://leetcode.com/problems/sum-of-two-integers/description/
#
# algorithms
# Easy (51.21%)
# Total Accepted:    129.7K
# Total Submissions: 254.2K
# Testcase Example:  '1\n2'
#
# Calculate the sum of two integers a and b, but you are not allowed to use the
# operator + and -.
# 
# 
# Example 1:
# 
# 
# Input: a = 1, b = 2
# Output: 3
# 
# 
# 
# Example 2:
# 
# 
# Input: a = -2, b = 3
# Output: 1
# 
# 
# 
# 
#
class Solution(object):
    def _getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return a + b

    def __getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return sum([a, b])

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # Amazing
        if not a:
            return b
        if not b:
            return a
        return (a ^ b) + ((a & b) << 1)
