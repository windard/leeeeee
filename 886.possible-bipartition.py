# coding=utf-8
#
# @lc app=leetcode id=886 lang=python
#
# [886] Possible Bipartition
#
# https://leetcode.com/problems/possible-bipartition/description/
#
# algorithms
# Medium (41.24%)
# Likes:    346
# Dislikes: 16
# Total Accepted:    16.2K
# Total Submissions: 39.1K
# Testcase Example:  '4\n[[1,2],[1,3],[2,4]]'
#
# Given a set of N people (numbered 1, 2, ..., N), we would like to split
# everyone into two groups of any size.
# 
# Each person may dislike some other people, and they should not go into the
# same group. 
# 
# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the
# people numbered a and b into the same group.
# 
# Return true if and only if it is possible to split everyone into two groups
# in this way.
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
# Example 1:
# 
# 
# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]
# 
# 
# 
# Example 2:
# 
# 
# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false
# 
# 
# 
# Example 3:
# 
# 
# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 2000
# 0 <= dislikes.length <= 10000
# 1 <= dislikes[i][j] <= N
# dislikes[i][0] < dislikes[i][1]
# There does not exist i != j for which dislikes[i] == dislikes[j].
# 
# 
# 
# 
# 
#

# @lc code=start
from collections import defaultdict

class Solution(object):
    def _possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        # Time Limit
        opposite = defaultdict(list)
        for dislike in dislikes:
            opposite[dislike[0]].append(dislike[1])
            opposite[dislike[1]].append(dislike[0])

        def match(num, red_set, blue_set):
            red_set.add(num)
            for o in opposite[num]:
                if o in red_set:
                    return False
                if o in blue_set:
                    continue
                if not match(o, blue_set, red_set):
                    return False
            return True

        for i in range(1, N+1):
            if not match(i, set(), set()):
                return False
        return True

        
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        # Time Limit
        opposite = defaultdict(list)
        for dislike in dislikes:
            opposite[dislike[0]].append(dislike[1])
            opposite[dislike[1]].append(dislike[0])

        def match(num, red_set, blue_set):
            red_set.add(num)
            for o in opposite[num]:
                if o in red_set:
                    return False
                if o in blue_set:
                    continue
                if not match(o, blue_set, red_set):
                    return False
            return True

        red = set()
        blue = set()
        for i in range(1, N+1):
            if i in blue:
                if not match(i, blue, red):
                    return False
            else:
                if not match(i, red, blue):
                    return False
        return True

        
# @lc code=end

