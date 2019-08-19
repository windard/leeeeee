#
# @lc app=leetcode id=748 lang=python
#
# [748] Shortest Completing Word
#
# https://leetcode.com/problems/shortest-completing-word/description/
#
# algorithms
# Easy (54.94%)
# Likes:    131
# Dislikes: 472
# Total Accepted:    22.9K
# Total Submissions: 41.7K
# Testcase Example:  '"1s3 PSt"\n["step","steps","stripe","stepple"]'
#
# 
# Find the minimum length word from a given dictionary words, which has all the
# letters from the string licensePlate.  Such a word is said to complete the
# given string licensePlate
# 
# Here, for letters we ignore case.  For example, "P" on the licensePlate still
# matches "p" on the word.
# 
# It is guaranteed an answer exists.  If there are multiple answers, return the
# one that occurs first in the array.
# 
# The license plate might have the same letter occurring multiple times.  For
# example, given a licensePlate of "PP", the word "pair" does not complete the
# licensePlate, but the word "supper" does.
# 
# 
# Example 1:
# 
# Input: licensePlate = "1s3 PSt", words = ["step", "steps", "stripe",
# "stepple"]
# Output: "steps"
# Explanation: The smallest length word that contains the letters "S", "P",
# "S", and "T".
# Note that the answer is not "step", because the letter "s" must occur in the
# word twice.
# Also note that we ignored case for the purposes of comparing whether a letter
# exists in the word.
# 
# 
# 
# Example 2:
# 
# Input: licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
# Output: "pest"
# Explanation: There are 3 smallest length words that contains the letters "s".
# We return the one that occurred first.
# 
# 
# 
# Note:
# 
# licensePlate will be a string with length in range [1, 7].
# licensePlate will contain digits, spaces, or letters (uppercase or
# lowercase).
# words will have a length in the range [10, 1000].
# Every words[i] will consist of lowercase letters, and have length in range
# [1, 15].
# 
# 
#

import string


class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        license = {}
        for l in licensePlate:
            if l in string.ascii_letters:
                license[l.lower()] = license.get(l.lower(), 0) + 1

        min_length = float("inf")
        min_words = []

        for word in words:
            pat = {}
            for w in word:
                if w in string.ascii_letters:
                    pat[w.lower()] = pat.get(w.lower(), 0) + 1

            for key, value in license.items():
                if pat.get(key, 0) < value:
                    break
            else:
                if len(word) < min_length:
                    min_words = [word]
                    min_length = len(word)
                elif len(word) == min_length:
                    min_words.append(word)
        return min_words[0]


# if __name__ == '__main__':
#     s = Solution()
#     print s.shortestCompletingWord("1s3 PSt", ["step", "steps", "stripe","stepple"])
#     print s.shortestCompletingWord("1s3 456", ["looks", "pest", "stew", "show"])
