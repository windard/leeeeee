# coding=utf-8
#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (48.52%)
# Likes:    1949
# Dislikes: 126
# Total Accepted:    385.1K
# Total Submissions: 788.4K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
# 
# Example:
# 
# 
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# Note:
# 
# 
# All inputs will be in lowercase.
# The order of your output does not matter.
# 
# 
#


class HashDict(dict):

    @classmethod
    def fromstr(cls, strs):
        d = HashDict()
        for s in strs:
            d[s] = d.get(s, 0) + 1
        return d

    def __hash__(self):
        hashstr = ""
        for key, value in sorted(self.items()):
            hashstr += "{}{}".format(key, value)
        return hash(hashstr)


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        data = defaultdict(list)
        for s in strs:
            data[HashDict.fromstr(s)].append(s)
        return data.values()


# if __name__ == '__main__':
#     s = Solution()
#     print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
#     print s.groupAnagrams(["cab","pug","pei","nay","ron","rae","ems","ida","mes"])
