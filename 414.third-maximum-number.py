#
# @lc app=leetcode id=414 lang=python
#
# [414] Third Maximum Number
#
# https://leetcode.com/problems/third-maximum-number/description/
#
# algorithms
# Easy (28.66%)
# Likes:    377
# Dislikes: 688
# Total Accepted:    93.1K
# Total Submissions: 321.1K
# Testcase Example:  '[3,2,1]'
#
# Given a non-empty array of integers, return the third maximum number in this
# array. If it does not exist, return the maximum number. The time complexity
# must be in O(n).
# 
# Example 1:
# 
# Input: [3, 2, 1]
# 
# Output: 1
# 
# Explanation: The third maximum is 1.
# 
# 
# 
# Example 2:
# 
# Input: [1, 2]
# 
# Output: 2
# 
# Explanation: The third maximum does not exist, so the maximum (2) is returned
# instead.
# 
# 
# 
# Example 3:
# 
# Input: [2, 2, 3, 1]
# 
# Output: 1
# 
# Explanation: Note that the third maximum here means the third maximum
# distinct number.
# Both numbers with value 2 are both considered as second maximum.
# 
# 
#
class Solution(object):
    def _thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 题意理解有误
        # 不需要位置，返回的是值
        # 相同的数表示一位
        if not nums:
            return
        pos_map = {'f': 0, 's': 0, 't': 0}
        first = second = third = -float("inf")
        for key, num in enumerate(nums):
            if num > first:
                first, second, third = num, first, second
                pos_map['t'] = pos_map['s']
                pos_map['s'] = pos_map['f']
                pos_map['f'] = key
            elif num > second:
                second, third = num, second
                pos_map['t'] = pos_map['s']
                pos_map['s'] = key
            elif num > third:
                third = num
                pos_map['t'] = key
        print pos_map
        print first, second, third
        return pos_map['t']

    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 辛亏不要位置，使用 set 位置就改变了
        # 确实有可能出现两位，要求返回第三大的数
        nums = set(nums)
        # 还好没有出现零位的
        if len(nums) < 3:
            return max(nums)
        # 也可以用 -float('inf')
        first = second = third = min(nums)
        for num in nums:
            if num > first:
                first, second, third = num, first, second
            elif num > second:
                second, third = num, second
            elif num > third:
                third = num
        return third
