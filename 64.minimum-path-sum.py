# coding=utf-8
#
# @lc app=leetcode id=64 lang=python
#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (45.58%)
# Likes:    1536
# Dislikes: 42
# Total Accepted:    250.8K
# Total Submissions: 521.7K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.
# 
# Example:
# 
# 
# Input:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
# 
# 
#


class Solution(object):
    def _minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # DP Classical Algorithm
        dp = [[0]*len(grid[0]) for _ in range(len(grid))]
        for r in range(len(grid)):
            for w in range(len(grid[0])):
                if r > 0:
                    if w > 0:
                        dp[r][w] = min(dp[r-1][w], dp[r][w-1]) + grid[r][w]
                    else:
                        dp[r][w] = dp[r-1][w] + grid[r][w]
                else:
                    if w > 0:
                        dp[r][w] = dp[r][w-1] + grid[r][w]
                    else:
                        dp[r][w] = grid[r][w]
        # for d in dp:
        #     print d

        return dp[-1][-1]

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # DP Classical Algorithm
        for r in range(len(grid)):
            for w in range(len(grid[0])):
                if r > 0:
                    if w > 0:
                        grid[r][w] = min(grid[r-1][w], grid[r][w-1]) + grid[r][w]
                    else:
                        grid[r][w] = grid[r-1][w] + grid[r][w]
                else:
                    if w > 0:
                        grid[r][w] = grid[r][w-1] + grid[r][w]
                    else:
                        grid[r][w] = grid[r][w]
        # for d in grid:
        #     print d

        return grid[-1][-1]

# if __name__ == '__main__':
#     s = Solution()
#     print s.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
