#
# @lc app=leetcode id=516 lang=python
#
# [516] Longest Palindromic Subsequence
#
# https://leetcode.com/problems/longest-palindromic-subsequence/description/
#
# algorithms
# Medium (45.47%)
# Likes:    985
# Dislikes: 134
# Total Accepted:    67K
# Total Submissions: 140.4K
# Testcase Example:  '"bbbab"'
#
# 
# Given a string s, find the longest palindromic subsequence's length in s. You
# may assume that the maximum length of s is 1000.
# 
# 
# Example 1:
# Input: 
# 
# "bbbab"
# 
# Output: 
# 
# 4
# 
# One possible longest palindromic subsequence is "bbbb".
# 
# 
# Example 2:
# Input:
# 
# "cbbd"
# 
# Output:
# 
# 2
# 
# One possible longest palindromic subsequence is "bb".
# 
#
class Solution(object):
    def _longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dynamic Programming
        # subsequence not substring
        # Wrong Answer
        max_length = 0
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i):
                if s[i] == s[j] and (dp[i-1][j+1] or i - j <= 2):
                    dp[i][j] = True
                    if i - j + 1 > max_length:
                        max_length = i - j + 1
        return max_length

    def __longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # bbbab
        # cacbab
        # Wrong DP
        max_length = 0
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i):
                if s[i] == s[j]:
                    if i - j <= 2:
                        dp[i][j] = i - j + 1
                    else:
                        dp[i][j] = dp[i-1][j+1] + 2
                    if dp[i][j] > max_length:
                        max_length = i - j + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j+1])
        return max_length


    def ___longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # bbbab
        # cacbab
        max_length = 1
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                    if dp[i][j] > max_length:
                        max_length = dp[i][j]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return max_length


    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # bbbab
        # cacbab
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][len(s)-1]

# if __name__ == "__main__":
#     s = Solution()
#     print s.longestPalindromeSubseq("bbbab")
#     print s.longestPalindromeSubseq("cacbab")
