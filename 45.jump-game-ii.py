#
# @lc app=leetcode id=45 lang=python
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (27.50%)
# Total Accepted:    157.3K
# Total Submissions: 569.7K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Your goal is to reach the last index in the minimum number of jumps.
# 
# Example:
# 
# 
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# ⁠   Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# Note:
# 
# You can assume that you can always reach the last index.
# 
#
class Solution(object):

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 再次优化
        dp = [float("INF")] * len(nums)
        dp[-1] = 0
        n = len(nums) - 2
        if len(nums) <= 1:
            return 0
        elif nums and nums[0] > len(nums) - 1:
            return 1
        while n >= 0:
            if nums[n] + n >= len(nums) - 1:
                dp[n] = 1
            else:
                dp[n] = min(dp[n:n+nums[n]+1]) + 1
            if dp[nums[0]] != float("INF") and dp[nums[0]] <= min(dp) + 1:
                return dp[nums[0]] + 1
            n -= 1
        return dp[0]

    def _jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 循环比递归更快
        # 还是 Time Limit 
        # 最后一个 91/92 
        # 最终优化版
        # 刚刚过
        count = {}
        count[len(nums)-1] = 0
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= len(nums) -1:
                count[i] = 1
            elif nums[i] == 0:
                count[i] = float("INF")
            else:
                count[i] = min([count[i+j] for j in range(1, nums[i]+1)]) + 1
            if nums[0] in count and count[nums[0]] <= min(count.values()) + 1:
                return count[nums[0]] + 1
        return count[0]

    def _jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 贪心加回溯
        # 贪心应该从最大开始算起
        # 一切皆可缓存
        # 最终 Time Limit
        self.counted = {}
        if len(nums) <= 1:
            return 0
        return self.canJump(nums, 0)

    def canJump(self, nums, index):
        if index >= len(nums):
            return
        elif index in self.counted:
            return self.counted[index]
        res = [float("INF")]
        for i in range(nums[index], 0, -1):
            if index + i >= len(nums) - 1:
                return 1
            r = self.canJump(nums, index+i)
            self.counted[index+i] = r
            res.append(r)
        return min(res) + 1 

# if __name__ == "__main__":
    # s = Solution()
    # print s.jump([2,3,1,1,4])
    # print s.counted
    # s = Solution()
    # print s.jump([3,4,1,3,6])
    # print s.counted
    # s = Solution()
    # print s.jump([9,8,2,2,0,2,2,0,4,1,5,7,9,6,6,0,6,5,0,5])
    # print s.counted