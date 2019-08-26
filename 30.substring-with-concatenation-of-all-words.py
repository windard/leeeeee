# coding=utf-8
#
# @lc app=leetcode id=30 lang=python
#
# [30] Substring with Concatenation of All Words
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (23.97%)
# Likes:    596
# Dislikes: 975
# Total Accepted:    143.1K
# Total Submissions: 595.6K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# You are given a string, s, and a list of words, words, that are all of the
# same length. Find all starting indices of substring(s) in s that is a
# concatenation of each word in words exactly once and without any intervening
# characters.
# 
# Example 1:
# 
# 
# Input:
# ⁠ s = "barfoothefoobarman",
# ⁠ words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar"
# respectively.
# The output order does not matter, returning [9,0] is fine too.
# 
# 
# Example 2:
# 
# 
# Input:
# ⁠ s = "wordgoodgoodgoodbestword",
# ⁠ words = ["word","good","best","word"]
# Output: []
# 
# 
#


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # Time Limit
        from collections import Counter
        if not words:
            return []
        step = len(words[0])
        length = len(words)
        target = Counter(words)
        res = []
        for i in range(0, len(s)-step*length+1):
            current = []
            for j in range(length):
                current.append(s[i+j*step:i+(j+1)*step])
            if Counter(current) == target:
                res.append(i)
        return res


# if __name__ == '__main__':
#     s = Solution()
#     print s.findSubstring('', ['boo'])
#     print s.findSubstring('124', [])
#     print s.findSubstring("barfoothefoobarman", ['foo', 'bar'])
#     print s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"])
#     print s.findSubstring('lingmindraboofooowingdingbarrwingmonkeypoundcake', ["fooo","barr","wing","ding","wing"])
