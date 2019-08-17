# coding=utf-8
#
# @lc app=leetcode id=1037 lang=python
#
# [1037] Valid Boomerang
#
# https://leetcode.com/problems/valid-boomerang/description/
#
# algorithms
# Easy (37.69%)
# Likes:    41
# Dislikes: 134
# Total Accepted:    9.1K
# Total Submissions: 24.2K
# Testcase Example:  '[[1,1],[2,3],[3,2]]'
#
# A boomerang is a set of 3 points that are all distinct and not in a straight
# line.
# 
# Given a list of three points in the plane, return whether these points are a
# boomerang.
# 
# 
# 
# Example 1:
# 
# 
# Input: [[1,1],[2,3],[3,2]]
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: [[1,1],[2,2],[3,3]]
# Output: false
# 
# 
# 
# 
# Note:
# 
# 
# points.length == 3
# points[i].length == 2
# 0 <= points[i][j] <= 100
# 
# 
# 
# 
# 
#


class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        A, B, C = points
        if A == B or A == C or B == C:
            return False
        if A[1]-B[1] == 0:
            ver_a = float("inf")
        else:
            ver_a = float(A[0]-B[0])/float(A[1]-B[1])
        if B[1]-C[1] == 0:
            ver_b = float("inf")
        else:
            ver_b = float(B[0] - C[0]) / float(B[1] - C[1])
        if ver_a == ver_b:
            return False
        else:
            return True


# if __name__ == '__main__':
#     s = Solution()
#     print s.isBoomerang([[0,0],[1,1],[1,1]])
#     print s.isBoomerang([[1,1],[2,3],[3,2]])
#     print s.isBoomerang([[1,1],[2,2],[3,3]])
#     print s.isBoomerang([[0,0],[1,0],[2,2]])
#     print s.isBoomerang([[0,1],[0,2],[1,2]])
