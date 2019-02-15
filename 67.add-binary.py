#
# @lc app=leetcode id=67 lang=python
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (37.63%)
# Total Accepted:    271.2K
# Total Submissions: 719.7K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
#
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
#
#
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a)
        len_b = len(b)
        length = len_a if len_a > len_b else len_b
        res = ''
        flag = 0
        a = a[::-1]
        b = b[::-1]
        for i in range(length):
            g = flag
            if len(a) > i:
                g += int(a[i])
            if len(b) > i:
                g += int(b[i])
            res += "{}".format(g % 2)
            flag = g / 2
        if flag:
            res += '1'

        return res[::-1]
