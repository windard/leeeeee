# coding=utf-8
#
# @lc app=leetcode id=869 lang=python
#
# [869] Reordered Power of 2
#
# https://leetcode.com/problems/reordered-power-of-2/description/
#
# algorithms
# Medium (49.95%)
# Likes:    140
# Dislikes: 67
# Total Accepted:    10.3K
# Total Submissions: 20K
# Testcase Example:  '1'
#
# Starting with a positive integer N, we reorder the digits in any order
# (including the original order) such that the leading digit is not zero.
# 
# Return true if and only if we can do this in a way such that the resulting
# number is a power of 2.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: 10
# Output: false
# 
# 
# 
# Example 3:
# 
# 
# Input: 16
# Output: true
# 
# 
# 
# Example 4:
# 
# 
# Input: 24
# Output: false
# 
# 
# 
# Example 5:
# 
# 
# Input: 46
# Output: true
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 10^9
# 
# 
# 
# 
# 
# 
# 
#

from collections import Counter


class Solution(object):
    def _reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        length = len(str(N))
        index = 1
        options = []
        while len(str(index)) < length:
            index *= 2

        while len(str(index)) == length:
            options.append(index)
            index *= 2

        for option in options:
            if Counter(str(option)) == Counter(str(N)):
                return True
        return False

    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        counter = Counter(str(N))
        return any([counter == Counter(str(1 << n)) for n in range(32)])

    def _reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        # Time Limit
        # 271612776
        # from itertools import permutations
        # return any([bin(int(''.join(n))).count('1') == 1
                    # for n in permutations(str(N)) if n[0] != '0'])
        # official answer is also wrong
        import itertools
        return any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1
                   for cand in itertools.permutations(str(N)))

#
# if __name__ == '__main__':
#     s = Solution()
#     print s.reorderedPowerOf2(1)
#     print s.reorderedPowerOf2(10)
#     print s.reorderedPowerOf2(16)
#     print s.reorderedPowerOf2(64)
#     print s.reorderedPowerOf2(46)
#     print s.reorderedPowerOf2(24)
