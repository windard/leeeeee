# coding=utf-8
#
# @lc app=leetcode id=74 lang=python
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (35.11%)
# Likes:    958
# Dislikes: 113
# Total Accepted:    241.6K
# Total Submissions: 687.9K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# 
# 
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
# 
# 
# Example 1:
# 
# 
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 13
# Output: false
# 
#


class Solution(object):
    def _searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 判断 target 在哪一行
        # 如果大于的话，需要使用上一行的第一个值进行比较，结果是在上一行
        # 如果大于的话，需要使用本行的最后一个值进行比较，结果是在本行内
        if not matrix or not matrix[0]:
            return False
        if len(matrix) > 1:
            # 双重二分查找
            start = 0
            end = len(matrix) - 1
            flag = -1
            while start <= end:
                mid = (start + end) / 2
                if matrix[mid][0] == target:
                    return True
                elif matrix[mid][0] > target:
                    if mid and matrix[mid-1][0] < target:
                        flag = mid - 1
                        break
                    end = mid - 1
                else:
                    # if mid < len(matrix)-1 and matrix[mid+1][0] > target:
                    if matrix[mid][-1] >= target:
                        flag = mid
                        break
                    start = mid + 1

            if flag < 0:
                return False
        else:
            # 单重二分查找
            flag = 0

        start = 0
        end = len(matrix[flag]) - 1
        while start <= end:
            mid = (start + end) / 2
            if matrix[flag][mid] == target:
                return True
            elif matrix[flag][mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False

    def __searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 还有更牛逼的，将二维数组直接当成一维数组来二分查找
        # 或者将二维数组转成一维数组来查找
        if not matrix:
            return False
        matrix = reduce(lambda x, y: x + y, matrix)
        start = 0
        end = len(matrix) - 1
        while start <= end:
            mid = (start + end) / 2
            if matrix[mid] == target:
                return True
            elif matrix[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 直接按照二维数组计算二分
        if not matrix:
            return False
        m = len(matrix[0])
        n = len(matrix)
        end = m * n - 1
        start = 0
        while start <= end:
            mid = (start + end) / 2
            i = mid / m
            j = mid % m
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False


# if __name__ == '__main__':
#     s = Solution()
#     print s.searchMatrix([[1,3]], 3)
#     print s.searchMatrix([[1,2,3], [4,5,6]], 3)
#     print s.searchMatrix([[1,2,3], [4,5,6]], 6)
#     print s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3)
#     print s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 13)
#     print s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 30)
