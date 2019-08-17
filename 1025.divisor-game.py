# coding=utf-8
#
# @lc app=leetcode id=1025 lang=python
#
# [1025] Divisor Game
#
# https://leetcode.com/problems/divisor-game/description/
#
# algorithms
# Easy (64.23%)
# Likes:    128
# Dislikes: 368
# Total Accepted:    19.4K
# Total Submissions: 30.2K
# Testcase Example:  '2'
#
# Alice and Bob take turns playing a game, with Alice starting first.
# 
# Initially, there is a number N on the chalkboard.  On each player's turn,
# that player makes a move consisting of:
# 
# 
# Choosing any x with 0 < x < N and N % x == 0.
# Replacing the number N on the chalkboard with N - x.
# 
# 
# Also, if a player cannot make a move, they lose the game.
# 
# Return True if and only if Alice wins the game, assuming both players play
# optimally.
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
# Input: 2
# Output: true
# Explanation: Alice chooses 1, and Bob has no more moves.
# 
# 
# 
# Example 2:
# 
# 
# Input: 3
# Output: false
# Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more
# moves.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 1000
# 
# 
# 
#

import math


class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        if N < 2:
            return False
        elif N < 3:
            return True
        status = [0]*(N+1)
        status[2] = 1
        index = 3
        while index <= N:
            factors = self.getFactors(index)
            last_status = [status[index-f] for f in factors]
            status[index] = not all(last_status)
            index += 1
        return status[N]

    def getFactors(self, N):
        index = 1
        factors = []
        while index <= math.sqrt(N):
            if not N % index:
                factors.append(index)
            index += 1
        return factors

#
# if __name__ == '__main__':
#     s = Solution()
#     print s.divisorGame(4)  # True
#     print s.divisorGame(5)  # False
