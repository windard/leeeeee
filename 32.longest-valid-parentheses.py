# coding=utf-8
#
# @lc app=leetcode id=32 lang=python
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (26.05%)
# Likes:    2165
# Dislikes: 97
# Total Accepted:    209.4K
# Total Submissions: 801.2K
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
# 
# Example 1:
# 
# 
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# 
# 
# Example 2:
# 
# 
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
# 
# 
#


class Solution(object):
    def _longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Wrong Answer
        # Longest Valid Parentheses
        stack = []
        count = 0
        for p in s:
            if p == ')':
                if stack:
                    stack.pop()
                    count += 2
            else:
                stack.append(p)
        return count

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dynamic planning
        # 动态规划的两种情况
        # dp[i]=dp[i−2]+2
        # dp[i]=dp[i−1]+dp[i−dp[i−1]−2]+2
        # O(n) 的时间复杂度
        dp = [0]*len(s)
        max_length = 0

        for i in range(len(s)):
            if i and s[i] == ')' and s[i-1] == '(':
                dp[i] = dp[i-2]+2
            elif i and i - dp[i - 1] - 1 >= 0 and s[i] == ')' and s[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i-1]+dp[max(0, i-dp[i-1]-2)]+2
            max_length = max(max_length, dp[i])
        return max_length


# if __name__ == '__main__':
#     s = Solution()
#     print s.longestValidParentheses("(())")
#     print s.longestValidParentheses("())")
#     print s.longestValidParentheses('(()')
#     print s.longestValidParentheses(')()())')
#     print s.longestValidParentheses('()(()')
#     print s.longestValidParentheses('()(())')
