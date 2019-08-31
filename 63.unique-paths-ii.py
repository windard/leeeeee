# coding=utf-8
#
# @lc app=leetcode id=63 lang=python
#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (33.22%)
# Likes:    950
# Dislikes: 153
# Total Accepted:    216.2K
# Total Submissions: 643.1K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# Now consider if some obstacles are added to the grids. How many unique paths
# would there be?
# 
# 
# 
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# 
# Note: m and n will be at most 100.
# 
# Example 1:
# 
# 
# Input:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# 
# 
#


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # 动态规划 + 条件判断
        # 太过分了，石头放在入口，或者出口的位置
        # 这不是故意找茬的么
        if not obstacleGrid:
            return 0
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        route = [[0] * m for _ in range(n)]
        if not obstacleGrid[0][0]:
            route[0][0] = 1

        for i in range(n):
            for j in range(m):
                t = 0
                if i > 0:
                    t += not obstacleGrid[i-1][j] and route[i-1][j]
                if j > 0:
                    t += not obstacleGrid[i][j-1] and route[i][j-1]
                route[i][j] += t
        return route[-1][-1] if not obstacleGrid[-1][-1] else 0


# if __name__ == '__main__':
#     s = Solution()
#     print s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
