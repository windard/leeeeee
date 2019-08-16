# coding=utf-8
#
# @lc app=leetcode id=830 lang=python
#
# [830] Positions of Large Groups
#
# https://leetcode.com/problems/positions-of-large-groups/description/
#
# algorithms
# Easy (47.46%)
# Likes:    224
# Dislikes: 56
# Total Accepted:    29.6K
# Total Submissions: 61.5K
# Testcase Example:  '"abbxxxxzzy"'
#
# In a string S of lowercase letters, these letters form consecutive groups of
# the same character.
# 
# For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx",
# "z" and "yy".
# 
# Call a group large if it has 3 or more characters.  We would like the
# starting and ending positions of every large group.
# 
# The final answer should be in lexicographic order.
# 
# 
# 
# Example 1:
# 
# 
# Input: "abbxxxxzzy"
# Output: [[3,6]]
# Explanation: "xxxx" is the single large group with starting  3 and ending
# positions 6.
# 
# 
# Example 2:
# 
# 
# Input: "abc"
# Output: []
# Explanation: We have "a","b" and "c" but no large group.
# 
# 
# Example 3:
# 
# 
# Input: "abcdddeeeeaabbbcd"
# Output: [[3,5],[6,9],[12,14]]
# 
# 
# 
# Note:  1 <= S.length <= 1000
# 
#


class Solution(object):
    def _largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        last = None
        index = 1
        result = []
        for i, s in enumerate(S):
            if s == last:
                index += 1
            else:
                if index >= 3:
                    result.append([i-index, i-1])
                index = 1
            last = s

        if s == last:
            index += 1
        if index > 3:
            result.append([i - index + 2, i])
        return result

    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        if len(S) < 3:
            return []
        index = 1
        count = 1
        result = []
        while index < len(S):
            if S[index] == S[index-1]:
                count += 1
            else:
                if count >= 3:
                    result.append([index-count, index-1])
                count = 1
            index += 1
        if count >= 3:
            result.append([index-count, index-1])
        return result


# if __name__ == '__main__':
#     s = Solution()
#     print s.largeGroupPositions("abbxxxxzzy")
#     print s.largeGroupPositions("abc")
#     print s.largeGroupPositions("abcdddeeeeaabbbcd")
#     print s.largeGroupPositions("aaaaaaa")
#     print s.largeGroupPositions("aaa")
