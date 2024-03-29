# coding=utf-8
#
# @lc app=leetcode id=796 lang=python
#
# [796] Rotate String
#
# https://leetcode.com/problems/rotate-string/description/
#
# algorithms
# Easy (49.19%)
# Likes:    432
# Dislikes: 39
# Total Accepted:    44.8K
# Total Submissions: 91.1K
# Testcase Example:  '"abcde"\n"cdeab"'
#
# We are given two strings, A and B.
# 
# A shift on A consists of taking string A and moving the leftmost character to
# the rightmost position. For example, if A = 'abcde', then it will be 'bcdea'
# after one shift on A. Return True if and only if A can become B after some
# number of shifts on A.
# 
# 
# Example 1:
# Input: A = 'abcde', B = 'cdeab'
# Output: true
# 
# Example 2:
# Input: A = 'abcde', B = 'abced'
# Output: false
# 
# 
# Note:
# 
# 
# A and B will have length at most 100.
# 
# 
#


class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A == B:
            return True
        for _ in range(len(A)):
            A = A[1:]+A[0]
            if A == B:
                return True
        return False


# if __name__ == '__main__':
#     s = Solution()
#     print s.rotateString("abcde", "cdeab")
#     print s.rotateString("abcde", "abced")
