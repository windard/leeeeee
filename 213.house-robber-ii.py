# coding=utf-8
#
# @lc app=leetcode id=213 lang=python
#
# [213] House Robber II
#
# https://leetcode.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (35.51%)
# Likes:    1101
# Dislikes: 38
# Total Accepted:    133.7K
# Total Submissions: 374.9K
# Testcase Example:  '[2,3,2]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed. All houses at this place are
# arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, adjacent houses have security system connected and it will
# automatically contact the police if two adjacent houses were broken into on
# the same night.
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Example 1:
# 
# 
# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money =
# 2),
# because they are adjacent houses.
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
# 
#

# @lc code=start


class Solution(object):
    def _rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 只有两种情况？
        # 奇数或者偶数？
        # 或者四种情况
        # 好吧，我知道了，也有可能出现两家特别大，100,1,1,100,1
        # 或者 1,100,1,1,100
        # 行了，别说了
        # 动态规划
        # Wrong Answer
        if not nums:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        gems = [[] for _ in range(len(nums))]
        for index, num in enumerate(nums):
            if index < 1:
                gems[index] = [1, num]
            elif index < 2:
                if gems[index-1][1] > num:
                    gems[index] = gems[index-1]
                else:
                    gems[index] = [0, num]
            elif index == len(nums) - 1:
                if not gems[index-2][0]:
                    return max(gems[index-2][1]+num, gems[index-1][1])
                else:
                    return max(gems[index-2][1], gems[index-1][1])
            else:
                if gems[index-2][1] + num > gems[index-1][1]:
                    gems[index] = [gems[index-2][0], gems[index-2][1]+num]
                else:
                    gems[index] = gems[index - 1]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        with_index = without_index = 0
        # 取第一间，不算最后一间的最大值
        for num in nums[:-1]:
            with_index, without_index = without_index + num, max(with_index, without_index)
        with_first = max(with_index, without_index)
        # 取最后一件，不算第一间的最大值
        with_index = without_index = 0
        for num in nums[1:]:
            with_index, without_index = without_index + num, max(without_index, with_index)
        with_last = max(with_index, without_index)
        return max(with_first, with_last) if len(nums) != 1 else nums[0]

# @lc code=end


# if __name__ == '__main__':
#     s = Solution()
#     print s.rob([])
#     print s.rob([0])
#     print s.rob([1])
#     print s.rob([0,0])
#     print s.rob([2,3,2])
#     print s.rob([1,2,3,1])
#     print s.rob([100,1,1,100,1])
#     print s.rob([1,34,13,235,32,6,23,51,4])
#     print s.rob([1,1,3,6,7,10,7,1,8,5,9,1,4,4,3])
