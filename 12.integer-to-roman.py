#
# @lc app=leetcode id=12 lang=python
#
# [12] Integer to Roman
#
# https://leetcode.com/problems/integer-to-roman/description/
#
# algorithms
# Medium (49.81%)
# Total Accepted:    207.8K
# Total Submissions: 416.2K
# Testcase Example:  '3'
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D
# and M.
# 
# 
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 
# For example, two is written as II in Roman numeral, just two one's added
# together. Twelve is written as, XII, which is simply X + II. The number
# twenty seven is written as XXVII, which is XX + V + II.
# 
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is
# written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX. There
# are six instances where subtraction is used:
# 
# 
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# 
# 
# Given an integer, convert it to a roman numeral. Input is guaranteed to be
# within the range from 1 to 3999.
# 
# Example 1:
# 
# 
# Input: 3
# Output: "III"
# 
# Example 2:
# 
# 
# Input: 4
# Output: "IV"
# 
# Example 3:
# 
# 
# Input: 9
# Output: "IX"
# 
# Example 4:
# 
# 
# Input: 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
# 
# 
# Example 5:
# 
# 
# Input: 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# 
# 
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        ans = ""
        left = num / roman_map['M']
        num = num % roman_map['M']
        if left:
            if left <= 3:
                ans += left * "M"
            else:
                pass

        left = num / roman_map['C']
        num = num % roman_map['C']

        if left:
            if left <= 3:
                ans += left * "C"
            elif left < 5:
                ans += "CD"
            elif left < 9:
                ans += "D" + "C" * (left - 5)
            else:
                ans += "CM"

        left = num / roman_map['X']
        num = num % roman_map['X']

        if left:
            if left <= 3:
                ans += left * "X"
            elif left < 5:
                ans += "XL"
            elif left < 9:
                ans += "L" + "X" * (left - 5)
            else:
                ans += "XC"

        left = num / roman_map['I']
        num = num % roman_map['I']

        if left:
            if left <= 3:
                ans += left * "I"
            elif left < 5:
                ans += "IV"
            elif left < 9:
                ans += "V" + "I" * (left - 5)
            else:
                ans += "IX"
        
        return ans
