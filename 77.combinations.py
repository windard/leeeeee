# coding=utf-8
#
# @lc app=leetcode id=77 lang=python
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (46.06%)
# Likes:    790
# Dislikes: 47
# Total Accepted:    206.9K
# Total Submissions: 430.4K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
# 
# Example:
# 
# 
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 
#


class Solution(object):
    def _combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        from itertools import combinations
        return combinations(range(1, n+1), k)

    def combine(self, n, k):
        start = 1
        n += 1
        result = []

        def inner_combine(s, e, p):
            if e == 0:
                result.append(p)
                return

            for i in range(s, n):
                inner_combine(i+1, e-1, p+[i])

        inner_combine(start, k, [])
        return result

    def combinations_with_replacement(self, n, k):
        start = 1
        n += 1
        result = []

        def inner_combine(s, e, p):
            if e == 0:
                result.append(p)
                return

            for i in range(s, n):
                inner_combine(i, e-1, p+[i])

        inner_combine(start, k, [])
        return result


# if __name__ == '__main__':
#     s = Solution()
#     print s.combine(4, 2)
#     print s.combinations_with_replacement(4, 2)
