# coding=utf-8
#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (53.21%)
# Likes:    2836
# Dislikes: 176
# Total Accepted:    348.7K
# Total Submissions: 630.2K
# Testcase Example:  '3'
#
# 
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
#


class Solution(object):
    def _generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Wrong Answer
        if n == 1:
            return ['()']
        diagram = ['(){}', '{}()', '({})']
        graph = self.generateParenthesis(n-1)
        result = set()
        for g in graph:
            for dia in diagram:
                result.add(dia.format(g))
        return sorted(result)


    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ['()']
        result = set()
        graph = self.generateParenthesis(n-1)
        index = 1
        while index <= n/2:
            left = self.generateParenthesis(index)
            right = self.generateParenthesis(n-index)
            for l in left:
                for r in right:
                    result.add(l+r)
                    result.add(r+l)
            if index == 1:
                for r in right:
                    result.add('({})'.format(r))
            index += 1
        return sorted(result)

# if __name__ == '__main__':
#     s = Solution()
#     for i in range(1, 6):
#         print s.generateParenthesis(i)
