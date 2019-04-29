#
# @lc app=leetcode id=434 lang=python
#
# [434] Number of Segments in a String
#
# https://leetcode.com/problems/number-of-segments-in-a-string/description/
#
# algorithms
# Easy (36.66%)
# Total Accepted:    53.6K
# Total Submissions: 145.6K
# Testcase Example:  '"Hello, my name is John"'
#
# Count the number of segments in a string, where a segment is defined to be a
# contiguous sequence of non-space characters.
# 
# Please note that the string does not contain any non-printable characters.
# 
# Example:
# 
# Input: "Hello, my name is John"
# Output: 5
# 
# 
#
import string

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = 0
        res = 0
        while index < len(s):
            if s[index] == ' ':
                while index < len(s) and s[index] == ' ':
                    index += 1

            elif s[index] != ' ':
                res += 1
                while index < len(s) and s[index] != ' ':
                    index += 1
        
        return res

    def _countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())

if __name__ == "__main__":
    s = Solution()
    # print s.countSegments('""')
    # print s.countSegments(",,,, 1,43 13")
    # print s.countSegments('"        "')
    # print s._countSegments('"   "')
    print s.countSegments('"                "')
