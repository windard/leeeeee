#
# @lc app=leetcode id=728 lang=python
#
# [728] Self Dividing Numbers
#
# https://leetcode.com/problems/self-dividing-numbers/description/
#
# algorithms
# Easy (71.07%)
# Likes:    453
# Dislikes: 245
# Total Accepted:    89.2K
# Total Submissions: 125.5K
# Testcase Example:  '1\n22'
#
# 
# A self-dividing number is a number that is divisible by every digit it
# contains.
# 
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 ==
# 0, and 128 % 8 == 0.
# 
# Also, a self-dividing number is not allowed to contain the digit zero.
# 
# Given a lower and upper number bound, output a list of every possible self
# dividing number, including the bounds if possible.
# 
# Example 1:
# 
# Input: 
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
# 
# 
# 
# Note:
# The boundaries of each input argument are 1 .
# 
#


class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        index = left
        result = []
        while index <= right:
            if self.is_self_dividing(index):
                result.append(index)
            index += 1
        return result

    def is_self_dividing(self, x):
        if '0' in str(x):
            return False

        for s in str(x):
            if x % int(s):
                return False

        return True
