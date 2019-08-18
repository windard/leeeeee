# coding=utf-8
#
# @lc app=leetcode id=942 lang=python
#
# [942] DI String Match
#
# https://leetcode.com/problems/di-string-match/description/
#
# algorithms
# Easy (69.98%)
# Likes:    493
# Dislikes: 178
# Total Accepted:    38.6K
# Total Submissions: 55.2K
# Testcase Example:  '"IDID"'
#
# Given a string S that only contains "I" (increase) or "D" (decrease), let N =
# S.length.
# 
# Return any permutation A of [0, 1, ..., N] such that for all i = 0, ...,
# N-1:
# 
# 
# If S[i] == "I", then A[i] < A[i+1]
# If S[i] == "D", then A[i] > A[i+1]
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: "IDID"
# Output: [0,4,1,3,2]
# 
# 
# 
# Example 2:
# 
# 
# Input: "III"
# Output: [0,1,2,3]
# 
# 
# 
# Example 3:
# 
# 
# Input: "DDI"
# Output: [3,2,0,1]
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= S.length <= 10000
# S only contains characters "I" or "D".
# 
#


class Solution(object):
    def _diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # 上升时，让最大值占领最高的山峰
        # 下降时，让最小值占领最低的峡谷
        # 可以从前往后，也可以从后往前
        # 从后往前方便一些
        result = []
        max_val = len(S)
        index = len(S) - 1
        min_val = 0
        while index >= 0:
            if S[index] == 'I':
                result.insert(0, max_val)
                max_val -= 1
            else:
                result.insert(0, min_val)
                min_val += 1
            index -= 1
        result.insert(0, (max_val + min_val) / 2)
        return result

    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # 从前往后，还有一个类似的思路
        # 遇到增长的就取当前最小值，遇到下降的就取当前最大值
        result = []
        max_val = len(S)
        index = 0
        min_val = 0
        while index < len(S):
            if S[index] == 'I':
                result.append(min_val)
                min_val += 1
            else:
                result.append(max_val)
                max_val -= 1
            index += 1
        result.append(min_val)
        return result


# if __name__ == '__main__':
#     s = Solution()
#     print s.diStringMatch("IDID")
