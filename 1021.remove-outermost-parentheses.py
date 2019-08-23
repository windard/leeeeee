# coding=utf-8
#
# @lc app=leetcode id=1021 lang=python
#
# [1021] Remove Outermost Parentheses
#
# https://leetcode.com/problems/remove-outermost-parentheses/description/
#
# algorithms
# Easy (75.11%)
# Likes:    179
# Dislikes: 258
# Total Accepted:    38.7K
# Total Submissions: 51.4K
# Testcase Example:  '"(()())(())"'
#
# A valid parentheses string is either empty (""), "(" + A + ")", or A + B,
# where A and B are valid parentheses strings, and + represents string
# concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid
# parentheses strings.
# 
# A valid parentheses string S is primitive if it is nonempty, and there does
# not exist a way to split it into S = A+B, with A and B nonempty valid
# parentheses strings.
# 
# Given a valid parentheses string S, consider its primitive decomposition: S =
# P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
# 
# Return S after removing the outermost parentheses of every primitive string
# in the primitive decomposition of S.
# 
# 
# 
# Example 1:
# 
# 
# Input: ""(()())(())""
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" +
# "(())".
# After removing outer parentheses of each part, this is "()()" + "()" =
# "()()()".
# 
# 
# 
# Example 2:
# 
# 
# Input: "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation: 
# The input string is "(()())(())(()(()))", with primitive decomposition
# "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" +
# "()(())" = "()()()()(())".
# 
# 
# 
# Example 3:
# 
# 
# Input: "()()"
# Output: ""
# Explanation: 
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# S.length <= 10000
# S[i] is "(" or ")"
# S is a valid parentheses string
# 
# 
# 
# 
# 
# 
# 
#


class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        primitive = ""
        result = ""
        for s in S:
            primitive += s
            if s == "(":
                stack.append(s)
            else:
                stack.pop()
                if not stack and primitive:
                    result += primitive[1:-1]
                    primitive = ""
        return result


# if __name__ == '__main__':
#     s = Solution()
#     print s.removeOuterParentheses("(()())(())")
#     print s.removeOuterParentheses("(()())(())(()(()))")
#     print s.removeOuterParentheses("()()")
