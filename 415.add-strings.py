#
# @lc app=leetcode id=415 lang=python
#
# [415] Add Strings
#
# https://leetcode.com/problems/add-strings/description/
#
# algorithms
# Easy (43.04%)
# Total Accepted:    90.2K
# Total Submissions: 207.9K
# Testcase Example:  '"0"\n"0"'
#
# Given two non-negative integers num1 and num2 represented as string, return
# the sum of num1 and num2.
# 
# Note:
# 
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#
class Solution(object):
    def _addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) + int(num2))
        
    def _addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        length = max(len(num1), len(num2))
        index = 0
        coverage = 0
        current = 0
        res = ''
        num1 = list(reversed(num1))
        num2 = list(reversed(num2))
        while index < length:
            a = 0
            if len(num1) > index:
                a += int(num1[index])
            if len(num2) > index:
                a += int(num2[index])
            
            a += coverage
            current = a % 10
            coverage = a / 10

            res = str(current) + res
            index += 1
        if coverage:
            res = str(coverage) + res
        return res

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        length = max(len(num1), len(num2))
        current = coverage = 0
        res = ''
        num1 = num1.zfill(length)
        num2 = num2.zfill(length)
        for index in range(length-1, -1, -1):
            a = self.int(num1[index]) + self.int(num2[index]) + coverage
            coverage, current = divmod(a, 10)
            res = str(current) + res
        if coverage:
            res = str(coverage) + res
        return res

    def int(self, num):
        return ord(num) - ord('0')
