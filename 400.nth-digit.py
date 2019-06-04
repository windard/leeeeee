#
# @lc app=leetcode id=400 lang=python
#
# [400] Nth Digit
#
# https://leetcode.com/problems/nth-digit/description/
#
# algorithms
# Easy (30.09%)
# Total Accepted:    46K
# Total Submissions: 152.3K
# Testcase Example:  '3'
#
# Find the n^th digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8,
# 9, 10, 11, ... 
# 
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n <
# 2^31).
# 
# 
# Example 1:
# 
# Input:
# 3
# 
# Output:
# 3
# 
# 
# 
# Example 2:
# 
# Input:
# 11
# 
# Output:
# 0
# 
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0,
# which is part of the number 10.
# 
# 
#
class Solution(object):
    def _findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time Limit Exceeded
        index = 1
        res = ''
        while True:
            res += str(index)
            if len(res) >= n:
                return res[n-1]
            index += 1
    
    def __findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time Limit Exceeded
        index = 1
        res = ''
        len_res = len(res)
        while True:
            str_index = str(index)
            len_index = len(str_index)
            res += str_index
            len_res += len_index
            if len_res >= n:
                return str_index[len_index + n - len_res - 1]
                # return res[n-1]

            index += 1
    
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        while True:
            t = 10 ** (i - 1)
            m = i * 9 * t
            if n <= m:
                n -= 1
                return int(str(t + n // i)[n % i])
            n -= m
            i += 1

if __name__ == "__main__":
    s = Solution()
    print s.findNthDigit(3)
    print s.findNthDigit(10)
    print s.findNthDigit(100)
    print s.findNthDigit(1000)
    print s.findNthDigit(10000)
    print s.findNthDigit(100000)
    print s.findNthDigit(1000000)
    print s.findNthDigit(100000000)
