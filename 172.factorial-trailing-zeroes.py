#
# @lc app=leetcode id=172 lang=python
#
# [172] Factorial Trailing Zeroes
#
# https://leetcode.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Easy (37.26%)
# Likes:    455
# Dislikes: 653
# Total Accepted:    153.8K
# Total Submissions: 411.9K
# Testcase Example:  '3'
#
# Given an integer n, return the number of trailing zeroes in n!.
# 
# Example 1:
# 
# 
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# 
# Example 2:
# 
# 
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# 
# Note: Your solution should be in logarithmic time complexity.
# 
#
import math
class Solution(object):
    def _trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time Limited
        # 8979

        # s = 1
        # for i in range(1, n+1):
        #     s *= i
        
        s = math.factorial(n)
        l = 0
        for i in reversed(str(s)):
            if i == '0':
                l += 1
            else:
                return l
        return l

    def __trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Runtime Error
        if n == 0:
            return 0
        return n / 5 + self.trailingZeroes(n-1) if n % 5 == 0 else self.trailingZeroes(n-1)

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Accept
        # beautiful
        if n == 0:
            return 0
        return n / 5 + self.trailingZeroes(n / 5)
    
    def ____trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # count five nums
        # total wrong
        # caan't finish
        i = 0
        if n < 5:
            return 0
        s = n
        while n >= 5:
            i += 1
            n,l = divmod(n, 5)
        if s < 25:
            f = n
        else:
            f = l + 1
        return 5 * i * (i - 1) / 2 + f
