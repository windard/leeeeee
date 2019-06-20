#
# @lc app=leetcode id=868 lang=python
#
# [868] Binary Gap
#
# https://leetcode.com/problems/binary-gap/description/
#
# algorithms
# Easy (59.30%)
# Likes:    126
# Dislikes: 306
# Total Accepted:    23.7K
# Total Submissions: 39.8K
# Testcase Example:  '22'
#
# Given a positive integer N, find and return the longest distance between two
# consecutive 1's in the binary representation of N.
# 
# If there aren't two consecutive 1's, return 0.
# 
# 
# 
# 
# 
# 
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
# Input: 22
# Output: 2
# Explanation: 
# 22 in binary is 0b10110.
# In the binary representation of 22, there are three ones, and two consecutive
# pairs of 1's.
# The first consecutive pair of 1's have distance 2.
# The second consecutive pair of 1's have distance 1.
# The answer is the largest of these two distances, which is 2.
# 
# 
# 
# Example 2:
# 
# 
# Input: 5
# Output: 2
# Explanation: 
# 5 in binary is 0b101.
# 
# 
# 
# Example 3:
# 
# 
# Input: 6
# Output: 1
# Explanation: 
# 6 in binary is 0b110.
# 
# 
# 
# Example 4:
# 
# 
# Input: 8
# Output: 0
# Explanation: 
# 8 in binary is 0b1000.
# There aren't any consecutive pairs of 1's in the binary representation of 8,
# so we return 0.
# 
# 
# 
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
# 
#
class Solution(object):
    def _binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        bin_str = bin(N)
        max_length = 0
        last_index = -1
        for index, value in enumerate(bin_str):
            if value == '1':
                if last_index > -1:
                    max_length = max(index - last_index, max_length)
                last_index = index
        return max_length

    def __binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        max_length = 0
        count = -1
        while N:
            N, left = divmod(N, 2)
            if left == 0:
                if count > -1:
                    count += 1
            else:
                max_length = max(max_length, count + 1)
                count = 0
        return max_length

    def ___binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        indexs = []
        for i in range(32):
            if N & 1:
                indexs.append(i)
            N >>= 1
            if not N:
                break
        max_length = 0
        for i in range(len(indexs)-1):
            max_length = max(max_length, indexs[i+1] - indexs[i])

        return max_length

    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        max_length = 0
        last_index = -1
        for i in range(32):
            if N & 1:
                if last_index > -1:
                    max_length = max(max_length, i - last_index)
                last_index = i                    
            N >>= 1
            if not N:
                break

        return max_length

# if __name__ == "__main__":
#     s = Solution()
#     print s.binaryGap(5)
#     print s.binaryGap(6)
#     print s.binaryGap(8)
#     print s.binaryGap(22)
