#
# @lc app=leetcode id=551 lang=python
#
# [551] Student Attendance Record I
#
# https://leetcode.com/problems/student-attendance-record-i/description/
#
# algorithms
# Easy (45.14%)
# Likes:    150
# Dislikes: 599
# Total Accepted:    52.4K
# Total Submissions: 115.6K
# Testcase Example:  '"PPALLP"'
#
# You are given a string representing an attendance record for a student. The
# record only contains the following three characters:
# 
# 
# 
# 'A' : Absent. 
# 'L' : Late.
# ⁠'P' : Present. 
# 
# 
# 
# 
# A student could be rewarded if his attendance record doesn't contain more
# than one 'A' (absent) or more than two continuous 'L' (late).    
# 
# You need to return whether the student could be rewarded according to his
# attendance record.
# 
# Example 1:
# 
# Input: "PPALLP"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "PPALLL"
# Output: False
# 
# 
# 
# 
# 
#

import re

class Solution(object):
    def _checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return len(re.findall('A', s)) <= 1 and len(re.findall('LLL', s)) < 1

    def __checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        al = False
        bp = 0
        for i in s:
            if i == 'A':
                if al:
                    return False
                else:
                    al = True
                bp = 0
            elif i == 'L':
                if bp > 1:
                    return False
                else:
                    bp += 1
            else:
                bp = 0
        return True

    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s.count('A') <= 1 and 'LLL' not in s
