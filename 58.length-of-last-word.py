#
# @lc app=leetcode id=58 lang=python
#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (32.14%)
# Total Accepted:    242.8K
# Total Submissions: 755.5K
# Testcase Example:  '"Hello World"'
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space
# characters only.
#
# Example:
#
# Input: "Hello World"
# Output: 5
#
#
#
import string

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        flag = False
        digitals = string.lowercase + string.uppercase
        length = 0
        for i in s:
            if i in digitals:
                if not flag:
                    length = 0
                    flag = True
                length += 1
            elif i == ' ':
                flag = False
        return length


if __name__ == "__main__":
    s = Solution()
    s.lengthOfLastWord("hello World")
