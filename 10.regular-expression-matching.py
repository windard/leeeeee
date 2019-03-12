#
# @lc app=leetcode id=10 lang=python
#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (24.98%)
# Total Accepted:    279.3K
# Total Submissions: 1.1M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement regular expression
# matching with support for '.' and '*'.
# 
# 
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# 
# 
# The matching should cover the entire input string (not partial).
# 
# Note:
# 
# 
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like
# . or *.
# 
# 
# Example 1:
# 
# 
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# 
# 
# Example 2:
# 
# 
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
# 
# 
# Example 3:
# 
# 
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# 
# 
# Example 4:
# 
# 
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore
# it matches "aab".
# 
# 
# Example 5:
# 
# 
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false
# 
# 
#
import re
import string
class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # True Solution
        # DP: Dynamic Programming

    def isReMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # re library
        return bool(re.match("^" + p + "$", s))

    def isNotGreedMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # "aaaaaaa"\n"a*a"
        if not s:
            return True
        if s and not p:
            return False
        
        last_pattern = None
        si = 0
        pi = 0
        while 1:
            next_pattern, ti = self.getNextPattern(p, pi)
            if si >= len(s) and pi >= len(p):
                return True
            if next_pattern and self.checkMatch(next_pattern, s[si]):
                last_pattern = next_pattern
                si += 1
                pi = ti
            elif last_pattern and self.checkMatch(last_pattern, s[si]):
                si += 1

    def getNextPattern(self, p, pi):
        if pi >= len(p):
            return None, 0
        if pi + 1 < len(p) and p[pi] == "*":
            next_pattern = p[pi:pi+1]
            pi += 2
        else:
            next_pattern = p[pi:pi]
            pi += 1
        return next_pattern, pi

    def checkMatch(self, pattern, s):
        if pattern[0] == s or pattern[0] == ".":
            return True
        return False

    def isGreedMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # pattern should greed match
        # "aaa"\n"a*a"
        if not s:
            return True
        if s and not p:
            return False
        
        si = 0
        pi = 0
        while 1:
            if si >= len(s) and (pi >= len(p) or (pi == len(p) - 1 and p[pi] == "*")):
                return True
            elif si >= len(s) or pi >= len(p):
                return False
            if p[pi] in string.lowercase or p[pi] == ".":
                if s[si] == p[pi] or p[pi] == ".":
                    si += 1
                    pi += 1
                else:
                    if pi + 1 < len(p) and p[pi + 1] == "*":
                        pi += 1
                    else:
                        return False
            else:
                if pi > 0 and (p[pi - 1] == s[si] or p[pi-1] == "."):
                    si += 1
                else:
                    pi += 1


    def isPartMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # pattern should Perfect match
        # "aaa"\n"a*b"
        if not s:
            return True
        if s and not p:
            return False
        pi = 0
        i = 0
        while 1:
            if i >= len(s):
                if pi >= len(p):
                    return True
                else:
                    return False
            if pi >= len(p):
                return False
            if p[pi] == "." or p[pi] == s[i]:
                if pi + 1 < len(p) and p[pi + 1] == "*":
                    pass
                else:
                    pi += 1
                i += 1
            else:
                if pi + 2 < len(p) and p[pi + 1] == "*":
                    pi += 2 
                    continue
                else:
                    return False
        return True

# if __name__ == "__main__":
#     s = Solution()
#     print s.isMatch("aaa", "aaaa")
