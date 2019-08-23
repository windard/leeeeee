# coding=utf-8
#
# @lc app=leetcode id=840 lang=python
#
# [840] Magic Squares In Grid
#
# https://leetcode.com/problems/magic-squares-in-grid/description/
#
# algorithms
# Easy (36.00%)
# Likes:    85
# Dislikes: 725
# Total Accepted:    14.4K
# Total Submissions: 40K
# Testcase Example:  '[[4,3,8,4],[9,5,1,9],[2,7,6,2]]'
#
# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9
# such that each row, column, and both diagonals all have the same sum.
# 
# Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?
# (Each subgrid is contiguous).
# 
# 
# 
# Example 1:
# 
# 
# Input: [[4,3,8,4],
# ⁠       [9,5,1,9],
# ⁠       [2,7,6,2]]
# Output: 1
# Explanation: 
# The following subgrid is a 3 x 3 magic square:
# 438
# 951
# 276
# 
# while this one is not:
# 384
# 519
# 762
# 
# In total, there is only one magic square inside the given grid.
# 
# 
# Note:
# 
# 
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# 0 <= grid[i][j] <= 15
# 
# 
#


class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        for row in range(len(grid)-2):
            for column in range(len(grid[0])-2):
                if self.checkSquare(row, column, grid):
                    count += 1
        return count

    def checkSquare(self, row, column, grid):
        """
        must be 1-9
        """
        count = 15
        result = []
        for i in range(3):
            result.append(grid[row+i][column])
            result.append(grid[row+i][column+1])
            result.append(grid[row+i][column+2])
            if grid[row+i][column] + grid[row+i][column+1] + grid[row+i][column+2] != count:
                return False
            if grid[row][column+i] + grid[row+1][column+i] + grid[row+2][column+i] != count:
                return False
        if grid[row][column] + grid[row+1][column+1] + grid[row+2][column+2] != count:
            return False
        if grid[row+2][column] + grid[row+1][column+1] + grid[row][column+2] != count:
            return False
        return sorted(result) == range(1,10)


# if __name__ == '__main__':
#     s = Solution()
#     print s.numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]])
#     print s.numMagicSquaresInside([[1,1,1],[1,1,1],[1,1,1]])
#     print s.numMagicSquaresInside([[1,8,6],[10,5,0],[4,2,9]])
