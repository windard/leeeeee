# coding=utf-8
#
# @lc app=leetcode id=62 lang=python
#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (46.42%)
# Likes:    1788
# Dislikes: 124
# Total Accepted:    316.5K
# Total Submissions: 650.7K
# Testcase Example:  '3\n2'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# How many possible unique paths are there?
# 
# 
# Above is a 7 x 3 grid. How many possible unique paths are there?
# 
# Note: m and n will be at most 100.
# 
# Example 1:
# 
# 
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the
# bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# 
# 
# Example 2:
# 
# 
# Input: m = 7, n = 3
# Output: 28
# 
#


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # DFS|BFS
        # 回溯剪枝
        # 动态规划
        # 贪心算法
        route = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                t = 0
                if i > 0:
                    t += route[i-1][j]
                if j > 0:
                    t += route[i][j-1]
                route[i][j] = t or 1
        return route[-1][-1]


# if __name__ == '__main__':
#     s = Solution()
#     print s.uniquePaths(3,2)
#     print s.uniquePaths(7,3)
