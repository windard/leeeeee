#
# @lc app=leetcode id=557 lang=python
#
# [557] Reverse Words in a String III
#
# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
#
# algorithms
# Easy (63.15%)
# Likes:    624
# Dislikes: 67
# Total Accepted:    127.4K
# Total Submissions: 198.3K
# Testcase Example:  `"Let's take LeetCode contest"`
#
# Given a string, you need to reverse the order of characters in each word
# within a sentence while still preserving whitespace and initial word order.
# 
# Example 1:
# 
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# 
# 
# 
# Note:
# In the string, each word is separated by single space and there will not be
# any extra space in the string.
# 
#
class Solution(object):
    def _reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sl = s.split()
        ls = []
        for l in sl:
            ls.append(''.join(list(l)[::-1]))
        return ' '.join(ls)        

    def __reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sl = s.split()
        for index, value in enumerate(sl):
            sl[index] = ''.join(list(value)[::-1])
        return ' '.join(sl)

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1])[::-1]
