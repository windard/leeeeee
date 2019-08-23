# coding=utf-8
#
# @lc app=leetcode id=994 lang=python
#
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Easy (46.55%)
# Likes:    327
# Dislikes: 21
# Total Accepted:    16K
# Total Submissions: 34.5K
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# In a given grid, each cell can have one of three values:
# 
# 
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# 
# 
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten
# orange becomes rotten.
# 
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange.  If this is impossible, return -1 instead.
# 
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# 
# 
# 
# Example 2:
# 
# 
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
# 
# 
# 
# Example 3:
# 
# 
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the
# answer is just 0.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.
# 
# 
# 
# 
#
import copy


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # same with @999
        index = 0
        while True:
            if self.checkRotting(grid):
                return index
            new_grid = self.rotting(grid)
            if new_grid == grid:
                return -1
            grid = new_grid
            index += 1

    def rotting(self, grid):
        new_grid = copy.deepcopy(grid)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    if r > 0:
                        if grid[r-1][c] == 1:
                            new_grid[r-1][c] = 2
                    if c > 0:
                        if grid[r][c-1] == 1:
                            new_grid[r][c-1] = 2
                    if r < len(grid) - 1:
                        if grid[r+1][c] == 1:
                            new_grid[r+1][c] = 2
                    if c < len(grid[0]) - 1:
                        if grid[r][c+1] == 1:
                            new_grid[r][c+1] = 2
        return new_grid

    def checkRotting(self, grid):
        """
        if no fresh orange return True
        :param grid:
        :return:
        """
        return all([all(map(lambda x:x != 1, g)) for g in grid])


# if __name__ == '__main__':
#     s = Solution()
#     print s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
#     print s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
#     print s.orangesRotting([[0,2]])
