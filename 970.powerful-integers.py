# coding=utf-8
#
# @lc app=leetcode id=970 lang=python
#
# [970] Powerful Integers
#
# https://leetcode.com/problems/powerful-integers/description/
#
# algorithms
# Easy (39.45%)
# Likes:    76
# Dislikes: 166
# Total Accepted:    13K
# Total Submissions: 33K
# Testcase Example:  '2\n3\n10'
#
# Given two positive integers x and y, an integer is powerful if it is equal to
# x^i + y^j for some integers i >= 0 and j >= 0.
# 
# Return a list of all powerful integers that have value less than or equal to
# bound.
# 
# You may return the answer in any order.  In your answer, each value should
# occur at most once.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: x = 2, y = 3, bound = 10
# Output: [2,3,4,5,7,9,10]
# Explanation: 
# 2 = 2^0 + 3^0
# 3 = 2^1 + 3^0
# 4 = 2^0 + 3^1
# 5 = 2^1 + 3^1
# 7 = 2^2 + 3^1
# 9 = 2^3 + 3^0
# 10 = 2^0 + 3^2
# 
# 
# 
# Example 2:
# 
# 
# Input: x = 3, y = 5, bound = 15
# Output: [2,4,6,8,10,14]
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= x <= 100
# 1 <= y <= 100
# 0 <= bound <= 10^6
# 
#


class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        result = set()
        outer = inner = 0
        if x == 1 or y == 1:
            last = x + y - 1
            if last == 1:
                if bound > 1:
                    return [2]
                else:
                    return []
            index = 0
            while True:
                value = last**index + 1
                if value > bound:
                    break
                index += 1
                result.add(value)
            return result
        while True:
            while True:
                value = x**outer + y**inner
                if value > bound:
                    break
                result.add(value)
                inner += 1
            inner = 0
            outer += 1
            value = x**outer + y**inner
            if value > bound:
                break
            result.add(value)
            inner += 1
        return result


# if __name__ == "__main__":
#     s = Solution()
#     print s.powerfulIntegers(2, 1, 10)
