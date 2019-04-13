#
# @lc app=leetcode id=409 lang=python
#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (47.46%)
# Total Accepted:    93K
# Total Submissions: 194.7K
# Testcase Example:  '"abccccdd"'
#
# Given a string which consists of lowercase or uppercase letters, find the
# length of the longest palindromes that can be built with those letters.
# 
# This is case sensitive, for example "Aa" is not considered a palindrome
# here.
# 
# Note:
# Assume the length of given string will not exceed 1,010.
# 
# 
# Example: 
# 
# Input:
# "abccccdd"
# 
# Output:
# 7
# 
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# 
# 
#
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # same and easy
        sl = []
        res = 0
        for i in s:
            if i in sl:
                sl.remove(i)
                res += 2
            else:
                sl.append(i)
        return res if not sl else res + 1

    def _longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        sl = []
        res = 0
        for i in s:
            if i in sl:
                sl.remove(i)
                res += 1
            else:
                sl.append(i)
        return res * 2 if not sl else res * 2 + 1
