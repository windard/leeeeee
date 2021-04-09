# coding=utf-8
# @lc app=leetcode id=1143 lang=python
#
# [1143] Longest Common Subsequence
#
# https://leetcode.com/problems/longest-common-subsequence/description/
#
# algorithms
# Medium (57.61%)
# Total Accepted:    159.8K
# Total Submissions: 272.9K
# Testcase Example:  '"abcde"\n"ace"'
#
# Given two strings text1 and text2, return the length of their longest common
# subsequence.
# 
# A subsequence of a string is a new string generated from the original string
# with some characters(can be none) deleted without changing the relative order
# of the remaining characters. (eg, "ace" is a subsequence of "abcde" while
# "aec" is not). A common subsequence of two strings is a subsequence that is
# common to both strings.
# 
# 
# 
# If there is no common subsequence, return 0.
# 
# 
# Example 1:
# 
# 
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# 
# 
# Example 2:
# 
# 
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# 
# 
# Example 3:
# 
# 
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= text1.length <= 1000
# 1 <= text2.length <= 1000
# The input strings consist of lowercase English characters only.
# 
# 
#
class Solution(object):
    def longestCommonSubsequence1(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # "banfgganadbf", "asdanfga"
        dp = [[0]*len(text2) for _ in range(len(text1))]
        # dp[i][j] = max(dp[i][j-1]|dp[i][j-1]+1, dp[i-1][j])
        for i in range(len(text1)):
            # flag = True
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    if i > 0 and j > 0:
                        source = dp[i-1][j-1]
                    else:
                        source = 0
                    dp[i][j] = source + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            #     dp[i][j] = dp[i][j-1]
            #     if flag and text1[i] == text2[j]:
            #         dp[i][j] += 1
            #         if dp[i][j] > dp[i-1][j]:
            #             flag = False
            #     dp[i][j] = max(dp[i][j], dp[i-1][j])
            #     if text1[i] == text2[j]:
            #         dp[i][j] = 1
        # for line in dp:
        #     for point in line:
        #         print(point),
        #         # print ("*" if point else "_"),
        #     print("")
        return dp[-1][-1]

    def solution(self, text1, text2):
        dp = [[0]*(len(text2)+1) for _ in range((len(text1)+1))]

        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # for line in dp:
        #     for point in line:
        #         print (point),
        #     print("")
        return dp[len(text1)][len(text2)]

    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # 完了，再次做错了，上来就错
        # 重点在于数组长度要加一，但是对比的是减一的位置
        m = len(text1)+1
        n = len(text2)+1
        dp = [[0]*n for _ in range(m)]
        max_result = 0
        for i in range(1, m):
            for j in range(1, n):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                max_result = max(max_result, dp[i][j])
        return max_result

# 错误示例
# 1. 不能用 dp[i][j] = dp[i-1][j-1],因为会循环取到上一行的最后一个，作为新一行的第一个开始
# 2. 遇到相同的之后可以加一，但是下次再相同，不能又加一
# 3. 不行，还是不能理解，dp[i+1][j+1]
# 4. 最后比较大小的时候，还是要和同j位的上一个i对比
# 5. 先相加，再对比
#
# 所以，状态转移方程是上一个j-1位平移到下一个j位，如果相等就加1，否则不变
# 然后，和上一个i-1位对比，是否自身匹配还不如之前匹配的结果，或者自己其实不匹配，可以继续用之前的匹配值
# 其中，比较关键的是否字符已经匹配使用过的判断，需要注意下
# 继续是错误示范，啥也不知道啊，太难了吧。
#
# 正确的思路是 dp[i][j]=dp[i-1][j-1] + 1 | max(dp[i-1][j], dp[i][j-1])
# 就是说，如果用上一个的匹配的值的话，那就不能贪图这次还不占用
# 之前的思路是先平移过来，平移过来之后再比较，但是实际上是不能贪恋的，
# 若是平移过来的，就不能与上一步的比较，如果想比较的话，可以综合的做比较，将i-1和j-1做比较
# 若是想计算上一步，那接下来就只能计算下一步，不能和平移的结果做比较，这个限制没有考虑清楚


if __name__ == '__main__':
    s = Solution()
    # print(s.longestCommonSubsequence("abc", "def"))
    # print(s.longestCommonSubsequence("abc", "abc"))
    # print(s.longestCommonSubsequence("abcde", "ace"))
    print(s.longestCommonSubsequence("banfgganadbf", "asdanfga"))                   # 5
    print(s.longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd"))      # 4
    #                                     h   b r  c      h     b   rc
    print(s.longestCommonSubsequence("banfgganadbf", "asdanfga"))                   # 5
    print(s.longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd"))      # 4
    print(s.longestCommonSubsequence("oxcpqrsvwf", "shmtulqrypy"))                  # 2
