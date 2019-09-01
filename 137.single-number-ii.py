# coding=utf-8
#
# @lc app=leetcode id=137 lang=python
#
# [137] Single Number II
#
# https://leetcode.com/problems/single-number-ii/description/
#
# algorithms
# Medium (46.72%)
# Likes:    937
# Dislikes: 266
# Total Accepted:    177.4K
# Total Submissions: 378.1K
# Testcase Example:  '[2,2,3,2]'
#
# Given a non-empty array of integers, every element appears three times except
# for one, which appears exactly once. Find that single one.
# 
# Note:
# 
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
# Example 1:
# 
# 
# Input: [2,2,3,2]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: [0,1,0,1,0,1,99]
# Output: 99
# 
#


class Solution(object):
    def _singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (sum(set(nums)) * 3 - sum(nums)) / 2

    def __singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # copy one
        b1, b2 = 0, 0
        for n in nums:
            b1 = (b1 ^ n) & ~ b2
            b2 = (b2 ^ n) & ~ b1
        return b1

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(self.three, nums)

    def three(self, x, y):
        # 实现三进制运算符
        # 三进制的不进位加法
        # 负数怎么考虑
        flag = True
        if x * y < 0:
            flag = False
            x = abs(x)
            y = abs(y)
        t = 0
        index = 1
        while x or y:
            l = r = 0
            if x:
                x, l = divmod(x, 3)
            if y:
                y, r = divmod(y, 3)
            t += ((l + r) % 3) * index
            index *= 3
        return t if flag else -t


if __name__ == '__main__':
    s = Solution()
    # print s.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2])
    print s.singleNumber([1,1,1,2])
    print s.singleNumber([2,2,3,2])
    print s.singleNumber([0,1,0,1,0,1,99])
