# coding=utf-8
#
# @lc app=leetcode id=48 lang=python
#
# [48] Rotate Image
#
# https://leetcode.com/problems/rotate-image/description/
#
# algorithms
# Medium (46.86%)
# Likes:    1782
# Dislikes: 164
# Total Accepted:    276.3K
# Total Submissions: 553.2K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# You are given an n x n 2D matrix representing an image.
# 
# Rotate the image by 90 degrees (clockwise).
# 
# Note:
# 
# You have to rotate the image in-place, which means you have to modify the
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the
# rotation.
# 
# Example 1:
# 
# 
# Given input matrix = 
# [
# ⁠ [1,2,3],
# ⁠ [4,5,6],
# ⁠ [7,8,9]
# ],
# 
# rotate the input matrix in-place such that it becomes:
# [
# ⁠ [7,4,1],
# ⁠ [8,5,2],
# ⁠ [9,6,3]
# ]
# 
# 
# Example 2:
# 
# 
# Given input matrix =
# [
# ⁠ [ 5, 1, 9,11],
# ⁠ [ 2, 4, 8,10],
# ⁠ [13, 3, 6, 7],
# ⁠ [15,14,12,16]
# ], 
# 
# rotate the input matrix in-place such that it becomes:
# [
# ⁠ [15,13, 2, 5],
# ⁠ [14, 3, 4, 1],
# ⁠ [12, 6, 8, 9],
# ⁠ [16, 7,10,11]
# ]
# 
# 
#


class Solution(object):
    def _rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        from copy import deepcopy
        board = deepcopy(matrix)

        if not matrix:
            return

        n = len(matrix)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = board[n-1-j][i]

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # 先转置
        # 再逆序
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for ma in matrix:
            ma.reverse()


# if __name__ == '__main__':
#     s = Solution()
#     matrix = [
#         [1,2,3],
#         [4,5,6],
#         [7,8,9]
#     ]
#     s.rotate(matrix)
#     print matrix
