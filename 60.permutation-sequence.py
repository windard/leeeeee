# coding=utf-8
#
# @lc app=leetcode id=60 lang=python
#
# [60] Permutation Sequence
#
# https://leetcode.com/problems/permutation-sequence/description/
#
# algorithms
# Medium (33.81%)
# Likes:    941
# Dislikes: 248
# Total Accepted:    147.5K
# Total Submissions: 435.2K
# Testcase Example:  '3\n3'
#
# The set [1,2,3,...,n] contains a total of n! unique permutations.
# 
# By listing and labeling all of the permutations in order, we get the
# following sequence for n = 3:
# 
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# Given n and k, return the k^th permutation sequence.
# 
# Note:
# 
# 
# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.
# 
# 
# Example 1:
# 
# 
# Input: n = 3, k = 3
# Output: "213"
# 
# 
# Example 2:
# 
# 
# Input: n = 4, k = 9
# Output: "2314"
# 
# 
#

import time
import math

def api_deco(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print time.time() - start
        return result
    return wrapper


class Solution(object):
    def _getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Time Limit
        # 9,171669
        permutions = self.reroll_permute(range(1, n+1), n)
        permutions.sort()
        return ''.join(map(str, permutions[k-1]))

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

    # @api_deco
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.count = 0
        self.result = None

        def backtrack(nums, p):
            if self.count > k:
                return
            if not nums:
                self.count += 1
                if self.count == k:
                    self.result = ''.join(map(str, p))

            for i, v in enumerate(nums):
                x = math.factorial(len(nums)-1)
                if self.count + x < k:
                    self.count += x
                    continue
                backtrack(nums[:i]+nums[i+1:], p+[v])

        backtrack(range(1, n+1), [])
        return self.result


# if __name__ == '__main__':
#     s = Solution()
#     print s.getPermutation(3,3)         # 213
#     print s.getPermutation(3,5)         # 312
#     print s.getPermutation(4,9)         # 2314
#     print s.getPermutation(9,171669)    # 531679428
#     print s.getPermutation(9,13531)     # 147869235
