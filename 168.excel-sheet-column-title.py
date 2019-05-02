#
# @lc app=leetcode id=168 lang=python
#
# [168] Excel Sheet Column Title
#
# https://leetcode.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (28.52%)
# Total Accepted:    168K
# Total Submissions: 584.4K
# Testcase Example:  '1'
#
# Given a positive integer, return its corresponding column title as appear in
# an Excel sheet.
# 
# For example:
# 
# 
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB 
# ⁠   ...
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: "A"
# 
# 
# Example 2:
# 
# 
# Input: 28
# Output: "AB"
# 
# 
# Example 3:
# 
# 
# Input: 701
# Output: "ZY"
# 
#
import string

class Solution(object):
    def _convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        left, right = divmod(n, 26)
        res = string.uppercase[right-1]
        if right == 0:
            left -= 1
        while left:
            left, right = divmod(left, 26)
            res = string.uppercase[right-1] + res
            if right == 0:
                left -= 1
        return res

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        while n:
            n -= 1
            n, right = divmod(n, 26)
            res = string.uppercase[right] + res
        return res

# if __name__ == "__main__":
#     s = Solution()
#     print s.convertToTitle(1)
#     print s.convertToTitle(2)
#     print s.convertToTitle(26)
#     print s.convertToTitle(27)
#     print s.convertToTitle(28)
#     print s.convertToTitle(701)
#     print s.convertToTitle(7701)
