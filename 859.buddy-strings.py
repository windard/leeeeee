# coding=utf-8
#
# @lc app=leetcode id=859 lang=python
#
# [859] Buddy Strings
#
# https://leetcode.com/problems/buddy-strings/description/
#
# algorithms
# Easy (27.53%)
# Likes:    324
# Dislikes: 196
# Total Accepted:    28K
# Total Submissions: 100.9K
# Testcase Example:  '"ab"\n"ba"'
#
# Given two strings A and B of lowercase letters, return true if and only if we
# can swap two letters in A so that the result equals B.
# 
# 
# 
# Example 1:
# 
# 
# 
# Input: A = "ab", B = "ba"
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: A = "ab", B = "ab"
# Output: false
# 
# 
# 
# Example 3:
# 
# 
# Input: A = "aa", B = "aa"
# Output: true
# 
# 
# 
# Example 4:
# 
# 
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
# 
# 
# 
# Example 5:
# 
# 
# Input: A = "", B = "aa"
# Output: false
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A and B consist only of lowercase letters.
# 
# 
# 
# 
# 
# 
# 
#


class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) < 2 or len(A) != len(B):
            return False

        index = 0
        first = -1
        second = -1
        while index < len(A):
            if A[index] != B[index]:
                if first == -1:
                    first = index
                elif second > -1:
                    return False
                else:
                    second = index
                    if A[first] == B[second] and A[second] == B[first]:
                        pass
                    else:
                        return False
            index += 1
        if first == -1 and second == -1:
            if len(set(A)) < len(A):
                return True
        return first > -1 and second > -1


# if __name__ == '__main__':
#     s = Solution()
#     print s.buddyStrings("ab", "ba")
#     print s.buddyStrings("", "nn")
#     print s.buddyStrings("aaaaaaabc", "aaaaaaacb")
#     print s.buddyStrings("ab", "ab")  # False
#     print s.buddyStrings("aa", "aa")  # True
#     print s.buddyStrings("aba", "aba")  # True
#     print s.buddyStrings("aab", "aab")  # True
