#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (35.72%)
# Total Accepted:    501.8K
# Total Submissions: 1.4M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
#
# Note that an empty string is also considered valid.
#
# Example 1:
#
#
# Input: "()"
# Output: true
#
#
# Example 2:
#
#
# Input: "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: "(]"
# Output: false
#
#
# Example 4:
#
#
# Input: "([)]"
# Output: false
#
#
# Example 5:
#
#
# Input: "{[]}"
# Output: true
#
#
#

import Queue

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        left = ["(", "{", "["]
        right = [")", "}", "]"]

        bracket_map = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        stack = Queue.LifoQueue()
        for index,value in enumerate(s):
            if value in left:
                stack.put(value)
                continue
            try:
                l = stack.get(False)
            except Queue.Empty:
                l = None
            if bracket_map[value] != l:
                return False
        try:
            stack.get(False)
        except Queue.Empty:
            return True
        else:
            return False

