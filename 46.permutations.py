# coding=utf-8
#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (53.45%)
# Likes:    2083
# Dislikes: 61
# Total Accepted:    389.9K
# Total Submissions: 700.8K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#


class Solution(object):
    def _permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import permutations
        return permutations(nums)

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.reroll_permute(nums, len(nums))

    def reroll_permute(self, nums, length):
        output = []

        def backtrack(first=0):
            if first == length:
                output.append(nums[:])
            else:
                for i in range(first, len(nums)):
                    nums[i], nums[first] = nums[first], nums[i]
                    backtrack(first+1)
                    nums[first], nums[i] = nums[i], nums[first]
        backtrack()
        return output

    def recursion_permute(self, nums, length):
        if length == 1:
            return [[n] for n in nums]

        nums = list(nums)
        result = []
        paths = self.recursion_permute(nums, length-1)
        for path in paths:
            items = nums[:]
            for p in path:
                items.remove(p)
            for item in items:
                result.append(path+[item])
        return result

    def iteration_permute(self, nums, length):
        # iteration
        if length > len(nums):
            return
        nums = list(nums)

        result = []
        loop = 0
        while loop < length:
            if not result:
                for n in nums:
                    result.append([n])
            else:
                new_result = []
                for group in result:
                    items = nums[:]
                    for g in group:
                        items.remove(g)
                    for i in items:
                        new_result.append(group+[i])
                result = new_result
            loop += 1
        return result


# if __name__ == '__main__':
#     s = Solution()
#     print s.permute([1,2,3])
#     print s.recursion_permute('abcde', 2)
#     print s.recursion_permute('aabcde', 2)
