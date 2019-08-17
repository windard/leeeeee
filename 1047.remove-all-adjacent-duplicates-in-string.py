# coding=utf-8
#
# @lc app=leetcode id=1047 lang=python
#
# [1047] Remove All Adjacent Duplicates In String
#
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
#
# algorithms
# Easy (63.77%)
# Likes:    184
# Dislikes: 18
# Total Accepted:    21.7K
# Total Submissions: 34K
# Testcase Example:  '"abbaca"'
#
# Given a string S of lowercase letters, a duplicate removal consists of
# choosing two adjacent and equal letters, and removing them.
# 
# We repeatedly make duplicate removals on S until we no longer can.
# 
# Return the final string after all such duplicate removals have been made.  It
# is guaranteed the answer is unique.
# 
# 
# 
# Example 1:
# 
# 
# Input: "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent
# and equal, and this is the only possible move.  The result of this move is
# that the string is "aaca", of which only "aa" is possible, so the final
# string is "ca".
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= S.length <= 20000
# S consists only of English lowercase letters.
# 
#


class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        while True:
            index = 0
            current = ""
            flag = False
            while index < len(S):
                if index < len(S) - 1:
                    if S[index] == S[index+1]:
                        index += 2
                        flag = True
                        continue
                current += S[index]
                index += 1

            if not flag:
                return current
            S = current


# if __name__ == "__main__":
#     s = Solution()
#     print s.removeDuplicates("abbaca")
#     print s.removeDuplicates("azxxzy")

