#
# @lc app=leetcode id=258 lang=python
#
# [258] Add Digits
#
# https://leetcode.com/problems/add-digits/description/
#
# algorithms
# Easy (53.53%)
# Total Accepted:    230K
# Total Submissions: 428.8K
# Testcase Example:  '38'
#
# Given a non-negative integer num, repeatedly add all its digits until the
# result has only one digit.
# 
# Example:
# 
# 
# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
# Since 2 has only one digit, return it.
# 
# 
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
#
class Solution(object):
    def _addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            num = sum(map(int, list(str(num))))
        return num

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # No recursion and iteration
        if num < 9:
            return num
        left = num % 9 
        return left if left != 0 else 9

# if __name__ == "__main__":
#     s = Solution()
#     for i in range(100):
#         print i, s._addDigits(i), s.addDigits(i)
