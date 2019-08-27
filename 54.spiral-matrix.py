# coding=utf-8
#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (29.64%)
# Likes:    1267
# Dislikes: 438
# Total Accepted:    254.5K
# Total Submissions: 819.2K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# Input:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
#


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        min_row = min_column = -1
        row_length = len(matrix)
        column_length = len(matrix[0])

        ri = 0
        ci = -1
        result = []
        # 1 从左往右
        # 2 从上往下
        # 3 从下往上
        # 4 从右往左
        redirect = 1
        while True:
            if redirect == 1:
                ci += 1
                if ci == column_length:
                    ci -= 1
                    redirect = 2
                    min_row += 1
                    if ci == min_column:
                        break
                    else:
                        continue

            elif redirect == 2:
                ri += 1
                if ri == row_length:
                    ri -= 1
                    redirect = 3
                    column_length -= 1
                    if ri == min_row:
                        break
                    else:
                        continue
            elif redirect == 3:
                ci -= 1
                if ci == min_column:
                    ci += 1
                    redirect = 4
                    row_length -= 1
                    if ci == column_length:
                        break
                    else:
                        continue

            else:
                ri -= 1
                if ri == min_row:
                    ri += 1
                    redirect = 1
                    min_column += 1
                    if ri == row_length:
                        break
                    else:
                        continue

            result.append(matrix[ri][ci])

        return result

#
# if __name__ == '__main__':
#     s = Solution()
#     print s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
#     print s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
