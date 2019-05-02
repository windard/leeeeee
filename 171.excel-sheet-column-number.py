#
# @lc app=leetcode id=171 lang=python
#
# [171] Excel Sheet Column Number
#
# https://leetcode.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (50.87%)
# Total Accepted:    213.7K
# Total Submissions: 417.4K
# Testcase Example:  '"A"'
#
# Given a column title as appear in an Excel sheet, return its corresponding
# column number.
# 
# For example:
# 
# 
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28 
# ⁠   ...
# 
# 
# Example 1:
# 
# 
# Input: "A"
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: "AB"
# Output: 28
# 
# 
# Example 3:
# 
# 
# Input: "ZY"
# Output: 701
# 
#
import string

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        i = 0
        while s:
            index = s[-1:]
            s = s[:-1]
            index_num = string.uppercase.index(index) + 1
            res += index_num * (26 ** i)
            i += 1
        return res

# if __name__ == "__main__":
#     s = Solution()
#     print s.titleToNumber('A')
#     print s.titleToNumber('Z')
#     print s.titleToNumber('AA')
#     print s.titleToNumber('AZ')
#     print s.titleToNumber('YZ')
#     print s.titleToNumber('ZY')
