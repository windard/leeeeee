# coding=utf-8
#
# @lc app=leetcode id=470 lang=python
#
# [470] Implement Rand10() Using Rand7()
#
# https://leetcode.com/problems/implement-rand10-using-rand7/description/
#
# algorithms
# Medium (45.24%)
# Likes:    265
# Dislikes: 89
# Total Accepted:    13.2K
# Total Submissions: 29.2K
# Testcase Example:  '1'
#
# Given a function rand7 which generates a uniform random integer in the range
# 1 to 7, write a function rand10 which generates a uniform random integer in
# the range 1 to 10.
# 
# Do NOT use system's Math.random().
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: [7]
# 
# 
# 
# Example 2:
# 
# 
# Input: 2
# Output: [8,4]
# 
# 
# 
# Example 3:
# 
# 
# Input: 3
# Output: [8,1,10]
# 
# 
# 
# 
# Note:
# 
# 
# rand7 is predefined.
# Each testcase has one argument: n, the number of times that rand10 is
# called.
# 
# 
# 
# 
# Follow up:
# 
# 
# What is the expected value for the number of calls to rand7() function?
# Could you minimize the number of calls to rand7()?
# 
# 
# 
# 
# 
#

# @lc code=start
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


class Solution(object):
    def _rand10(self):
        """
        :rtype: int
        """
        # Wrong Answer
        # rand7 * 10 / 7
        # but not right
        # 1 2 3 4 5 6 7
        # 1 2 4 5 7 8 10
        return rand7() * 10 / 7

    def rand10(self):
        """
        :rtype: int
        """
        # 调用两次随机的结果。
        # 49种情况，只取前40，后九种就丢弃。
        # 每个数都有四次机会被选上
        #
        #   | 1   2   3   4   5   6   7
        # -----------------------------
        #  1| 1   2   3   4   5   6   7
        #  2| 8   9  10   1   2   3   4
        #  3| 5   6   7   8   9  10   1
        #  4| 2   3   4   5   6   7   8
        #  5| 9  10   1   2   3   4   5
        #  6| 6   7   8   9  10   *   *
        #  7| *   *   *   *   *   *   *
        while True:
            x = rand7()
            y = rand7()
            if 7 * (y-1) + x <= 40:
                # return (7 * (y-1) + x) % 10 if (7 * (y-1) + x) % 10 else 10
                return (7 * (y-1) + x) % 10 + 1

# @lc code=end

