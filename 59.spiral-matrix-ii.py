# coding=utf-8
#
# @lc app=leetcode id=59 lang=python
#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (45.37%)
# Likes:    517
# Dislikes: 85
# Total Accepted:    144.6K
# Total Submissions: 302.9K
# Testcase Example:  '3'
#
# Given a positive integer n, generate a square matrix filled with elements
# from 1 to n^2 in spiral order.
# 
# Example:
# 
# 
# Input: 3
# Output:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
# 
# 
#


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in range(n)]
        index = 1

        row = col = 0
        row_max = col_max = n
        row_min = col_min = -1
        flag = 1
        while index <= n*n:
            matrix[row][col] = index
            if flag == 1:
                col += 1
                if col == col_max:
                    flag = 2
                    col -= 1
                    row_min += 1
                    continue
            elif flag == 2:
                row += 1
                if row == row_max:
                    flag = 3
                    row -= 1
                    col_max -= 1
                    continue
            elif flag == 3:
                col -= 1
                if col == col_min:
                    flag = 4
                    col += 1
                    row_max -= 1
                    continue
            elif flag == 4:
                row -= 1
                if row == row_min:
                    flag = 1
                    row += 1
                    col_min += 1
                    continue
            index += 1

        return matrix


# if __name__ == '__main__':
#     s = Solution()
#     print s.generateMatrix(3)
#     print s.generateMatrix(4)
