# coding=utf-8
#
# @lc app=leetcode id=686 lang=python
#
# [686] Repeated String Match
#
# https://leetcode.com/problems/repeated-string-match/description/
#
# algorithms
# Easy (31.32%)
# Likes:    525
# Dislikes: 518
# Total Accepted:    71.8K
# Total Submissions: 227.2K
# Testcase Example:  '"abcd"\n"cdabcdab"'
#
# Given two strings A and B, find the minimum number of times A has to be
# repeated such that B is a substring of it. If no such solution, return -1.
# 
# For example, with A = "abcd" and B = "cdabcdab".
# 
# Return 3, because by repeating A three times (“abcdabcdabcd”), B is a
# substring of it; and B is not a substring of A repeated two times
# ("abcdabcd").
# 
# Note:
# The length of A and B will be between 1 and 10000.
# 
#
class Solution(object):
    def _repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        index = 1
        repeat = A
        while True:
            if B in repeat:
                return index
            if len(repeat) > len(B)*2 and index > 5:
                return -1
            index += 1
            repeat += A

    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        # Wrong Answer
        if B in A:
            return 1
        import math
        if A in B:
            mi = int(math.ceil(len(B) / float(len(A))))
            if B in mi*A:
                return mi
            elif B in (mi+1)*A:
                return mi+1
            return -1
        if B in 2*A:
            return 2
        return -1

# if __name__ == "__main__":
#     s = Solution()
#     print s.repeatedStringMatch("aa", "a")
#     print s.repeatedStringMatch("abcd", "abcdb")
#     print s.repeatedStringMatch("cdabcdab", "abcd")
#     print s.repeatedStringMatch("aaaaaaaaaaaaaaaaaaaaaab", "ba")
