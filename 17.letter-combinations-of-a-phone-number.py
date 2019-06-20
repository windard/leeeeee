#
# @lc app=leetcode id=17 lang=python
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (40.43%)
# Likes:    2236
# Dislikes: 301
# Total Accepted:    399.4K
# Total Submissions: 954.7K
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent.
# 
# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
# 
# 
# 
# Example:
# 
# 
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# Note:
# 
# Although the above answer is in lexicographical order, your answer could be
# in any order you want.
# 
#

key_map = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}

class Solution(object):
    def _letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        sources = []
        for d in digits:
            if not sources:
                sources.extend(list(key_map.get(d)))
            else:
                new_sources = []
                for char in key_map.get(d):
                    new_sources.extend(map(lambda x:x+char, sources[:]))
                sources = new_sources
        return sorted(sources)

    def __letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        from itertools import product
        sources = []
        for d in digits:
            if not sources:
                sources.extend(list(key_map.get(d)))
            else:
                sources = map(lambda x:''.join(x), product(sources, key_map.get(d)))
        return sources

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        return self.recall_digital(digits, [])
    
    def recall_digital(self, digits, sources):
        if not digits:
            return sources
        if not sources:
            return self.recall_digital(digits[1:], list(key_map.get(digits[0])))
        new_sources = []
        for source in sources:
            for char in key_map.get(digits[0]):
                new_sources.append(source + char)
        return self.recall_digital(digits[1:], new_sources)
