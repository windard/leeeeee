# coding=utf-8
#
# @lc app=leetcode id=941 lang=python
#
# [941] Valid Mountain Array
#
# https://leetcode.com/problems/valid-mountain-array/description/
#
# algorithms
# Easy (35.41%)
# Likes:    176
# Dislikes: 47
# Total Accepted:    24.7K
# Total Submissions: 69.9K
# Testcase Example:  '[2,1]'
#
# Given an array A of integers, return true if and only if it is a valid
# mountain array.
# 
# Recall that A is a mountain array if and only if:
# 
# 
# A.length >= 3
# There exists some i with 0 < i < A.length - 1 such that:
# 
# A[0] < A[1] < ... A[i-1] < A[i] 
# A[i] > A[i+1] > ... > A[A.length - 1]
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [2,1]
# Output: false
# 
# 
# 
# Example 2:
# 
# 
# Input: [3,5,5]
# Output: false
# 
# 
# 
# Example 3:
# 
# 
# Input: [0,3,2,1]
# Output: true
# 
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#


class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False
        if A[0] >= A[1]:
            return False
        if A[-2] <= A[-1]:
            return False
        flag = True
        index = 1
        while index < len(A):
            if A[index-1] < A[index]:
                if not flag:
                    return False
            elif A[index-1] > A[index]:
                if flag:
                    flag = False
            else:
                return False
            index += 1
        return True


# if __name__ == '__main__':
#     s = Solution()
#     print s.validMountainArray([2,1])
#     print s.validMountainArray([3,5,5])
#     print s.validMountainArray([0,3,2,1])
#     print s.validMountainArray([1,2,3])
#     print s.validMountainArray([3,2,1])
#     print s.validMountainArray([1,2,3,5,4,3,6,8])
#     print s.validMountainArray([0,3,2,1])
