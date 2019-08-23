#
# @lc app=leetcode id=720 lang=python
#
# [720] Longest Word in Dictionary
#
# https://leetcode.com/problems/longest-word-in-dictionary/description/
#
# algorithms
# Easy (43.74%)
# Likes:    382
# Dislikes: 478
# Total Accepted:    39.7K
# Total Submissions: 87.4K
# Testcase Example:  '["w","wo","wor","worl","world"]'
#
# Given a list of strings words representing an English Dictionary, find the
# longest word in words that can be built one character at a time by other
# words in words.  If there is more than one possible answer, return the
# longest word with the smallest lexicographical order.  If there is no answer,
# return the empty string.
# 
# Example 1:
# 
# Input: 
# words = ["w","wo","wor","worl", "world"]
# Output: "world"
# Explanation: 
# The word "world" can be built one character at a time by "w", "wo", "wor",
# and "worl".
# 
# 
# 
# Example 2:
# 
# Input: 
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# Output: "apple"
# Explanation: 
# Both "apply" and "apple" can be built from other words in the dictionary.
# However, "apple" is lexicographically smaller than "apply".
# 
# 
# 
# Note:
# All the strings in the input will only contain lowercase letters.
# The length of words will be in the range [1, 1000].
# The length of words[i] will be in the range [1, 30].
# 
#


class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        max_length = -float("inf")
        max_result = []
        for word in words:
            if self.checkWorld(word, words):
                length = len(word)
                if length > max_length:
                    max_length = length
                    max_result = [word]
                elif length == max_length:
                    max_result.append(word)
        return sorted(max_result)[0] if max_result else ""

    def checkWorld(self, word, worlds):
        worlds = set(worlds)
        for i in range(len(word)):
            if word[:i+1] not in worlds:
                return False
        return True


# if __name__ == "__main__":
#     s = Solution()
#     print s.longestWord(["w","wo","wor","worl", "world"])
#     print s.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"])
