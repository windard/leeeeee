#
# @lc app=leetcode id=896 lang=python
#
# [896] Monotonic Array
#
# https://leetcode.com/problems/monotonic-array/description/
#
# algorithms
# Easy (54.45%)
# Total Accepted:    30.8K
# Total Submissions: 56.5K
# Testcase Example:  '[1,2,2,3]'
#
# An array is monotonic if it is either monotone increasing or monotone
# decreasing.
#
# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array
# A is monotone decreasing if for all i <= j, A[i] >= A[j].
#
# Return true if and only if the given array A is monotonic.
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
# Input: [1,2,2,3]
# Output: true
#
#
#
# Example 2:
#
#
# Input: [6,5,4,4]
# Output: true
#
#
#
# Example 3:
#
#
# Input: [1,3,2]
# Output: false
#
#
#
# Example 4:
#
#
# Input: [1,2,4,5]
# Output: true
#
#
#
# Example 5:
#
#
# Input: [1,1,1]
# Output: true
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 50000
# -100000 <= A[i] <= 100000
#
#
#
#
#
#
#
#
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        if len(A) <= 1:
            return True
        flag = 0
        temp = None

        for i in A:
            if flag == 0:
                if temp != None:
                    if i > temp:
                        flag = 1
                    elif i < temp:
                        flag = -1
                    else:
                        pass
            else:
                if (i >= temp and flag == 1) or (i <= temp and flag == -1):
                    pass
                else:
                    return False
            temp = i
        return True