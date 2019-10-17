# coding=utf-8
#
# @lc app=leetcode id=212 lang=python
#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (27.59%)
# Likes:    1253
# Dislikes: 74
# Total Accepted:    124.1K
# Total Submissions: 419.6K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
# '["oath","pea","eat","rain"]'
#
# Given a 2D board and a list of words from the dictionary, find all words in
# the board.
# 
# Each word must be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring. The
# same letter cell may not be used more than once in a word.
# 
# 
# 
# Example:
# 
# 
# Input: 
# board = [
# ⁠ ['o','a','a','n'],
# ⁠ ['e','t','a','e'],
# ⁠ ['i','h','k','r'],
# ⁠ ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]
# 
# Output: ["eat","oath"]
# 
# 
# 
# 
# Note:
# 
# 
# All inputs are consist of lowercase letters a-z.
# The values of words are distinct.
# 
# 
#


class TrieTreeNode(object):
    def __init__(self):
        self.is_end = False
        self.children = {}


class Solution(object):
    def _findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # Time Limit
        return filter(lambda x: self.exist(board, x), words)
        
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        if not board:
            return False

        # 回溯
        def backtrack(i, j, word, reached):
            if (i, j) in reached:
                return False
            if not word:
                return True
            reached.add((i, j))
            if i - 1 >= 0 and board[i - 1][j] == word[0]:
                if backtrack(i - 1, j, word[1:], reached):
                    return True
            if i + 1 < len(board) and board[i + 1][j] == word[0]:
                if backtrack(i + 1, j, word[1:], reached):
                    return True
            if j - 1 >= 0 and board[i][j - 1] == word[0]:
                if backtrack(i, j - 1, word[1:], reached):
                    return True
            if j + 1 < len(board[0]) and board[i][j + 1] == word[0]:
                if backtrack(i, j + 1, word[1:], reached):
                    return True
            reached.remove((i, j))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtrack(i, j, word[1:], set()):
                        return True
        return False

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board:
            return []
        root = TrieTreeNode()
        for word in words:
            head = root
            for w in word:
                if w not in head.children:
                    head.children[w] = TrieTreeNode()
                head = head.children[w]
            head.is_end = True

        result = set()

        def backtrack(i, j, reached, head, prepare):
            if (i, j) in reached:
                return
            if head.is_end:
                result.add(prepare)
                if not head.children:
                    return
            reached.add((i, j))
            if i - 1 >= 0 and board[i-1][j] in head.children:
                n = board[i-1][j]
                backtrack(i-1, j, reached, head.children[n], prepare+n)
            if i + 1 < len(board) and board[i+1][j] in head.children:
                n = board[i+1][j]
                backtrack(i+1, j, reached, head.children[n], prepare+n)
            if j - 1 >= 0 and board[i][j-1] in head.children:
                n = board[i][j-1]
                backtrack(i, j-1, reached, head.children[n], prepare+n)
            if j + 1 < len(board[0]) and board[i][j+1] in head.children:
                n = board[i][j+1]
                backtrack(i, j+1, reached, head.children[n], prepare+n)
            reached.remove((i, j))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root.children:
                    n = board[i][j]
                    backtrack(i, j, set(), root.children[n], n)
        return result


# if __name__ == '__main__':
#     s = Solution()
#     print s.findWords([['a']], ['a'])
#     print s.findWords([['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']], ["oath","pea","eat","rain"])
