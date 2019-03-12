#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (26.32%)
# Total Accepted:    463.1K
# Total Submissions: 1.8M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 马拉车算法
        # 将奇偶两种情况转换为一种情况来处理
        # Manacher's Algorithm
        # T(n) = O(n)
        # 最长子串的长度是半径减1，起始位置是中间位置减去半径再除以2。
        ls = "$#"
        for i in s:
            ls += i
            ls += "#"
        ls += "&"


    def _longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # a little slow
        # T(n) = O(n * n)

        maxGroup = ""
        for i in range(len(s)):
            singleGroup = self.checkSinglePalindromic(s, i)
            if len(singleGroup) > len(maxGroup):
                maxGroup = singleGroup
            doubleGroup = self.checkDoublePalindromic(s, i)
            if len(doubleGroup) > len(maxGroup):
                maxGroup = doubleGroup
        return maxGroup

    def checkSinglePalindromic(self, s, index):
        group = s[index]
        for i in range(1, index+1):
            if index - i >= 0 and index + i < len(s):
                if s[index - i] == s[index + i]:
                    group = "{}{}{}".format(s[index - i], group, s[index + i])
                else:
                    return group
            else:
                break
        return group

    def checkDoublePalindromic(self, s, index):
        group = ""
        for i in range(index+1):
            if index - i >= 0 and index + i + 1 < len(s):
                if s[index - i] == s[index + i + 1]:
                    group = "{}{}{}".format(s[index - i], group, s[index + i + 1])
                else:
                    return group
            else:
                break
        return group

