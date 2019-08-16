# coding=utf-8
#
# @lc app=leetcode id=824 lang=python
#
# [824] Goat Latin
#
# https://leetcode.com/problems/goat-latin/description/
#
# algorithms
# Easy (56.85%)
# Likes:    163
# Dislikes: 436
# Total Accepted:    36.6K
# Total Submissions: 62.8K
# Testcase Example:  '"I speak Goat Latin"'
#
# A sentence S is given, composed of words separated by spaces. Each word
# consists of lowercase and uppercase letters only.
# 
# We would like to convert the sentence to "Goat Latin" (a made-up language
# similar to Pig Latin.)
# 
# The rules of Goat Latin are as follows:
# 
# 
# If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of
# the word.
# For example, the word 'apple' becomes 'applema'.
# 
# If a word begins with a consonant (i.e. not a vowel), remove the first letter
# and append it to the end, then add "ma".
# For example, the word "goat" becomes "oatgma".
# 
# Add one letter 'a' to the end of each word per its word index in the
# sentence, starting with 1.
# For example, the first word gets "a" added to the end, the second word gets
# "aa" added to the end and so on.
# 
# 
# Return the final sentence representing the conversion from S to Goat
# Latin. 
# 
# 
# 
# Example 1:
# 
# 
# Input: "I speak Goat Latin"
# Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
# 
# 
# Example 2:
# 
# 
# Input: "The quick brown fox jumped over the lazy dog"
# Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa
# hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
# 
# 
# 
# 
# Notes:
# 
# 
# S contains only uppercase, lowercase and spaces. Exactly one space between
# each word.
# 1 <= S.length <= 150.
# 
# 
#


class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        RS = ""
        if not S.strip():
            return RS
        for i,s in enumerate(S.split()):
            for v in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                if s.startswith(v):
                    s = s+"ma"
                    break
            else:
                s = s[1:]+s[0]+"ma"
            s = s + "a"*(i+1)
            RS += s + " "
        return RS[:-1]


# if __name__ == '__main__':
#     s = Solution()
#     print s.toGoatLatin("I speak Goat Latin")
#     print s.toGoatLatin("The quick brown fox jumped over the lazy dog")
#     # "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
