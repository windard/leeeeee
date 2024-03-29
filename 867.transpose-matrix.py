# coding=utf-8
#
# @lc app=leetcode id=867 lang=python
#
# [867] Transpose Matrix
#
# https://leetcode.com/problems/transpose-matrix/description/
#
# algorithms
# Easy (63.73%)
# Likes:    224
# Dislikes: 234
# Total Accepted:    52K
# Total Submissions: 81.2K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix A, return the transpose of A.
# 
# The transpose of a matrix is the matrix flipped over it's main diagonal,
# switching the row and column indices of the matrix.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# 
# 
# 
# Example 2:
# 
# 
# Input: [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 1000
# 1 <= A[0].length <= 1000
# 
# 
# 
# 
#


class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A:
            return []
        B = [[0]*len(A) for _ in range(len(A[0]))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                B[j][i] = A[i][j]
        return B
