# coding=utf-8
#
# @lc app=leetcode id=18 lang=python
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (29.74%)
# Likes:    1096
# Dislikes: 218
# Total Accepted:    239.2K
# Total Submissions: 778.4K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.
# 
# Note:
# 
# The solution set must not contain duplicate quadruplets.
# 
# Example:
# 
# 
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        # Double Point
        nums.sort()
        # index low
        il = 0
        # index fast(end)
        ie = len(nums)-1

        result = []
        for il in range(len(nums)-3):
            if il and nums[il-1] == nums[il]:
                continue

            for ie in range(len(nums)-1, il+2, -1):
                if ie < len(nums)-1 and nums[ie+1] == nums[ie]:
                    continue

                low = il + 1
                fast = ie - 1
                while low < fast:
                    if nums[il] + nums[low] + nums[fast] + nums[ie] == target:
                        result.append([nums[il], nums[low], nums[fast], nums[ie]])
                        low += 1
                        fast -= 1
                        while low < fast and nums[low-1] == nums[low]:
                            low += 1
                        while low < fast and nums[fast+1] == nums[fast]:
                            fast -= 1
                    elif nums[il] + nums[low] + nums[fast] + nums[ie] < target:
                        low += 1
                    else:
                        fast -= 1
        return result


# if __name__ == '__main__':
#     s = Solution()
#     print s.fourSum([1, 0, -1, 0, -2, 2], 0)
