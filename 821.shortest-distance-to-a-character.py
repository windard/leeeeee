# coding=utf-8
#
# @lc app=leetcode id=821 lang=python
#
# [821] Shortest Distance to a Character
#
# https://leetcode.com/problems/shortest-distance-to-a-character/description/
#
# algorithms
# Easy (62.75%)
# Likes:    658
# Dislikes: 57
# Total Accepted:    42K
# Total Submissions: 65.7K
# Testcase Example:  '"loveleetcode"\n"e"'
#
# Given a string S and a character C, return an array of integers representing
# the shortest distance from the character C in the string.
# 
# Example 1:
# 
# 
# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
# 
# 
# 
# 
# Note:
# 
# 
# S string length is in [1, 10000].
# C is a single character, and guaranteed to be in string S.
# All letters in S and C are lowercase.
# 
# 
#


class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        cp = []
        for i, s in enumerate(S):
            if s == C:
                cp.append(i)

        result = []
        for i, s in enumerate(S):
            result.append(min(map(lambda x: abs(i-x), cp)))

        return result
