#
# @lc app=leetcode id=55 lang=python
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (31.33%)
# Total Accepted:    241.2K
# Total Submissions: 767.4K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Determine if you are able to reach the last index.
# 
# Example 1:
# 
# 
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its
# maximum
# jump length is 0, which makes it impossible to reach the last index.
# 
# 
#

class Solution(object):
    def _canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 不能从前往后找
        # 只能从后往前找
        n = len(nums) - 1
        m = n
        while n:
            if m < 0:
                return False
            if nums[m] >= n - m:
                n = m
            m -= 1
        return True
    
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 递归比迭代更快
        max_length = 0
        for key,value in enumerate(nums):
            if key > max_length:
                return False
            max_length = max(max_length, key+value)
            if max_length >= len(nums) -1:
                return True
        if max_length >= len(nums) -1:
            return True
        else:
            return False

    def _canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 贪心加回溯
        # 贪心应该从最大开始算起
        # 贪心算法只要有一个即可
        # 算太多会 Time Limit
        # 加缓存的回溯能更快一点
        # 不能用全局变量，会有影响
        # 还是 time limit
        self.counted = []

        if len(nums) <= 1:
            return True
        return bool(self.jump(nums, 0))

    def jump(self, nums, index):
        if index >= len(nums):
            return
        elif index in self.counted:
            return
        for i in range(nums[index], 0, -1):
            if index + i >= len(nums) - 1:
                return True
            r = self.jump(nums, index+i)
            if r:
                return True
            else:
                self.counted.append(index+i)
# if __name__ == "__main__":
#     s = Solution()
#     s.canJump([1,2,3])