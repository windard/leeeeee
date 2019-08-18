# coding=utf-8
#
# @lc app=leetcode id=917 lang=python
#
# [917] Reverse Only Letters
#
# https://leetcode.com/problems/reverse-only-letters/description/
#
# algorithms
# Easy (56.12%)
# Likes:    284
# Dislikes: 27
# Total Accepted:    32.1K
# Total Submissions: 57.2K
# Testcase Example:  '"ab-cd"'
#
# Given a string S, return the "reversed" string where all characters that are
# not a letter stay in the same place, and all letters reverse their
# positions.
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
# Input: "ab-cd"
# Output: "dc-ba"
# 
# 
# 
# Example 2:
# 
# 
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# 
# 
# 
# Example 3:
# 
# 
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
# 
# 
# 
# 
# 
# Note:
# 
# 
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122 
# S doesn't contain \ or "
# 
# 
# 
# 
# 
#

import string


class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = list(S)
        start = 0
        end = len(S) - 1
        while start < end:
            while S[start] not in string.ascii_letters:
                start += 1
                if start >= len(S):
                    return ''.join(S)
            while S[end] not in string.ascii_letters:
                end -= 1
                if end < 0:
                    return ''.join(S)
            if start > end:
                break
            S[start], S[end] = S[end], S[start]
            start += 1
            end -= 1

        return ''.join(S)


# if __name__ == '__main__':
#     s = Solution()
#     print s.reverseOnlyLetters("7_28]")
#     print s.reverseOnlyLetters("?6C40E")
