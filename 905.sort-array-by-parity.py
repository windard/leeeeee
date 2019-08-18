# coding=utf-8
#
# @lc app=leetcode id=905 lang=python
#
# [905] Sort Array By Parity
#
# https://leetcode.com/problems/sort-array-by-parity/description/
#
# algorithms
# Easy (72.17%)
# Likes:    526
# Dislikes: 58
# Total Accepted:    117.8K
# Total Submissions: 162.1K
# Testcase Example:  '[3,1,2,4]'
#
# Given an array A of non-negative integers, return an array consisting of all
# the even elements of A, followed by all the odd elements of A.
# 
# You may return any answer array that satisfies this condition.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000
# 
# 
# 
#


class Solution(object):
    def _sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # 题目理解错误
        # 奇偶分离而已
        result = []
        odd = []
        even = []
        need = False
        for n in A:
            if n % 2:
                if need:
                    result.append(n)
                    need = False
                else:
                    if even:
                        result.append(even.pop())
                        result.append(n)
                    else:
                        odd.append(n)
            else:
                if not need:
                    result.append(n)
                    need = True
                else:
                    if odd:
                        result.append(odd.pop())
                        result.append(n)
                    else:
                        even.append(n)
        while True:
            if need:
                if odd:
                    result.append(odd.pop())
                need = False
            else:
                if even:
                    result.append(even.pop())
                    need = True
                else:
                    break
        return result

    def _sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = filter(lambda x: x % 2, A)
        even = filter(lambda x: not x % 2, A)
        return even + odd

    def _sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        index = 0
        length = len(A)
        count = 0
        while count < length:
            if A[index] % 2:
                A.append(A.pop(index))
                count += 1
            else:
                index += 1
                count += 1
        return A

    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # Double Point
        start = 0
        end = len(A) - 1
        while start < end:
            while not A[start] % 2:
                start += 1
                if start >= len(A):
                    return A
            while A[end] % 2:
                end -= 1
                if end < 0:
                    return A
            if start > end:
                break
            A[start], A[end] = A[end], A[start]
            # start += 1
            # end -= 1
        return A


# if __name__ == '__main__':
#     s = Solution()
#     print s.sortArrayByParity([3,1,2,4])
    # print s.sortArrayByParity([0,2])
