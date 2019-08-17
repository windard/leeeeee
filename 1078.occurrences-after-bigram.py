# coding=utf-8
#
# @lc app=leetcode id=1078 lang=python
#
# [1078] Occurrences After Bigram
#
# https://leetcode.com/problems/occurrences-after-bigram/description/
#
# algorithms
# Easy (65.59%)
# Likes:    49
# Dislikes: 67
# Total Accepted:    12.9K
# Total Submissions: 19.7K
# Testcase Example:  '"alice is a good girl she is a good student"\n"a"\n"good"'
#
# Given words first and second, consider occurrences in some text of the form
# "first second third", where second comes immediately after first, and third
# comes immediately after second.
# 
# For each such occurrence, add "third" to the answer, and return the
# answer.
# 
# 
# 
# Example 1:
# 
# 
# Input: text = "alice is a good girl she is a good student", first = "a",
# second = "good"
# Output: ["girl","student"]
# 
# 
# 
# Example 2:
# 
# 
# Input: text = "we will we will rock you", first = "we", second = "will"
# Output: ["we","rock"]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= text.length <= 1000
# text consists of space separated words, where each word consists of lowercase
# English letters.
# 1 <= first.length, second.length <= 10
# first and second consist of lowercase English letters.
# 
# 
#


class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        words = text.split()
        result = []
        for i in range(len(words)-2):
            if words[i] == first and words[i+1] == second:
                result.append(words[i+2])
        return result

