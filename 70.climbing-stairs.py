#
# @lc app=leetcode id=70 lang=python
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (43.14%)
# Total Accepted:    352.2K
# Total Submissions: 813.4K
# Testcase Example:  '2'
#
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
#
# Note: Given n will be a positive integer.
#
# Example 1:
#
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
#
# Example 2:
#
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
#

from functools import wraps


def cache(func):
    saved = {}

    @wraps(func)
    def new_func(*args):
        # one point
        # set can be dict key
        if args in saved:
            return saved[args]
        result = func(*args)
        saved[args] = result
        return result
    return new_func


class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # not recursive
        # but cycle iteration
        N = n
        result = 0
        last_one = 0
        last_two = 0
        for i in range(N + 1):
            if i == 0:
                result = 0
            elif i == 1:
                result = 1
            elif i == 2:
                result = 2
            else:
                result = last_one + last_two
            if last_one:
                last_two = last_one
            last_one = result
        return result

    @cache
    def _climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # best solution but time limit
        #  - - cry... cache can do speed up
        if n < 1:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self._climbStairs(n - 1) + self._climbStairs(n - 2)
