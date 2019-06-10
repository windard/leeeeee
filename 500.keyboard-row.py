#
# @lc app=leetcode id=500 lang=python
#
# [500] Keyboard Row
#
# https://leetcode.com/problems/keyboard-row/description/
#
# algorithms
# Easy (61.68%)
# Likes:    397
# Dislikes: 497
# Total Accepted:    89K
# Total Submissions: 143K
# Testcase Example:  '["Hello","Alaska","Dad","Peace"]'
#
# Given a List of words, return the words that can be typed using letters of
# alphabet on only one row's of American keyboard like the image below.
# 
# 
# 
# 
# 
# 
# Example:
# 
# 
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
# 
# 
# 
# 
# Note:
# 
# 
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.
# 
# 
#
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard = ['qwertyuiopQWERTYUIOP', 'asdfghjklASDFGHJKL', 'zxcvbnmZXCVBNM']
        res = []
        for word in words:
            pos = []
            for w in word:
                for index, key in enumerate(keyboard):
                    if w in key:
                        pos.append(index)
                        break
            if len(set(pos)) == 1:
                res.append(word)
        return res

    def _findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # Faster
        keyboard = [set('qwertyuiopQWERTYUIOP'), set('asdfghjklASDFGHJKL'), set('zxcvbnmZXCVBNM')]
        res = []
        for word in words:
            pos = []
            for index, key in enumerate(keyboard):
                if set(word) & key == set(word):
                    pos.append(index)
            if len(set(pos)) == 1:
                res.append(word)
        return res
