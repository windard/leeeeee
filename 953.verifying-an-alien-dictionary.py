# coding=utf-8
#
# @lc app=leetcode id=953 lang=python
#
# [953] Verifying an Alien Dictionary
#
# https://leetcode.com/problems/verifying-an-alien-dictionary/description/
#
# algorithms
# Easy (55.94%)
# Likes:    238
# Dislikes: 86
# Total Accepted:    28.1K
# Total Submissions: 50.1K
# Testcase Example:  '["hello","leetcode"]\n"hlabcdefgijkmnopqrstuvwxyz"'
#
# In an alien language, surprisingly they also use english lowercase letters,
# but possibly in a different order. The order of the alphabet is some
# permutation of lowercase letters.
# 
# Given a sequence of words written in the alien language, and the order of the
# alphabet, return true if and only if the given words are sorted
# lexicographicaly in this alien language.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is
# sorted.
# 
# 
# 
# Example 2:
# 
# 
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] >
# words[1], hence the sequence is unsorted.
# 
# 
# 
# Example 3:
# 
# 
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is
# shorter (in size.) According to lexicographical rules "apple" > "app",
# because 'l' > '∅', where '∅' is defined as the blank character which is less
# than any other character (More info).
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are english lowercase letters.
# 
# 
# 
# 
# 
#


class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        for i in range(len(words)-1):
            if not self.compare(order, words[i], words[i+1]):
                return False
        return True

    def compare(self, order, front, behind):
        index = 0
        while index < len(front) or index < len(behind):
            if index == len(front):
                return True
            elif index == len(behind):
                return False
            if order.index(front[index]) < order.index(behind[index]):
                return True
            elif order.index(front[index]) > order.index(behind[index]):
                return False

            index += 1
        return True


# if __name__ == '__main__':
#     s = Solution()
#     print s.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
#     print s.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz")
#     print s.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")
