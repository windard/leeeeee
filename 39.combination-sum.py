# coding=utf-8
#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (46.76%)
# Likes:    2076
# Dislikes: 63
# Total Accepted:    352.6K
# Total Submissions: 720.1K
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given a set of candidate numbers (candidates) (without duplicates) and a
# target number (target), find all unique combinations in candidates where the
# candidate numbers sums to target.
# 
# The same repeated number may be chosen from candidates unlimited number of
# times.
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
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
# 
#


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        start = 0
        result = []

        def inner_combine(s, p):
            if sum(p) == target:
                result.append(p)
                return
            elif sum(p) > target:
                return

            # 不能用 for i,v in enumerate(candidates[2:])
            # i 会一直为0，而不是从指定位置开始
            for i in range(s, len(candidates)):
                inner_combine(i, p+[candidates[i]])

        inner_combine(start, [])
        return result


# if __name__ == '__main__':
#     s = Solution()
    # print s.combinationSum([2,3,6,7], 7)
    # print s.combinationSum([2,3,5], 8)
    # print s.combinationSum([2,3,5], 8)
