# coding=utf-8
#
# @lc app=leetcode id=289 lang=python
#
# [289] Game of Life
#
# https://leetcode.com/problems/game-of-life/description/
#
# algorithms
# Medium (47.01%)
# Likes:    1165
# Dislikes: 215
# Total Accepted:    135.4K
# Total Submissions: 279K
# Testcase Example:  '[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]'
#
# According to the Wikipedia's article: "The Game of Life, also known simply as
# Life, is a cellular automaton devised by the British mathematician John
# Horton Conway in 1970."
# 
# Given a board with m by n cells, each cell has an initial state live (1) or
# dead (0). Each cell interacts with its eight neighbors (horizontal, vertical,
# diagonal) using the following four rules (taken from the above Wikipedia
# article):
# 
# 
# Any live cell with fewer than two live neighbors dies, as if caused by
# under-population.
# Any live cell with two or three live neighbors lives on to the next
# generation.
# Any live cell with more than three live neighbors dies, as if by
# over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by
# reproduction.
# 
# 
# Write a function to compute the next state (after one update) of the board
# given its current state. The next state is created by applying the above
# rules simultaneously to every cell in the current state, where births and
# deaths occur simultaneously.
# 
# Example:
# 
# 
# Input: 
# [
# [0,1,0],
# [0,0,1],
# [1,1,1],
# [0,0,0]
# ]
# Output: 
# [
# [0,0,0],
# [1,0,1],
# [0,1,1],
# [0,1,0]
# ]
# 
# 
# Follow up:
# 
# 
# Could you solve it in-place? Remember that the board needs to be updated at
# the same time: You cannot update some cells first and then use their updated
# values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the
# board is infinite, which would cause problems when the active area encroaches
# the border of the array. How would you address these problems?
# 
# 
#

# @lc code=start
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        state_transfer = [[0, 0, 0, 1, 0, 0, 0, 0, 0],
                          [0, 0, 1, 1, 0, 0, 0, 0, 0]]
        last_row = []
        for i in range(len(board)):
            current_row = board[i][::]
            next_row = []
            if i < len(board) - 1:
                next_row = board[i + 1][::]
            for j in range(len(board[0])):
                board[i][j] = state_transfer[board[i][j]][
                    self.right_calculate(last_row, current_row, next_row, j)]
            last_row = current_row

    def calculate(self, last_row, current_row, next_row, j):
        # Wrong Calculate
        result = 0
        if last_row:
            if j - 1 >= 0:
                result += last_row[j - 1]
                result += current_row[j - 1]
            result += last_row[j]
            if j + 1 < len(current_row):
                result += last_row[j + 1]
                result += current_row[j + 1]
        if next_row:
            if j - 1 >= 0:
                result += next_row[j - 1]
            result += next_row[j]
            if j + 1 < len(current_row):
                result += next_row[j + 1]
        return result

    def right_calculate(self, last_row, current_row, next_row, j):
        result = 0
        if j - 1 >= 0:
            if last_row:
                result += last_row[j-1]
            result += current_row[j-1]
            if next_row:
                result += next_row[j-1]
        if last_row:
            result += last_row[j]
        if next_row:
            result += next_row[j]
        if j + 1 < len(current_row):
            if last_row:
                result += last_row[j+1]
            result += current_row[j+1]
            if next_row:
                result += next_row[j+1]
        return result

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print s.gameOfLife([[1,1],[1,0]])