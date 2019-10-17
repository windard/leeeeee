# coding=utf-8
#
# @lc app=leetcode id=211 lang=python
#
# [211] Add and Search Word - Data structure design
#
# https://leetcode.com/problems/add-and-search-word-data-structure-design/description/
#
# algorithms
# Medium (29.18%)
# Likes:    944
# Dislikes: 59
# Total Accepted:    123.8K
# Total Submissions: 395.3K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n' +
#  '[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# Design a data structure that supports the following two operations:
# 
# 
# void addWord(word)
# bool search(word)
# 
# 
# search(word) can search a literal word or a regular expression string
# containing only letters a-z or .. A . means it can represent any one letter.
# 
# Example:
# 
# 
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# 
# 
# Note:
# You may assume that all words are consist of lowercase letters a-z.
# 
#

import re
from collections import defaultdict

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 可用用前缀树
        self.value = []
        # 或者根据长度比较
        self.data = defaultdict(list)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        # self.value.append(word)
        self.data[len(word)].append(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        # 正则匹配，点代表匹配除换行符'\n'之外的任意字符
        # for v in self.value:
        #     if re.search(word, v):
        #         return True
        # return False
        # 判断有误
        # for i, v in enumerate(word):
        #     if v == '.' or v == self.data[len(word)][i]:
        #         pass
        #     else:
        #         return False
        # return True
        words = self.data[len(word)][::]
        for i, v in enumerate(word):
            if not words:
                return False
            if v == '.':
                continue
            else:
                new_words = []
                for w in words:
                    if w[i] == v:
                        new_words.append(w)
                words = new_words
        return bool(words)


# Your WordDictionary object will be instantiated and called as such:
# if __name__ == '__main__':
#
#     obj = WordDictionary()
#     obj.addWord('bad')
#     obj.addWord('dad')
#     obj.addWord('mad')
#     obj.addWord('ab')
#     obj.addWord('a')
#     print obj.search('.a')
#     print obj.search('pad')
#     print obj.search('bad')
#     print obj.search('.ad')
#     print obj.search('b..')
