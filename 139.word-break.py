# coding=utf-8
#
# @lc app=leetcode id=139 lang=python
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (36.14%)
# Likes:    2586
# Dislikes: 136
# Total Accepted:    375K
# Total Submissions: 1M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words.
# 
# Note:
# 
# 
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
# 
# 
# Example 1:
# 
# 
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
# 
# 
# Example 2:
# 
# 
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
# 
# 
#


class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # dp
        # 一开始就应该想到用 动态规划
        # 最简单的
        # 最基础的
        dp = [-1] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
            else:
                dp[i] = False
        return dp[len(s)]

    def wrongSolution(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # Wrong Answer
        # aaaaaaa, [aaa, aaaa]
        if not s:
            return True
        if not wordDict:
            return False

        wordDict = set(wordDict)

        while wordDict:
            current = []
            word = ''
            for i in s:
                word += i
                if word in wordDict:
                    current.append(word)
                    word = ''
            if word:
                newDict = wordDict.difference(set(current))
                if wordDict == newDict:
                    return False
                wordDict = newDict
            else:
                return True
        return False

    def wrongSolution2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # Still Wrong
        if not s:
            return True
        if not wordDict:
            return False
        if s in wordDict:
            return True

        wordDict = set(wordDict)
        length = len(s)
        while True:
            current = []
            last = 0
            for i in range(length):
                if s[last:i] in wordDict and s[i:] in wordDict:
                    return True
                if s[last:i] in wordDict:
                    current.append(s[last:i])
                    last = i
                if s[i:] in wordDict:
                    current.append(s[i:])
                    break

            newDict = set(wordDict) - set(current)
            if newDict == wordDict:
                return False
            wordDict = newDict

    def _wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 回溯
        # Time Limit
        if not s:
            return True
        if not wordDict:
            return False

        data = [-1] * len(s)
        wordDict = set(wordDict)

        def backstack(strs, l):
            if data[l] > -1:
                return data[l]
            if strs in wordDict:
                return True

            for i, st in enumerate(strs):
                if strs[:i] in wordDict:
                    if backstack(strs[i:], i):
                        data[l] = 1
                        return True
            data[l] = 0
            return False
        return backstack(s, 0)

    def __wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 宽度搜索
        # 也需要一个记录标志位
        # 但是不知道怎么放
        # Time Limit
        stack = []
        wordDict = set(wordDict)
        l = 0
        while s or stack:
            if s:
                if s in wordDict:
                    return True
                for i in range(len(s)):
                    if s[:i] in wordDict:
                        stack.append([i, s[i:]])
            else:
                l, s = stack.pop()
        return False

    def ___wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 递归求解
        # Time Limit
        if not s:
            return True
        for i in range(len(s)+1):
            if s[:i] in wordDict:
                if self.wordBreak(s[i:], wordDict):
                    return True
        return False

    def ____wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 继续递归
        # 加上缓存
        self.data = [-1] * len(s)
        return self.solve(s, 0, wordDict)

    def solve(self, s, start, wordDict):
        if start >= len(s):
            return True
        if self.data[start] > -1:
            return self.data[start]
        index = start + 1
        while index < len(s)+1:
            if s[start:index] in wordDict:
                if self.solve(s, index, wordDict):
                    self.data[start] = 1
                    return True
            index += 1
        self.data[start] = 0
        return False


# if __name__ == '__main__':
#     s = Solution()
#     print s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
#     print s.wordBreak("goalspecial", ["go","goal","goals","special"])
#     print s.wordBreak("dogs", ['dog', 's', 'gs'])
#     print s.wordBreak("a", ['a'])
#     print s.wordBreak("aaaaaaa", ["aaaa","aaa"])
#     print s.wordBreak("leetcode", ["leet", "code"])
#     print s.wordBreak("applepenapple", ["apple", "pen"])
#     print s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
