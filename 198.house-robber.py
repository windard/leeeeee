#
# @lc app=leetcode id=198 lang=python
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Easy (40.78%)
# Total Accepted:    298.7K
# Total Submissions: 731.5K
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Example 1:
# 
# 
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
# 
# Example 2:
# 
# 
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
# 
# 
#
class Solution(object):
    def _rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Wrong Answer
        # [2,1,1,2]
        odd = 0
        even = 0
        for index, value in enumerate(nums):
            if index % 2 == 0:
                even += value
            else:
                odd += value
        return max(odd, even)

    def __rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # best is dp
        if len(nums) == 0:
            return 0
        if len(nums) < 3:
            return max(nums)
        elif len(nums) == 3:
            return max(nums[0]+nums[2], nums[1])
        else:
            res = []
            res.append(nums[0])
            res.append(nums[1])
            res.append(max(nums[2]+res[0], res[1]))
            for index in range(3, len(nums)):
                res.append(max(nums[index]+res[index-2], res[index-1], nums[index]+res[index-3]))
            return max(res[-1], res[-2])

    def ___rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # better dp
        if not nums:
            return 0
        elif len(nums) < 3:
            return max(nums)
        res = []
        res.append(nums[0])
        res.append(max(nums[0], nums[1]))

        for index in range(2, len(nums)):
            res.append(max(nums[index] + res[index-2], res[index-1]))
        
        return max(res[-1], res[-2])

    def ____rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # greedy
        index = ans_with_index = ans_without_index = 0

        while index < len(nums):
            if ans_with_index < ans_without_index:
                ans_with_index, ans_without_index = ans_without_index + nums[index], ans_without_index
            else:
                ans_with_index, ans_without_index = ans_without_index + nums[index], ans_with_index
            index += 1
        return max(ans_with_index, ans_without_index)

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans_with_index = ans_without_index = 0

        for num in nums:
            ans_with_index, ans_without_index = ans_without_index + num, max(ans_with_index, ans_without_index)
        return max(ans_with_index, ans_without_index)


# if __name__ == "__main__":
#     s = Solution()
#     print s.rob([2,1,1,2])
#     print s.rob([2,7,9,3,1])
#     print s.rob([1,2,3,1])
