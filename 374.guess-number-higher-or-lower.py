#
# @lc app=leetcode id=374 lang=python
#
# [374] Guess Number Higher or Lower
#
# https://leetcode.com/problems/guess-number-higher-or-lower/description/
#
# algorithms
# Easy (38.74%)
# Total Accepted:    102.8K
# Total Submissions: 263.1K
# Testcase Example:  '10\n6'
#
# We are playing the Guess Game. The game is as follows:
# 
# I pick a number from 1 to n. You have to guess which number I picked.
# 
# Every time you guess wrong, I'll tell you whether the number is higher or
# lower.
# 
# You call a pre-defined API guess(int num) which returns 3 possible results
# (-1, 1, or 0):
# 
# 
# -1 : My number is lower
# ⁠1 : My number is higher
# ⁠0 : Congrats! You got it!
# 
# 
# Example :
# 
# 
# 
# Input: n = 10, pick = 6
# Output: 6
# 
# 
# 
#
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

# def guess(n):
#     a = 2
#     if a > n:
#         return 1
#     elif a < n:
#         return -1
#     else:
#         return 0

class Solution(object):

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while True:
            index = (left + right) / 2
            r = guess(index)
            if r > 0:
                left = index + 1
            elif r < 0:
                right = index - 1
            else:
                return index

# if __name__ == "__main__":
#     s = Solution()
#     print s.guessNumber(2)
        
