# coding=utf-8
#
# @lc app=leetcode id=1128 lang=python
#
# [1128] Number of Equivalent Domino Pairs
#
# https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/
#
# algorithms
# Easy (44.33%)
# Likes:    67
# Dislikes: 36
# Total Accepted:    8.7K
# Total Submissions: 19.5K
# Testcase Example:  '[[1,2],[2,1],[3,4],[5,6]]'
#
# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] =
# [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is,
# one domino can be rotated to be equal to another domino.
# 
# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and
# dominoes[i] is equivalent to dominoes[j].
# 
# 
# Example 1:
# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1
# 
# 
# Constraints:
# 
# 
# 1 <= dominoes.length <= 40000
# 1 <= dominoes[i][j] <= 9
# 
#


class Solution(object):
    def _numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        # Time Limit
        count = 0
        for i in range(len(dominoes)-1):
            for j in range(i+1, len(dominoes)):
                if (dominoes[i][0] == dominoes[j][0] and dominoes[i][1] == dominoes[j][1]) or \
                        (dominoes[i][1] == dominoes[j][0] and dominoes[i][0] == dominoes[j][1]):
                    count += 1
        return count

    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        data = {}
        for domino in dominoes:
            value = '{}{}'.format(min(domino), max(domino))
            data[value] = data.get(value, 0) + 1

        count = 0
        for _, v in data.items():
            count += v * (v - 1) / 2

        return count

# if __name__ == '__main__':
#     s = Solution()
#     print s.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]])
