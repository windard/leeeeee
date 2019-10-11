# coding=utf-8
#
# @lc app=leetcode id=165 lang=python
#
# [165] Compare Version Numbers
#
# https://leetcode.com/problems/compare-version-numbers/description/
#
# algorithms
# Medium (24.29%)
# Likes:    328
# Dislikes: 1165
# Total Accepted:    146.8K
# Total Submissions: 601.3K
# Testcase Example:  '"0.1"\n"1.1"'
#
# Compare two version numbers version1 and version2.
# If version1 > version2 return 1; if version1 < version2 return -1;otherwise
# return 0.
# 
# You may assume that the version strings are non-empty and contain only digits
# and the . character.
# The . character does not represent a decimal point and is used to separate
# number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it
# is the fifth second-level revision of the second first-level revision.
# You may assume the default revision number for each level of a version number
# to be 0. For example, version number 3.4 has a revision number of 3 and 4 for
# its first and second level revision number. Its third and fourth level
# revision number are both 0.
# 
# 
# 
# Example 1:
# 
# Input: version1 = "0.1", version2 = "1.1"
# Output: -1
# 
# Example 2:
# 
# Input: version1 = "1.0.1", version2 = "1"
# Output: 1
# 
# Example 3:
# 
# Input: version1 = "7.5.2.4", version2 = "7.5.3"
# Output: -1
# 
# Example 4:
# 
# Input: version1 = "1.01", version2 = "1.001"
# Output: 0
# Explanation: Ignoring leading zeroes, both “01” and “001" represent the same
# number “1”
# 
# Example 5:
# 
# Input: version1 = "1.0", version2 = "1.0.0"
# Output: 0
# Explanation: The first version number does not have a third level revision
# number, which means its third level revision number is default to "0"
# 
# 
# 
# Note:
# 
# Version strings are composed of numeric strings separated by dots . and this
# numeric strings may have leading zeroes. 
# Version strings do not start or end with dots, and they will not be two
# consecutive dots.
# 
#


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        va = map(int, version1.split("."))
        vb = map(int, version2.split("."))
        if len(va) < len(vb):
            va.extend([0] * (len(vb) - len(va)))
        else:
            vb.extend([0] * (len(va) - len(vb)))

        for i in range(len(va)):
            if va[i] > vb[i]:
                return 1
            elif va[i] < vb[i]:
                return -1
        return 0


# if __name__ == '__main__':
#     s = Solution()
#     print s.compareVersion("0.1", "1.1")
#     print s.compareVersion("1.0.1", "1")
#     print s.compareVersion("1.0.1", "1.1")
#     print s.compareVersion("7.5.2.4", "7.5.3")
#     print s.compareVersion("1.01", "1.01")
#     print s.compareVersion("1.1", "1.11")
#     print s.compareVersion("1.8", "1.11")
