# coding=utf-8
#
# @lc app=leetcode id=377 lang=python
#
# [377] Combination Sum IV
#
# https://leetcode.com/problems/combination-sum-iv/description/
#
# algorithms
# Medium (43.70%)
# Likes:    875
# Dislikes: 98
# Total Accepted:    91K
# Total Submissions: 207.8K
# Testcase Example:  '[1,2,3]\n4'
#
# Given an integer array with all positive numbers and no duplicates, find the
# number of possible combinations that add up to a positive integer target.
# 
# Example:
# 
# 
# nums = [1, 2, 3]
# target = 4
# 
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# 
# Note that different sequences are counted as different combinations.
# 
# Therefore the output is 7.
# 
# 
# 
# 
# Follow up:
# What if negative numbers are allowed in the given array?
# How does it change the problem?
# What limitation we need to add to the question to allow negative numbers?
# 
# Credits:
# Special thanks to @pbrother for adding this problem and creating all test
# cases.
# 
#


class Solution(object):
    def scombinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Time Limit
        # [4,2,1], 32
        self.count = 0

        def inner_combine(p):
            if sum(p) == target:
                self.count += 1
                return
            elif sum(p) > target:
                return

            for i, v in enumerate(nums):
                inner_combine(p+[v])

        inner_combine([])
        return self.count

    def lcombinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Time Limit
        # [3,33,333], 10000
        if not nums or min(nums) > target:
            return 0
        target += 1
        answers = [0]*target
        for i in range(min(max(nums), target)):
            answers[i] = self.scombinationSum4(nums, i)

        for i in range(max(nums), target):
            answers[i] = sum([answers[i-n] for n in nums])

        return answers[-1]

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # DP is good
        if not nums:
            return 0

        length = min(max(nums)+1, target+1)
        answers = [0]*(target+1)
        nums.sort()
        read = []
        for i in range(length):
            answers[i] = sum([answers[i-n] for n in read])
            if i in nums:
                read.append(i)
                answers[i] += 1

        for i in range(length, target+1):
            answers[i] = sum([answers[i-n] for n in nums])
        return answers[-1]


# if __name__ == '__main__':
#     s = Solution()
    # for i in range(20):
    #     print i, s.scombinationSum4([1,2,4],i), s.combinationSum4([1,2,4],i)
    # print s.combinationSum4([3,33,333], 10000)
    # print s.combinationSum4([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], 10)
    # print s.scombinationSum4([9], 3)
    # print s.combinationSum4([9], 3)
    # print s.combinationSum4([1,2,3], 4)
    # print s.combinationSum4([4,2,1], 32)
    # print s.combinationSum4([4,2,1], 10)
    # print s.combinationSum4([4,2,1], 11)
    # print s.combinationSum4([4,2,1], 12)
    # print s.combinationSum4([4,2,1], 13)
    # print s.combinationSum4([4,2,1], 14)
    # print s.combinationSum4([4,2,1], 15)
