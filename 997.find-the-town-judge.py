# coding=utf-8
#
# @lc app=leetcode id=997 lang=python
#
# [997] Find the Town Judge
#
# https://leetcode.com/problems/find-the-town-judge/description/
#
# algorithms
# Easy (47.99%)
# Likes:    205
# Dislikes: 29
# Total Accepted:    23.2K
# Total Submissions: 46.9K
# Testcase Example:  '2\n[[1,2]]'
#
# In a town, there are N people labelled from 1 to N.  There is a rumor that
# one of these people is secretly the town judge.
# 
# If the town judge exists, then:
# 
# 
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# 
# 
# You are given trust, an array of pairs trust[i] = [a, b] representing that
# the person labelled a trusts the person labelled b.
# 
# If the town judge exists and can be identified, return the label of the town
# judge.  Otherwise, return -1.
# 
# 
# 
# Example 1:
# 
# 
# Input: N = 2, trust = [[1,2]]
# Output: 2
# 
# 
# 
# Example 2:
# 
# 
# Input: N = 3, trust = [[1,3],[2,3]]
# Output: 3
# 
# 
# 
# Example 3:
# 
# 
# Input: N = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
# 
# 
# 
# Example 4:
# 
# 
# Input: N = 3, trust = [[1,2],[2,3]]
# Output: -1
# 
# 
# 
# Example 5:
# 
# 
# Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# Output: 3
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 1000
# trust.length <= 10000
# trust[i] are all different
# trust[i][0] != trust[i][1]
# 1 <= trust[i][0], trust[i][1] <= N
# 
# 
#


class Solution(object):
    def _findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        coins = [0]*N
        for relation in trust:
            coins[relation[0]-1] -= 1
            coins[relation[1]-1] += 1
        for index, coin in enumerate(coins):
            if coin == N - 1:
                return index+1
        return -1

    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        coins = dict(zip(range(1, N+1), [0]*N))
        for relation in trust:
            coins[relation[0]] = coins.get(relation[0]) - 1
            coins[relation[1]] = coins.get(relation[1]) + 1
        for index, coin in coins.items():
            if coin == N - 1:
                return index
        return -1


# if __name__ == '__main__':
#     s = Solution()
#     print s.findJudge(2, [[1,2]])
#     print s.findJudge(3, [[1,3],[2,3]])
#     print s.findJudge(3, [[1,3],[2,3],[3,1]])
#     print s.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]])
