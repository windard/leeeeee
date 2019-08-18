# coding=utf-8
#
# @lc app=leetcode id=922 lang=python
#
# [922] Sort Array By Parity II
#
# https://leetcode.com/problems/sort-array-by-parity-ii/description/
#
# algorithms
# Easy (67.22%)
# Likes:    327
# Dislikes: 32
# Total Accepted:    53.2K
# Total Submissions: 79.2K
# Testcase Example:  '[4,2,5,7]'
#
# Given an array A of non-negative integers, half of the integers in A are odd,
# and half of the integers are even.
# 
# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is
# even, i is even.
# 
# You may return any answer array that satisfies this condition.
# 
# 
# 
# Example 1:
# 
# 
# Input: [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been
# accepted.
# 
# 
# 
# 
# Note:
# 
# 
# 2 <= A.length <= 20000
# A.length % 2 == 0
# 0 <= A[i] <= 1000
# 
# 
# 
# 
# 
#


class Solution(object):
    def _sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = filter(lambda x: x % 2, A)
        even = filter(lambda x: not x % 2, A)
        result = []
        while odd and even:
            result.append(even.pop())
            result.append(odd.pop())
        return result

    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A:
            return A
        even = 0
        odd = 1
        while even < len(A) and odd < len(A):
            while not A[even] % 2:
                even += 2
                if even >= len(A):
                    return A
            while A[odd] % 2:
                odd += 2
                if odd >= len(A):
                    return A
            A[odd], A[even] = A[even], A[odd]


# if __name__ == '__main__':
#     s = Solution()
#     print s.sortArrayByParityII([4,2,5,7])
