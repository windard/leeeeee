#
# @lc app=leetcode id=977 lang=python
#
# [977] Squares of a Sorted Array
#
# https://leetcode.com/problems/squares-of-a-sorted-array/description/
#
# algorithms
# Easy (71.83%)
# Likes:    427
# Dislikes: 46
# Total Accepted:    95.7K
# Total Submissions: 133.3K
# Testcase Example:  '[-4,-1,0,3,10]'
#
# Given an array of integers A sorted in non-decreasing order, return an array
# of the squares of each number, also in sorted non-decreasing order.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# 
# 
# 
# Example 2:
# 
# 
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A is sorted in non-decreasing order.
# 
# 
# 
#
class Solution(object):
    def _sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted(map(lambda x:x*x, A))

    def __sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A = sorted(map(abs, A))
        return [x*x for x in A]

    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        start = 0
        end = len(A) - 1
        newA = []
        while start <= end:
            if abs(A[start]) >= abs(A[end]):
                newA.insert(0, abs(A[start]))
                start += 1
            else:
                newA.insert(0, abs(A[end]))
                end -= 1
        return [x*x for x in newA]
