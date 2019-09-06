# coding=utf-8
#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (42.40%)
# Likes:    2117
# Dislikes: 106
# Total Accepted:    226.6K
# Total Submissions: 532.4K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
# 
# Your algorithm should run in O(n) complexity.
# 
# Example:
# 
# 
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
#


class Solution(object):
    def __longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        nums.sort()
        max_count = 0
        count = 0
        for i, n in enumerate(nums):
            if not i or nums[i-1] == nums[i] - 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1
        return max_count

    def _longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Wrong Answer
        # 不能满足条件
        s_nums = set(nums)
        max_count = 0
        count = 0
        for i in range(len(nums)):
            if not i or nums[i]-1 in s_nums:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1
        return max_count

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        data = dict(zip(nums, range(len(nums))))
        max_count = 0

        for i, n in enumerate(nums):
            count = 1
            if n - 1 not in data:
                m = n + 1
                while m in data:
                    count += 1
                    m += 1

                max_count = max(max_count, count)
        return max_count

#
# if __name__ == '__main__':
#     s = Solution()
#     print s.longestConsecutive([1,2,0,1])
#     print s.longestConsecutive([100, 4, 200, 1, 3, 2])
