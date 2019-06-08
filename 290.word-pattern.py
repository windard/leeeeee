#
# @lc app=leetcode id=290 lang=python
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (34.53%)
# Likes:    629
# Dislikes: 77
# Total Accepted:    141.5K
# Total Submissions: 403.8K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string str, find if str follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
# 
# Example 1:
# 
# 
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# 
# Example 2:
# 
# 
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# 
# Example 3:
# 
# 
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# 
# Example 4:
# 
# 
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
# 
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters that may be separated by a single space.
# 
#
class Solution(object):
    def _wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # 和之前的另外一道题比较类似
        # [205] Isomorphic Strings
        strs = str.split()
        if len(pattern) != len(strs):
            return False
        pm = {}
        for key, value in enumerate(pattern):
            if value in pm:
                if pm[value] != strs[key]:
                    return False
            else:
                if strs[key] in pm.values():
                    return False
                pm[value] = strs[key]
        return True

    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strs = str.split()
        return map(pattern.index, pattern) == map(strs.index, strs)
