# coding=utf-8
#
# @lc app=leetcode id=1033 lang=python
#
# [1033] Moving Stones Until Consecutive
#
# https://leetcode.com/problems/moving-stones-until-consecutive/description/
#
# algorithms
# Easy (37.26%)
# Likes:    30
# Dislikes: 262
# Total Accepted:    7.1K
# Total Submissions: 19.2K
# Testcase Example:  '1\n2\n5'
#
# Three stones are on a number line at positions a, b, and c.
# 
# Each turn, you pick up a stone at an endpoint (ie., either the lowest or
# highest position stone), and move it to an unoccupied position between those
# endpoints.  Formally, let's say the stones are currently at positions x, y, z
# with x < y < z.  You pick up the stone at either position x or position z,
# and move that stone to an integer position k, with x < k < z and k != y.
# 
# The game ends when you cannot make any more moves, ie. the stones are in
# consecutive positions.
# 
# When the game ends, what is the minimum and maximum number of moves that you
# could have made?  Return the answer as an length 2 array: answer =
# [minimum_moves, maximum_moves]
# 
# 
# 
# Example 1:
# 
# 
# Input: a = 1, b = 2, c = 5
# Output: [1,2]
# Explanation: Move the stone from 5 to 3, or move the stone from 5 to 4 to
# 3.
# 
# 
# 
# Example 2:
# 
# 
# Input: a = 4, b = 3, c = 2
# Output: [0,0]
# Explanation: We cannot make any moves.
# 
# 
# 
# Example 3:
# 
# 
# Input: a = 3, b = 5, c = 1
# Output: [1,2]
# Explanation: Move the stone from 1 to 4; or move the stone from 1 to 2 to
# 4.
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= a <= 100
# 1 <= b <= 100
# 1 <= c <= 100
# a != b, b != c, c != a
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#


class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        v = a + b + c
        a, c = min(a, b, c), max(a, b, c)
        b = v - a - c
        min_length = 0
        max_length = 0
        if b - a > 1:
            min_length += 1
            max_length += b - a - 1

        if c - b > 1:
            min_length += 1
            max_length += c - b - 1
        if b - a == 2 or c - b == 2:
            min_length = 1
        return min_length, max_length


# if __name__ == '__main__':
#     s = Solution()
#     print s.numMovesStones(4, 3, 2)
