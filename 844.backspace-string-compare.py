# coding=utf-8
#
# @lc app=leetcode id=844 lang=python
#
# [844] Backspace String Compare
#
# https://leetcode.com/problems/backspace-string-compare/description/
#
# algorithms
# Easy (45.26%)
# Likes:    718
# Dislikes: 47
# Total Accepted:    68.1K
# Total Submissions: 146.4K
# Testcase Example:  '"ab#c"\n"ad#c"'
#
# Given two strings S and T, return if they are equal when both are typed into
# empty text editors. # means a backspace character.
#
#
# Example 1:
#
#
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
#
#
#
# Example 2:
#
#
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
#
#
#
# Example 3:
#
#
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
#
#
#
# Example 4:
#
#
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
#
#
# Note:
#
#
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.
#
#
# Follow up:
#
#
# Can you solve it in O(N) time and O(1) space?
#
#
#
#
#
#
#


class Solution(object):
    def _backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        sq = []
        tq = []
        for s in S:
            if s != '#':
                sq.append(s)
            else:
                try:
                    sq.pop()
                except:
                    pass

        for t in T:
            if t != '#':
                tq.append(t)
            else:
                try:
                    tq.pop()
                except:
                    pass
        return tq == sq

    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s_str = ""
        s_index = len(S) - 1
        backspace = 0
        while s_index >= 0:
            if S[s_index] == "#":
                backspace += 1
            else:
                if backspace:
                    backspace -= 1
                else:
                    s_str += S[s_index]
            s_index -= 1

        t_index = len(T) - 1
        t_str = ""
        backspace = 0
        while t_index >= 0:
            if T[t_index] == "#":
                backspace += 1
            else:
                if backspace:
                    backspace -= 1
                else:
                    t_str += T[t_index]
            t_index -= 1

        return s_str == t_str

#
# if __name__ == '__main__':
#     s = Solution()
#     print s.backspaceCompare("a##c", "#a#c")
