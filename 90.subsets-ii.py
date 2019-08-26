# coding=utf-8
#
# @lc app=leetcode id=90 lang=python
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (41.46%)
# Likes:    996
# Dislikes: 50
# Total Accepted:    215.8K
# Total Submissions: 499.3K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
# 
#


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        start = 0
        e = len(nums)
        result = []
        nums.sort()

        def backtrack(s, p):
            result.append(p)

            for i in range(s, e):
                if i > s and nums[i-1] == nums[i]:
                    continue
                backtrack(i+1, p+[nums[i]])

        backtrack(start, [])
        return result


# if __name__ == '__main__':
#     s = Solution()
#     print s.subsetsWithDup([1,2,2])
