#
# @lc app=leetcode id=278 lang=python
#
# [278] First Bad Version
#
# https://leetcode.com/problems/first-bad-version/description/
#
# algorithms
# Easy (28.99%)
# Total Accepted:    210K
# Total Submissions: 717K
# Testcase Example:  '5\n4'
#
# You are a product manager and currently leading a team to develop a new
# product. Unfortunately, the latest version of your product fails the quality
# check. Since each version is developed based on the previous version, all the
# versions after a bad version are also bad.
# 
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first
# bad one, which causes all the following ones to be bad.
# 
# You are given an API bool isBadVersion(version) which will return whether
# version is bad. Implement a function to find the first bad version. You
# should minimize the number of calls to the API.
# 
# Example:
# 
# 
# Given n = 5, and version = 4 is the first bad version.
# 
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# 
# Then 4 is the first bad version. 
# 
#
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
#     if version >= 1:
#         return True
#     else:
#         return False

class Solution(object):
    def _firstBadVersion(self, n, start=0):
        """
        :type n: int
        :rtype: int
        """
        for i in range(start, n+1):
            if isBadVersion(i):
                return i

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        last = 0
        while 1:
            half = (last + n) / 2
            if isBadVersion(half):
                n = half
            else:
                last = half
            
            if n - last <= 2:
                return self._firstBadVersion(n, last)

# if __name__ == "__main__":
#     s = Solution()
#     print s.firstBadVersion(2)