# coding=utf-8
#
# @lc app=leetcode id=40 lang=python
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (40.20%)
# Likes:    859
# Dislikes: 47
# Total Accepted:    226.3K
# Total Submissions: 539K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sums to target.
# 
# Each number in candidates may only be used once in the combination.
# 
# Note:
# 
# 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
# [1,2,2],
# [5]
# ]
# 
# 
#


class Solution(object):
    def _combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        start = 0
        result = []
        counter_result = []
        from collections import Counter

        def inner_combine(s, p):
            if sum(p) == target:
                if Counter(p) not in counter_result:
                    result.append(p)
                    counter_result.append(Counter(p))
                return
            elif sum(p) > target:
                return

            for i in range(s, len(candidates)):
                inner_combine(i+1, p+[candidates[i]])

        inner_combine(start, [])
        return result

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        start = 0
        result = []
        candidates.sort()

        def inner_combine(s, p):
            if sum(p) == target:
                result.append(p)
                return
            elif sum(p) > target:
                return

            for i in range(s, len(candidates)):
                if i > s and candidates[i-1] == candidates[i]:
                    continue
                inner_combine(i+1, p+[candidates[i]])

        inner_combine(start, [])
        return result


# if __name__ == '__main__':
#     s = Solution()
#     print s.combinationSum2([10,1,2,7,6,1,5], 8)
#     print s.combinationSum2([2,5,2,1,2], 5)
#     print s.combinationSum2([2,2,2,2], 6)
#     print s.combinationSum2([1,2,2,2,2], 6)
