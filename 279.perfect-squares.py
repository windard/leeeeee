#
# @lc app=leetcode id=279 lang=python
#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (40.86%)
# Total Accepted:    169.1K
# Total Submissions: 410.2K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
# 
# Example 1:
# 
# 
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# 
# Example 2:
# 
# 
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#
import math

class Solution(object):

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.fourTheorem(n)

    def getSquares(self, n):
        # 广度遍历
        queue = []


    def fourTheorem(self, n):
        # 四平方定理: 任何一个正整数都能表示为不超过四个整数的平方之和
        # 1: 整数本身为平方数
        # 2，3
        # 4: 整数n可以表示为 n = 4^a * (8b + 7)
        one = math.sqrt(n)
        if one == int(one):
            return 1

        four = n
        while four % 4 == 0:
            four = four / 4
        if four % 8 == 7:
            return 4

        for i in range(n, 0, -1):
            left = math.sqrt(i)
            if int(left) == left:
                right = math.sqrt(n - i)
                if int(right) == right:
                    return 2
        return 3

    def findSquares(self, n):
        # 深度遍历死路一条
        res = []
        for i in range(n, 0, -1):
            num = math.sqrt(i)
            if int(num) == num:
                if n - i == 0:
                    res.append(i)
                    return res
                else:
                    left = self.findSquares(n-i)
                    if left:
                        res.append(i)
                        res.extend(left)
                        return res
        return res

# if __name__ == "__main__":
#     s = Solution()
#     print s.numSquares(12)

