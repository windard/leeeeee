# coding=utf-8
#
# @lc app=leetcode id=1002 lang=python
#
# [1002] Find Common Characters
#
# https://leetcode.com/problems/find-common-characters/description/
#
# algorithms
# Easy (69.80%)
# Likes:    365
# Dislikes: 46
# Total Accepted:    33K
# Total Submissions: 50.3K
# Testcase Example:  '["bella","label","roller"]'
#
# Given an array A of strings made only from lowercase letters, return a list
# of all characters that show up in all strings within the list (including
# duplicates).  For example, if a character occurs 3 times in all strings but
# not 4 times, you need to include that character three times in the final
# answer.
# 
# You may return the answer in any order.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: ["bella","label","roller"]
# Output: ["e","l","l"]
# 
# 
# 
# Example 2:
# 
# 
# Input: ["cool","lock","cook"]
# Output: ["c","o"]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j] is a lowercase letter
# 
# 
# 
#
class Solution(object):
    def _commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        if not A:
            return []
        result = list(A[0])
        for colum in A[1:]:
            current = []
            for c in colum:
                if c in result:
                    current.append(c)
                    result.remove(c)
            result = current
        return result

    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        if not A:
            return []
        data = {}
        for d in A[0]:
            data[d] = data.get(d, 0) + 1
        for colum in A[1:]:
            total = {}
            for c in colum:
                total[c] = total.get(c, 0) + 1
            for key in data:
                data[key] = min(data[key], total.get(key, 0))
        result = []
        for key,value in data.items():
            result += [key]*value
        return result
