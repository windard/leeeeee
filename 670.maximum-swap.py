# coding=utf-8
#
# @lc app=leetcode id=670 lang=python
#
# [670] Maximum Swap
#
# https://leetcode.com/problems/maximum-swap/description/
#
# algorithms
# Medium (41.01%)
# Total Accepted:    45.4K
# Total Submissions: 110.6K
# Testcase Example:  '2736'
#
# 
# Given a non-negative integer, you could swap two digits at most once to get
# the maximum valued number. Return the maximum valued number you could get.
# 
# 
# Example 1:
# 
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# 
# 
# 
# Example 2:
# 
# Input: 9973
# Output: 9973
# Explanation: No swap.
# 
# 
# 
# 
# Note:
# 
# The given number is in the range [0, 10^8]
# 
# 
#


class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 同样单调栈
        stack = []
        for i, n in enumerate(str(num)):
            # 复杂的很
            # 98368 -> 98863
            # 1993  -> 9913
            while stack and (stack[-1][1] < n or (
                    stack[-1][1] == n and stack[-1][0] >= len(stack))):
                stack.pop()
            stack.append([i, n])
        for index, entry in enumerate(stack):
            if index != entry[0]:
                num = list(str(num))
                num[index], num[entry[0]] = num[entry[0]], num[index]
                return int(''.join(num))
        return num
