# coding=utf-8
#
# @lc app=leetcode id=264 lang=python
#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (37.08%)
# Likes:    1094
# Dislikes: 73
# Total Accepted:    115.6K
# Total Submissions: 308.6K
# Testcase Example:  '10'
#
# Write a program to find the n-th ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# 
# Example:
# 
# 
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.
# 
# Note:  
# 
# 
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
# 
#


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglys = [1]
        l_2 = l_3 = l_5 = 0
        length = 1
        while length < n:
            ugly = min(uglys[l_2] * 2, uglys[l_3] * 3, uglys[l_5] * 5)
            if ugly != uglys[-1]:
                uglys.append(ugly)
                length += 1
            if ugly == uglys[l_2] * 2:
                l_2 += 1
            elif ugly == uglys[l_3] * 3:
                l_3 += 1
            else:
                l_5 += 1
        return uglys[-1]

    def ___nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Wrong Solution
        if n < 1:
            return 1
        uglys = [1, 0]
        a_index = -1
        b_index = -1
        c_index = -1
        length = 0
        ugly = 0
        while True:
            a_index += 1
            ugly = 2 * uglys[a_index] + 3 * uglys[b_index] + 5 * uglys[c_index]
            length += 1
            if length == n:
                return ugly
            uglys.insert(-1, ugly)

            b_index += 1
            ugly = 2 * uglys[a_index] + 3 * uglys[b_index] + 5 * uglys[c_index]
            length += 1
            if length == n:
                return ugly
            uglys.insert(-1, ugly)

            c_index += 1
            ugly = 2 * uglys[a_index] + 3 * uglys[b_index] + 5 * uglys[c_index]
            length += 1
            if length == n:
                return ugly
            uglys.insert(-1, ugly)

    def __nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time Limit
        length = 0
        index = 0
        while length < n:
            index += 1
            if self.isUgly(index):
                length += 1
        return index

    def _nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 思路是错的，不是线性增长出来的
        if n < 1:
            return None

        common = reduce(self.lcm, [2, 3, 5])
        common_nums = []
        for i in range(common+1):
            if self.isUgly(i):
                common_nums.append(i)

        # 18 个 ，从 1 到 30
        if n <= len(common_nums):
            return common_nums[n-1]
        # 17 个，从 32 到 60
        else:
            step, left = divmod(n - len(common_nums), len(common_nums[1:]))
            return common * (step + 1) + common_nums[1:][left-1]

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        while num:
            if num % 2 != 0:
                break
            num = num / 2

        while num:
            if num % 3 != 0:
                break
            num = num / 3

        while num:
            if num % 5 != 0:
                break
            num = num / 5

        if num == 1:
            return True
        else:
            return False

    def gcd(self, a, b):
        a, b = max(a, b), min(a, b)
        while b:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        return a * b / self.gcd(a, b)


# if __name__ == '__main__':
#     s = Solution()
    # for i in range(1, 11):
    #     print s.nthUglyNumber(i)
    # print s.nthUglyNumber(10)
    # print s.nthUglyNumber(19)
    # print s.nthUglyNumber(20)
    # print s.nthUglyNumber(30)
#     print s.gcd(3,5)
#     print s.gcd(10,8)
#     print s.lcm(2,6)
#     print s.lcm(8,10)
#     print reduce(s.lcm, [2,3,5])
#     for i in range(10):
#         print 10*i, s.nthUglyNumber(10*i)
#
