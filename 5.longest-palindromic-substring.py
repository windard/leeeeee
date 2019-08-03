# coding=utf-8
#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (26.32%)
# Total Accepted:    463.1K
# Total Submissions: 1.8M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s

        ls = "$#"
        for i in s:
            ls += i
            ls += "#"
        ls += "&"
        data = {}

        max_index = 0
        right_max_index = 0
        data[right_max_index] = 0
        for index in range(len(ls)):
            init = 0
            if index <= right_max_index + data[right_max_index]:
                symmetry_idnex = 2*right_max_index - index
                # 中线往后的点，当前位置加对称点的半径仍然小于右边界可直接设值
                if index - right_max_index + data[symmetry_idnex] < data[right_max_index]:
                    data[index] = data[symmetry_idnex]
                    continue
                # 中线往后的点，当前位置加对称点的半径仍然等于右边界可以从对称点的半径开始计算
                elif index - right_max_index + data[symmetry_idnex] == data[right_max_index]:
                    init = data[symmetry_idnex]
                # 中线往后的点，当前位置加对称点的半径大于右边界，可以从右边界开始减去当前位置当作半径开始计算
                else:
                    init = right_max_index + data[right_max_index] - index
            while index - index >= 0 and init + index < len(ls):
                if ls[index-init] == ls[index+init]:
                    init += 1
                else:
                    break
            data[index] = init - 1
            if data[index] + index > data[right_max_index] + right_max_index:
                right_max_index = index
            if data[index] > data[max_index]:
                max_index = index
        
        return ls[max_index-data[max_index]:max_index+data[max_index]+1].replace("#", "")

    def __longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 马拉车算法
        # 将奇偶两种情况转换为一种情况来处理
        # Manacher's Algorithm
        # T(n) = O(n)
        # 最长子串的长度是半径减1，起始位置是中间位置减去半径再除以2。

        # 走一半力，借一半力，不能完全依赖之前的结果
        # 比如 ababababa
        # Wrong Answer
        if not s:
            return s

        ls = "$#"
        for i in s:
            ls += i
            ls += "#"
        ls += "&"
        data = {}

        max_index = 0
        right_max_index = 0
        data[right_max_index] = 0
        for index, _ in enumerate(ls):
            if index < right_max_index + data[right_max_index] / 2:
                    data[index] = data[right_max_index - (index - right_max_index)]
                    continue

            ts = self.checkSinglePalindromic(ls, index)
            data[index] = len(ts) / 2
            if index + data[index] > right_max_index + data[right_max_index]:
                right_max_index = index
                if data[right_max_index] > data[max_index]:
                    max_index = right_max_index
        return ls[max_index-data[max_index]:max_index+data[max_index]+1].replace("#","")

    def _longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # a little slow
        # T(n) = O(n * n)

        maxGroup = ""
        for i in range(len(s)):
            singleGroup = self.checkSinglePalindromic(s, i)
            if len(singleGroup) > len(maxGroup):
                maxGroup = singleGroup
            doubleGroup = self.checkDoublePalindromic(s, i)
            if len(doubleGroup) > len(maxGroup):
                maxGroup = doubleGroup
        return maxGroup

    def checkSinglePalindromic(self, s, index):
        group = s[index]
        for i in range(1, index+1):
            if index - i >= 0 and index + i < len(s):
                if s[index - i] == s[index + i]:
                    group = "{}{}{}".format(s[index - i], group, s[index + i])
                else:
                    return group
            else:
                break
        return group

    def checkDoublePalindromic(self, s, index):
        group = ""
        for i in range(index+1):
            if index - i >= 0 and index + i + 1 < len(s):
                if s[index - i] == s[index + i + 1]:
                    group = "{}{}{}".format(s[index - i], group, s[index + i + 1])
                else:
                    return group
            else:
                break
        return group

# if __name__ == "__main__":
#     s = Solution()
#     print s.longestPalindrome("babadada")
#     print s.longestPalindrome("ababababa")
#     test_case = ["", "abcdcef", "adaelele", "cabadabae", "aaaabcdefgfedcbaa", "aaba", "aaaaaaaaa"]
#     test_case = ["aaaaaaaaa"]
#     for t in test_case:
#         print s.longestPalindrome(t)
#         print 
