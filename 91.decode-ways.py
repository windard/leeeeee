# coding=utf-8
#
# @lc app=leetcode id=91 lang=python
#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (22.70%)
# Likes:    1607
# Dislikes: 1849
# Total Accepted:    285.6K
# Total Submissions: 1.3M
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
# 
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.
# 
# Example 1:
# 
# 
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# 
# 
# Example 2:
# 
# 
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
# 6).
# 
#


class Solution(object):
    def _numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Wrong Answer
        # 理解错误
        d = [0] * len(s)
        for i in range(len(s)):
            if not i:
                d[i] = 1
            else:
                if int(s[i-1:i+1]) < 27:
                    d[i] = d[i-1]+2
                else:
                    d[i] = d[i-1]+1
        return d[-1]

    def __numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 特殊情况太多
        if not s:
            return 0
        d = [0] * len(s)
        for i in range(len(s)):
            tmp = 0
            if int(s[i]) > 0:
                if i:
                    tmp += d[i-1]
                else:
                    tmp += 1
            if i and (s[i-1] == '1' or (s[i-1] == '2' and int(s[i]) < 7)):
                if i-2 >= 0:
                    tmp += d[i-2]
                else:
                    tmp += 1
            d[i] = tmp
            if not tmp:
                return 0
        return d[-1]

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 递归的性能太差
        # Time Limit
        if not s:
            return 0
        if s.startswith('0'):
            return 0
        # 用回溯
        global result
        result = 0

        def backtrack(prefix, value):
            if prefix.startswith('0'):
                return
            global result
            if 0 < int(prefix) < 27:
                if not value:
                    result += 1
                else:
                    for i in range(1, min(3, len(value)+1)):
                        backtrack(value[:i], value[i:])

        for i in range(1, min(3, len(s)+1)):
            backtrack(s[:i], s[i:])
        return result


# if __name__ == '__main__':
#     s = Solution()
#     print s.numDecodings("101")     # 1
#     print s.numDecodings("01")      # 0
#     print s.numDecodings("00")      # 0
#     print s.numDecodings("0")       # 0
#     print s.numDecodings("10")      # 1
#     print s.numDecodings("90")      # 0
#     print s.numDecodings("12")      # 2
#     print s.numDecodings("226")     # 3
#     print s.numDecodings("1129012") # 0
