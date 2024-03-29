#
# @lc app=leetcode id=201 lang=python
#
# [201] Bitwise AND of Numbers Range
#
# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
#
# algorithms
# Medium (35.44%)
# Total Accepted:    77.3K
# Total Submissions: 217.7K
# Testcase Example:  '5\n7'
#
# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND
# of all numbers in this range, inclusive.
#
# Example 1:
#
#
# Input: [5,7]
# Output: 4
#
#
# Example 2:
#
#
# Input: [0,1]
# Output: 0
#
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Extraordinary Solution
        max_num = 2 ** 31 - 1
        while (max_num & m != max_num & n):
            max_num = max_num << 1
        print max_num
        return max_num & m

    def _rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # memory error
        return reduce(lambda x,y: x & y, range(m, n+1))

