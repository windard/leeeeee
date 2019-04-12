#
# @lc app=leetcode id=461 lang=python
#
# [461] Hamming Distance
#
# https://leetcode.com/problems/hamming-distance/description/
#
# algorithms
# Easy (70.04%)
# Total Accepted:    227.3K
# Total Submissions: 324.1K
# Testcase Example:  '1\n4'
#
# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.
# 
# Given two integers x and y, calculate the Hamming distance.
# 
# Note:
# 0 ≤ x, y < 2^31.
# 
# 
# Example:
# 
# Input: x = 1, y = 4
# 
# Output: 2
# 
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
# ⁠      ↑   ↑
# 
# The above arrows point to positions where the corresponding bits are
# different.
# 
# 
#
class Solution(object):

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # unbelieveable
        return bin(x ^ y).count('1')

    def ___hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # unbelieveable
        return bin(x ^ y).count('1')

    def __hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = 0
        while x or y:
            if x:
                l = x % 2
                x = x / 2
            else:
                l = 0

            if y:
                r = y % 2
                y = y / 2
            else:
                r = 0

            if l != r:
                res += 1
        return res

    def _hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # compare with bin stringg
        xb = bin(x)[2:]
        yb = bin(y)[2:]
        length = max(len(xb), len(yb))
        xb = xb.zfill(length)
        yb = yb.zfill(length)
        i = 0
        res = 0
        while i < length:
            if xb[i] != yb[i]:
                res += 1
            i += 1
        return res

# if __name__ == "__main__":
#     s = Solution()
#     print s.hammingDistance(1, 4)
#     print s.hammingDistance(2,5)
