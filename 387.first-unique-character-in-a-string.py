#
# @lc app=leetcode id=387 lang=python
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (49.20%)
# Total Accepted:    250.5K
# Total Submissions: 504.5K
# Testcase Example:  '"leetcode"'
#
# 
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
# 
# Examples:
# 
# s = "leetcode"
# return 0.
# 
# s = "loveleetcode",
# return 2.
# 
# 
# 
# 
# Note: You may assume the string contain only lowercase letters.
# 
#

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1
