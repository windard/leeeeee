# coding=utf-8
#
# @lc app=leetcode id=73 lang=python
#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (40.54%)
# Likes:    1226
# Dislikes: 217
# Total Accepted:    230.1K
# Total Submissions: 566K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in-place.
# 
# Example 1:
# 
# 
# Input: 
# [
# [1,1,1],
# [1,0,1],
# [1,1,1]
# ]
# Output: 
# [
# [1,0,1],
# [0,0,0],
# [1,0,1]
# ]
# 
# 
# Example 2:
# 
# 
# Input: 
# [
# [0,1,2,0],
# [3,4,5,2],
# [1,3,1,5]
# ]
# Output: 
# [
# [0,0,0,0],
# [0,4,5,0],
# [0,3,1,0]
# ]
# 
# 
# Follow up:
# 
# 
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best
# solution.
# Could you devise a constant space solution?
# 
# 
#


class Solution(object):
    def _setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # 空间复杂度
        # O(m*n)
        from copy import deepcopy
        board = deepcopy(matrix)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    for x in range(len(board)):
                        matrix[x][j] = 0
                    for y in range(len(board[0])):
                        matrix[i][y] = 0

    def __setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # O(m+n)
        xs = []
        ys = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    xs.append(i)
                    ys.append(j)

        for i in range(len(matrix)):
            for y in ys:
                matrix[i][y] = 0
        for j in range(len(matrix[0])):
            for x in xs:
                matrix[x][j] = 0

    def ___setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        xs = set()
        ys = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    xs.add(i)
                    ys.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in xs or j in ys:
                    matrix[i][j] = 0

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # O(1) 的空间复杂度
        # 将该行或该列首位置零设为标志位
        if not matrix:
            return

        flag = [0, 0]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    if i == 0:
                        flag[0] = 1
                    if j == 0:
                        flag[1] = 1

        # 不能合二为一
        # [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        # Wrong Answer
        # 也不能全部遍历查找
        # 还是会重复
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[0][j] == 0 or matrix[i][0] == 0:
        #             matrix[i][j] = 0

        # 计算 第一行第一列的值
        # 先算横轴，除第一行
        # 再算竖轴，除第一列
        # 补充第一行第一列的值

        # 这下面👇两个可以合二为一
        for i in range(len(matrix)-1, 0, -1):
            for j in range(len(matrix[0])):
                if matrix[i][0] == 0:
                    matrix[i][j] = 0

        for j in range(len(matrix[0])-1, 0, -1):
            for i in range(len(matrix)):
                if matrix[0][j] == 0:
                    matrix[i][j] = 0

        if flag[0]:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if flag[1]:
            for i in range(len(matrix)):
                matrix[i][0] = 0

#
# if __name__ == '__main__':
#     s = Solution()
#     a = [[1,1,1],[1,0,1],[1,1,1]]
#     b = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
#     c = [[1,1,2,0],[3,4,5,2],[1,3,1,5]]
#     s.setZeroes(a)
#     s.setZeroes(b)
#     s.setZeroes(c)
#     print a
#     print b
#     print c
