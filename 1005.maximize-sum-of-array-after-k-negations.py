# coding=utf-8
#
# @lc app=leetcode id=1005 lang=python
#
# [1005] Maximize Sum Of Array After K Negations
#
# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/
#
# algorithms
# Easy (50.02%)
# Likes:    124
# Dislikes: 20
# Total Accepted:    14.1K
# Total Submissions: 28.2K
# Testcase Example:  '[4,2,3]\n1'
#
# Given an array A of integers, we must modify the array in the following way:
# we choose an i and replace A[i] with -A[i], and we repeat this process K
# times in total.  (We may choose the same index i multiple times.)
# 
# Return the largest possible sum of the array after modifying it in this
# way.
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [4,2,3], K = 1
# Output: 5
# Explanation: Choose indices (1,) and A becomes [4,-2,3].
# 
# 
# 
# Example 2:
# 
# 
# Input: A = [3,-1,0,2], K = 3
# Output: 6
# Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].
# 
# 
# 
# Example 3:
# 
# 
# Input: A = [2,-3,-1,5,-4], K = 2
# Output: 13
# Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 10000
# 1 <= K <= 10000
# -100 <= A[i] <= 100
# 
# 
#


class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        nega = sorted([i for i in A if i < 0])
        posi = sorted([i for i in A if i >= 0])
        if nega:
            if len(nega) > K:
                return sum(posi) + abs(sum(nega[:K])) + sum(nega[K:])
            else:
                posi += [-n for n in nega]
                K = K - len(nega)
                posi.sort()
        K = K % 2
        return sum(posi[K:]) - sum(posi[:K])
