#
# @lc app=leetcode id=506 lang=python
#
# [506] Relative Ranks
#
# https://leetcode.com/problems/relative-ranks/description/
#
# algorithms
# Easy (47.91%)
# Total Accepted:    40.8K
# Total Submissions: 84.9K
# Testcase Example:  '[5,4,3,2,1]'
#
# 
# Given scores of N athletes, find their relative ranks and the people with the
# top three highest scores, who will be awarded medals: "Gold Medal", "Silver
# Medal" and "Bronze Medal".
# 
# Example 1:
# 
# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, so
# they got "Gold Medal", "Silver Medal" and "Bronze Medal". For the left two
# athletes, you just need to output their relative ranks according to their
# scores.
# 
# 
# 
# Note:
# 
# N is a positive integer and won't exceed 10,000.
# All the scores of athletes are guaranteed to be unique.
# 
# 
# 
#
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        sorted_nums = sorted(nums, reverse=True)
        res = []
        for i in nums:
            index = sorted_nums.index(i)
            if index <= 2:
                res.append(medals[index])
            else:
                res.append(str(index + 1))
        return res
