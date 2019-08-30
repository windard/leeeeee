# coding=utf-8
#
# @lc app=leetcode id=43 lang=python
#
# [43] Multiply Strings
#
# https://leetcode.com/problems/multiply-strings/description/
#
# algorithms
# Medium (29.97%)
# Likes:    1015
# Dislikes: 472
# Total Accepted:    205.7K
# Total Submissions: 666.4K
# Testcase Example:  '"2"\n"3"'
#
# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2, also represented as a string.
# 
# Example 1:
# 
# 
# Input: num1 = "2", num2 = "3"
# Output: "6"
# 
# Example 2:
# 
# 
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# 
# 
# Note:
# 
# 
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0
# itself.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        count = 0
        step_a = 1
        for a in num1[::-1]:
            step_b = 1
            for b in num2[::-1]:
                count += int(a) * int(b) * step_a * step_b
                step_b *= 10

            step_a *= 10
        return str(count)


# if __name__ == '__main__':
#     s = Solution()
#     print s.multiply("123", "25")
