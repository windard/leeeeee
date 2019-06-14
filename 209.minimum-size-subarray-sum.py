#
# @lc app=leetcode id=209 lang=python
#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (34.26%)
# Total Accepted:    171.1K
# Total Submissions: 494.7K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of n positive integers and a positive integer s, find the
# minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
# one, return 0 instead.
# 
# Example: 
# 
# 
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem
# constraint.
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution of
# which the time complexity is O(n log n). 
# 
#
class Solution(object):
    def _minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if max(nums) >= s:
            return 1

        first = 0
        after = 0
        total = 0
        min_length = float("inf")
        flag = True
        while flag:
            flag = False
            while total < s and first < len(nums):
                flag = True
                total += nums[first]
                first += 1
            
            while total >= s:
                flag = True
                min_length = min(min_length, first - after)
                total -= nums[after]
                after += 1
        
        return 0 if min_length == float("inf") else min_length

    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        first = 0
        after = 0
        total = 0
        min_length = float("inf")
        while True:
            if total < s:
                if first >= len(nums):
                    break
                total += nums[first]
                first += 1
            else:
                min_length = min(min_length, first - after)
                total -= nums[after]
                after += 1
        
        return 0 if min_length == float("inf") else min_length

# if __name__ == "__main__":
#     s = Solution()
#     print s.minSubArrayLen(3, [1, 1])
#     print s.minSubArrayLen(7, [2,3,1,2,4,3, 7, 1])
