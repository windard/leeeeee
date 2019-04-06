#
# @lc app=leetcode id=520 lang=python
#
# [520] Detect Capital
#
# https://leetcode.com/problems/detect-capital/description/
#
# algorithms
# Easy (52.23%)
# Total Accepted:    81.2K
# Total Submissions: 155.2K
# Testcase Example:  '"USA"'
#
# 
# Given a word, you need to judge whether the usage of capitals in it is right
# or not.
# 
# 
# 
# We define the usage of capitals in a word to be right when one of the
# following cases holds:
# 
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital if it has more than one letter,
# like "Google".
# 
# Otherwise, we define that this word doesn't use capitals in a right way.
# 
# 
# 
# Example 1:
# 
# Input: "USA"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "FlaG"
# Output: False
# 
# 
# 
# Note:
# The input will be a non-empty word consisting of uppercase and lowercase
# latin letters.
# 
#
import string

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        us = 0
        for w in word:
            if w in string.uppercase:
                us += 1

        if us == 0:
            return True
        elif us == 1 and word[0] in string.uppercase:
            return True
        elif us == len(word):
            return True
        else:
            return False
