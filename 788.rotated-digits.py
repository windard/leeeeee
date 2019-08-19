# coding=utf-8
#
# @lc app=leetcode id=788 lang=python
#
# [788] Rotated Digits
#
# https://leetcode.com/problems/rotated-digits/description/
#
# algorithms
# Easy (54.96%)
# Likes:    221
# Dislikes: 752
# Total Accepted:    31.6K
# Total Submissions: 57.5K
# Testcase Example:  '10'
#
# X is a good number if after rotating each digit individually by 180 degrees,
# we get a valid number that is different from X.  Each digit must be rotated -
# we cannot choose to leave it alone.
# 
# A number is valid if each digit remains a digit after rotation. 0, 1, and 8
# rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each
# other, and the rest of the numbers do not rotate to any other number and
# become invalid.
# 
# Now given a positive number N, how many numbers X from 1 to N are good?
# 
# 
# Example:
# Input: 10
# Output: 4
# Explanation: 
# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after
# rotating.
# 
# 
# Note:
# 
# 
# N  will be in range [1, 10000].
# 
# 
#


class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        data = {
            '1': '1',
            '0': '0',
            '8': '8',
            '2': '5',
            '5': '2',
            '6': '9',
            '9': '6',
            '3': None,
            '4': None,
            '7': None,
        }
        index = 0
        count = 0
        while index <= N:
            source = ''
            for i in str(index):
                if data.get(i):
                    source += data[i]
                else:
                    break
            else:
                if int(source) != index:
                    count += 1
            index += 1
        return count
