#
# @lc app=leetcode id=205 lang=python
#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (36.73%)
# Likes:    751
# Dislikes: 213
# Total Accepted:    205K
# Total Submissions: 548K
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings are isomorphic if the characters in s can be replaced to get t.
# 
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character but a character may map to itself.
# 
# Example 1:
# 
# 
# Input: s = "egg", t = "add"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "foo", t = "bar"
# Output: false
# 
# Example 3:
# 
# 
# Input: s = "paper", t = "title"
# Output: true
# 
# Note:
# You may assume both s and t have the same length.
# 
#
class Solution(object):
    def _isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        transfer = {}
        i = 0
        while i < len(s):
            if s[i] not in transfer:
                transfer[s[i]] = t[i]
            else:
                if transfer[s[i]] != t[i]:
                    return False
            i += 1
        return len(transfer.values()) == len(set(transfer.values()))

    def __isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        transfer = {}
        i = 0
        while i < len(s):
            if s[i] not in transfer:
                if t[i] in transfer.values():
                    return False
                transfer[s[i]] = t[i]
            else:
                if transfer[s[i]] != t[i]:
                    return False
            i += 1
        return True

    def isIsomorphic(self, s, t):
        # Copy One
        return len(s) == len(t) and len(set(s)) == len(set(t)) == len(set(zip(s,t)))

# if __name__ == "__main__":
#     s = Solution()
#     print s.isIsomorphic('egg', 'add')
#     print s.isIsomorphic("foo", 'bar')
#     print s.isIsomorphic("paper", 'title')
