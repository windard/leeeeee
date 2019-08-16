# coding=utf-8
#
# @lc app=leetcode id=709 lang=python
#
# [709] To Lower Case
#
# https://leetcode.com/problems/to-lower-case/description/
#
# algorithms
# Easy (76.28%)
# Likes:    310
# Dislikes: 1079
# Total Accepted:    131.9K
# Total Submissions: 170.6K
# Testcase Example:  '"Hello"'
#
# Implement function ToLowerCase() that has a string parameter str, and returns
# the same string in lowercase.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: "Hello"
# Output: "hello"
# 
# 
# 
# Example 2:
# 
# 
# Input: "here"
# Output: "here"
# 
# 
# 
# Example 3:
# 
# 
# Input: "LOVELY"
# Output: "lovely"
# 
# 
# 
# 
# 
#


class Solution(object):
    def _toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()

    def __toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        convert = dict(zip(upper, lower))
        result = ''
        for s in str:
            result += convert.get(s, s)
        return result

    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        result = ''
        for s in str:
            if 65 <= ord(s) <= 90:
                result += chr(ord(s)+32)
            else:
                result += s
        return result
