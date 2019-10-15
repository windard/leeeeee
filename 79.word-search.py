# coding=utf-8
#
# @lc app=leetcode id=79 lang=python
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (32.03%)
# Likes:    2301
# Dislikes: 121
# Total Accepted:    339.9K
# Total Submissions: 1M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# Example:
# 
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
# 
# 
#

# @lc code=start
class Solution(object):
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

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print s.exist([['a','a']], 'aaa')
    print s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCEDF")
    print s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
