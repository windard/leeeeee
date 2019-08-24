# coding=utf-8
#
# @lc app=leetcode id=16 lang=python
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (40.85%)
# Total Accepted:    294.3K
# Total Submissions: 711.7K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
#
import time


def api_deco(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print time.time() - start
        return result
    return wrapper


class Solution(object):
    @api_deco
    def _threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Brute Force
        # Time Limit
        min_length = float("inf")
        min_result = None
        for ix in range(len(nums)):
            for iy in range(ix+1, len(nums)):
                for iz in range(iy+1, len(nums)):
                    diff = nums[ix] + nums[iy] + nums[iz] - target
                    if abs(diff) < min_length:
                        min_length = abs(diff)
                        min_result = nums[ix] + nums[iy] + nums[iz]
        return min_result

    # @api_deco
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Double Point
        # Like 3sum
        min_length = float("inf")
        min_result = None
        nums.sort()
        for ix, x in enumerate(nums[:-2]):
            if ix and nums[ix-1] == x:
                continue
            low = ix + 1
            fast = len(nums) - 1
            while low < fast:
                v = x + nums[low] + nums[fast]
                if abs(v - target) < min_length:
                    min_length = abs(v - target)
                    min_result = v
                if v > target:
                    fast -= 1
                elif v < target:
                    low += 1
                else:
                    return min_result
        return min_result


# if __name__ == '__main__':
#     s = Solution()
#     print s.threeSumClosest([-1,2,1,-4], 1)
#     print s.threeSumClosest([-12,-44,-67,-65,17,17,-80,73,51,46,-48,-43,-31,17,68,25,79,65,-41,18,-68,-7,29,-19,-48,3,-67,73,-57,-90,12,37,-16,-1,-65,47,53,-79,0,-62,-96,-10,-79,-25,38,93,28,6,99,68,-25,-27,-1,-61,70,-50,-54,-93,43,-34,31,98,-56,-70,44,49,-52,13,15,55,63,16,-30,-15,-25,87,75,81,19,17,88,-99,9,-92,-52,75,-16,97,-99,-86,60,-45,-88,99,75,36,-82,-67,-12,-47,37,-44,-45,67,85,-32,57,-11,-35,-51,-25,-38,54,-30,96,-62,-31,53,-79,-19,37,-73,95,-38,-60,72,-8,-24,-46,-61,63,-41,95,37,-79,-1,74,-9,92,97,-34,-69,-43,38,79,64,21,68,64], 189)
