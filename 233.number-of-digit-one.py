# coding=utf-8
#
# @lc app=leetcode id=233 lang=python
#
# [233] Number of Digit One
#
# https://leetcode.com/problems/number-of-digit-one/description/
#
# algorithms
# Hard (30.53%)
# Likes:    188
# Dislikes: 482
# Total Accepted:    42.6K
# Total Submissions: 139.6K
# Testcase Example:  '13'
#
# Given an integer n, count the total number of digit 1 appearing in all
# non-negative integers less than or equal to n.
# 
# Example:
# 
# 
# Input: 13
# Output: 6 
# Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
# 
# 
#


class Solution(object):
    def _countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time Limit
        # 824883294
        index = 0
        count = 0
        while index <= n:
            count += str(index).count("1")
            index += 1
        return count

    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        level = 1
        count = 0
        while True:
            step, redundancy = divmod(n, level*10)
            count += level*step
            r, l = divmod(redundancy, level)
            if r > 1:
                count += level
            elif r > 0:
                count += l + 1

            level *= 10
            if not step:
                return count


# if __name__ == '__main__':
#     s = Solution()
#     print s.countDigitOne(0)      # 0
#     print s.countDigitOne(10)     # 2
#     print s.countDigitOne(100)    # 21
#     print s.countDigitOne(1000)   # 301

#     print s.countDigitOne(1)      # 1
#     print s.countDigitOne(2)      # 1
#     print s.countDigitOne(13)     # 6
#     print s.countDigitOne(124)    # 58
#     print s.countDigitOne(1135)
#     print s.countDigitOne(54515)
