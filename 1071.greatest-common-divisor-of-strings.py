# coding=utf-8
#
# @lc app=leetcode id=1071 lang=python
#
# [1071] Greatest Common Divisor of Strings
#
# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
#
# algorithms
# Easy (54.29%)
# Likes:    130
# Dislikes: 43
# Total Accepted:    10.3K
# Total Submissions: 19K
# Testcase Example:  '"ABCABC"\n"ABC"'
#
# For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T
# concatenated with itself 1 or more times)
# 
# Return the largest string X such that X divides str1 and X divides str2.
# 
# 
# 
# Example 1:
# 
# 
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# 
# 
# Example 2:
# 
# 
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# 
# 
# Example 3:
# 
# 
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= str1.length <= 1000
# 1 <= str2.length <= 1000
# str1[i] and str2[i] are English uppercase letters.
# 
#

import math


class Solution(object):
    def _gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if not str1 or not str2:
            return ""
        factors = self.getFactors(len(str1), len(str2))
        for factor in sorted(factors, reverse=True):
            piece = str1[:factor]
            index = 0
            while index < max(len(str1), len(str2)):
                if index+factor <= len(str1):
                    if str1[index:index+factor] != piece:
                        break
                if index+factor <= len(str2):
                    if str2[index:index+factor] != piece:
                        break
                index += factor
            else:
                return piece
        return ""

    def getFactors(self, a, b):
        a, b = max(a, b), min(a, b)
        factors = []
        while b:
            a, b = b, a % b
        factors.append(a)
        index = 2
        while index <= math.sqrt(a):
            if not a % index:
                factors.append(index)
                factors.append(a / index)
            index += 1
        return factors

    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:self.gcd(len(str1), len(str2))]

    def gcd(self, a, b):
        a, b = max(a, b), min(a, b)
        while b:
            a, b = b, a % b
        return a

# if __name__ == '__main__':
#     s = Solution()
#     print s.gcdOfStrings("", "")
#     print s.gcdOfStrings("", "ab")
#     print s.gcdOfStrings("ABCABC", "ABC")
#     print s.gcdOfStrings("ABABAB", "ABAB")
#     print s.gcdOfStrings("LEFT", "RIGHT")
#     print s.gcdOfStrings("aaaaa", "aaaa")
#     print s.gcdOfStrings("aaaaaaaa", 'aaaaaa')
