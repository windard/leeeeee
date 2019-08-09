#
# @lc app=leetcode id=976 lang=python
#
# [976] Largest Perimeter Triangle
#
# https://leetcode.com/problems/largest-perimeter-triangle/description/
#
# algorithms
# Easy (56.89%)
# Likes:    178
# Dislikes: 24
# Total Accepted:    18.8K
# Total Submissions: 33.1K
# Testcase Example:  '[2,1,2]'
#
# Given an array A of positive lengths, return the largest perimeter of a
# triangle with non-zero area, formed from 3 of these lengths.
# 
# If it is impossible to form any triangle of non-zero area, return 0.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [2,1,2]
# Output: 5
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,1]
# Output: 0
# 
# 
# 
# Example 3:
# 
# 
# Input: [3,2,3,4]
# Output: 10
# 
# 
# 
# Example 4:
# 
# 
# Input: [3,6,2,3]
# Output: 8
# 
# 
# 
# 
# Note:
# 
# 
# 3 <= A.length <= 10000
# 1 <= A[i] <= 10^6
# 
# 
# 
# 
# 
#

from itertools import combinations


class Solution(object):
    def _largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # Time Limit
        max_length = 0
        for line in combinations(A, 3):
            if sum(line) - max(line) <= max(line):
                continue
            if sum(line) > max_length:
                max_length = sum(line)
        return max_length

    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        for i in range(len(A)-3, -1, -1):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0
