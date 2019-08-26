# coding=utf-8
#
# @lc app=leetcode id=47 lang=python
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (39.19%)
# Likes:    1026
# Dislikes: 44
# Total Accepted:    248.7K
# Total Submissions: 609.1K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
# 
# Example:
# 
# 
# Input: [1,1,2]
# Output:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
# 
#


class Solution(object):
    def _permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Wrong Answer
        from itertools import permutations
        return list(permutations(nums, len(nums)))

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()

        def backtrack(nums, p):
            if not nums:
                result.append(p)

            for i, n in enumerate(nums):
                if i and nums[i-1] == nums[i]:
                    continue
                backtrack(nums[:i]+nums[i+1:], p+[n])

        backtrack(nums, [])
        return result


# if __name__ == '__main__':
#     s = Solution()
#     print s.permuteUnique([1,1,2])
