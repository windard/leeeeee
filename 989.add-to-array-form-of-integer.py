# coding=utf-8
#
# @lc app=leetcode id=989 lang=python
#
# [989] Add to Array-Form of Integer
#
# https://leetcode.com/problems/add-to-array-form-of-integer/description/
#
# algorithms
# Easy (44.95%)
# Likes:    151
# Dislikes: 28
# Total Accepted:    20.3K
# Total Submissions: 45.8K
# Testcase Example:  '[1,2,0,0]\n34'
#
# For a non-negative integer X, the array-form of X is an array of its digits
# in left to right order.  For example, if X = 1231, then the array form is
# [1,2,3,1].
# 
# Given the array-form A of a non-negative integer X, return the array-form of
# the integer X+K.
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
# Input: A = [1,2,0,0], K = 34
# Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234
# 
# 
# 
# Example 2:
# 
# 
# Input: A = [2,7,4], K = 181
# Output: [4,5,5]
# Explanation: 274 + 181 = 455
# 
# 
# 
# Example 3:
# 
# 
# Input: A = [2,1,5], K = 806
# Output: [1,0,2,1]
# Explanation: 215 + 806 = 1021
# 
# 
# 
# Example 4:
# 
# 
# Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
# Output: [1,0,0,0,0,0,0,0,0,0,0]
# Explanation: 9999999999 + 1 = 10000000000
# 
# 
# 
# 
# Note：
# 
# 
# 1 <= A.length <= 10000
# 0 <= A[i] <= 9
# 0 <= K <= 10000
# If A.length > 1, then A[0] != 0
# 
# 
# 
# 
# 
#


class Solution(object):
    def _addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        return map(int, list(str(int(''.join(map(str, A))) + K)))

    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        proportion = 10
        result = []
        supply = 0
        index = len(A)-1
        while index >= 0 or K:
            if index >= 0:
                i = A[index]
            else:
                i = 0
            K, c = divmod(K, proportion)
            supply, last = divmod(i+c+supply, proportion)
            result.insert(0, last)
            index -= 1
        if supply:
            result.insert(0, supply)
        return result


# if __name__ == '__main__':
#     s = Solution()
#     print s.addToArrayForm([0], 23)
#     print s.addToArrayForm([1,2,0,0], 34)
#     print s.addToArrayForm([2,7,4], 181)
#     print s.addToArrayForm([2,1,5], 806)
#     print s.addToArrayForm([9,9,9,9,9,9,9,9,9,9], 1)
