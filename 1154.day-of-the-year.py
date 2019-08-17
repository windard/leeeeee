# coding=utf-8
#
# @lc app=leetcode id=1154 lang=python
#
# [1154] Day of the Year
#
# https://leetcode.com/problems/day-of-the-year/description/
#
# algorithms
# Easy (51.18%)
# Likes:    23
# Dislikes: 35
# Total Accepted:    5.8K
# Total Submissions: 11.5K
# Testcase Example:  '"2019-01-09"\r'
#
# Given a string date representing a Gregorian calendar date formatted as
# YYYY-MM-DD, return the day number of the year.
# 
# 
# Example 1:
# 
# 
# Input: date = "2019-01-09"
# Output: 9
# Explanation: Given date is the 9th day of the year in 2019.
# 
# 
# Example 2:
# 
# 
# Input: date = "2019-02-10"
# Output: 41
# 
# 
# Example 3:
# 
# 
# Input: date = "2003-03-01"
# Output: 60
# 
# 
# Example 4:
# 
# 
# Input: date = "2004-03-01"
# Output: 61
# 
# 
# 
# Constraints:
# 
# 
# date.length == 10
# date[4] == date[7] == '-', and all other date[i]'s are digits
# date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.
# 
# 
#

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        year, month, day = date.split("-")
        is_leap_year = self.isLeapYear(int(year))
        count = 0
        for i in range(int(month)-1):
            if is_leap_year:
                count += leap_days[i]
            else:
                count += days[i]
        return count + int(day)

    def isLeapYear(self, year):
        return bool((not year % 4 and year % 100) or (not year % 400))


# if __name__ == '__main__':
#     s = Solution()
#     print s.isLeapYear(1900)
#     print s.isLeapYear(2000)
#     print s.isLeapYear(2004)
#     print s.dayOfYear("2019-01-09")
#     print s.dayOfYear("2019-02-10")
#     print s.dayOfYear("2003-03-01")
#     print s.dayOfYear("2004-03-01")
