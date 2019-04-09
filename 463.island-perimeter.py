#
# @lc app=leetcode id=463 lang=python
#
# [463] Island Perimeter
#
# https://leetcode.com/problems/island-perimeter/description/
#
# algorithms
# Easy (60.31%)
# Total Accepted:    127.3K
# Total Submissions: 210.1K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# You are given a map in form of a two-dimensional integer grid where 1
# represents land and 0 represents water.
# 
# Grid cells are connected horizontally/vertically (not diagonally). The grid
# is completely surrounded by water, and there is exactly one island (i.e., one
# or more connected land cells).
# 
# The island doesn't have "lakes" (water inside that isn't connected to the
# water around the island). One cell is a square with side length 1. The grid
# is rectangular, width and height don't exceed 100. Determine the perimeter of
# the island.
# 
# 
# 
# Example:
# 
# 
# Input:
# [[0,1,0,0],
# ⁠[1,1,1,0],
# ⁠[0,1,0,0],
# ⁠[1,1,0,0]]
# 
# Output: 16
# 
# Explanation: The perimeter is the 16 yellow stripes in the image below:
# 
# 
# 
# 
#

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Surround By Zero
        
        for g in grid:
            g.append(0)
            g.insert(0, 0)
        grid.insert(0, [0]*len(grid[0]))
        grid.append([0]*len(grid[-1]))
        
        s = 0
        width = len(grid[0])
        height = len(grid)

        for i in range(1, height-1):
            for j in range(1, width-1):
                if grid[i][j] == 1:
                    # print i,j, self.checkSurround(grid, i, j)
                    s += self.checkSurround(grid, i, j)
        
        return s
    
    def checkSurround(self, grid, i, j):
        s = 0
        if grid[i+1][j] == 0:
            s += 1
        if grid[i-1][j] == 0:
            s += 1
        if grid[i][j+1] == 0:
            s += 1
        if grid[i][j-1] == 0:
            s += 1
        return s

# if __name__ == "__main__":
#     s = Solution()
#     print s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])