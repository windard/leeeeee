# coding=utf-8
#
# @lc app=leetcode id=1013 lang=python
#
# [1013] Partition Array Into Three Parts With Equal Sum
#
# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/description/
#
# algorithms
# Easy (55.96%)
# Likes:    161
# Dislikes: 29
# Total Accepted:    17.2K
# Total Submissions: 30.7K
# Testcase Example:  '[0,2,1,-6,6,-7,9,1,2,0,1]'
#
# Given an array A of integers, return true if and only if we can partition the
# array into three non-empty parts with equal sums.
# 
# Formally, we can partition the array if we can find indexes i+1 < j with
# (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1]
# + ... + A[A.length - 1])
# 
# 
# 
# Example 1:
# 
# 
# Input: [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
# 
# 
# 
# Example 2:
# 
# 
# Input: [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false
# 
# 
# 
# Example 3:
# 
# 
# Input: [3,3,6,5,-2,2,5,1,-9,4]
# Output: true
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 3 <= A.length <= 50000
# -10000 <= A[i] <= 10000
# 
#


class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # 按题目的意思，似乎是已经将顺序排好了
        # 只需从前往后截断即可
        # 怪不得是 easy
        # 否则直接求的话，可以做 hard 题目
        if int(sum(A) / 3.0) != sum(A) / 3:
            return False
        target = sum(A) / 3
        count = 0
        for i in A:
            # 整形有正有负，不能按照大小比较
            # if count + i > target:
            #     return False
            # elif count + i == target:
            #     count = 0
            # else:
            #     count += i
            if count + i == target:
                count = 0
            else:
                count += i
        return count == 0


# if __name__ == '__main__':
#     s = Solution()
#     print s.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1])
#     print s.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1])
#     print s.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4])
