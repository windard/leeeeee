# coding=utf-8
#
# @lc app=leetcode id=216 lang=python
#
# [216] Combination Sum III
#
# https://leetcode.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (52.54%)
# Likes:    674
# Dislikes: 34
# Total Accepted:    131.7K
# Total Submissions: 249.9K
# Testcase Example:  '3\n7'
#
# 
# Find all possible combinations of k numbers that add up to a number n, given
# that only numbers from 1 to 9 can be used and each combination should be a
# unique set of numbers.
# 
# Note:
# 
# 
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# 
# 
# Example 2:
# 
# 
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
# 
# 
#


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        start = 1
        length = k
        target = n
        result = []

        def backtrack(s, l, p):
            if l == 0:
                if sum(p) == target:
                    result.append(p)
                return

            for i in range(s, 10):
                backtrack(i+1, l-1, p+[i])

        backtrack(start, length, [])
        return result


# if __name__ == '__main__':
#     s = Solution()
#     print s.combinationSum3(3,7)
#     print s.combinationSum3(3,9)
