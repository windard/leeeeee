# coding=utf-8
#
# @lc app=leetcode id=1010 lang=python
#
# [1010] Pairs of Songs With Total Durations Divisible by 60
#
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/
#
# algorithms
# Easy (45.72%)
# Likes:    198
# Dislikes: 16
# Total Accepted:    15.3K
# Total Submissions: 33.5K
# Testcase Example:  '[30,20,150,100,40]'
#
# In a list of songs, the i-th song has a duration of time[i] seconds. 
# 
# Return the number of pairs of songs for which their total duration in seconds
# is divisible by 60.  Formally, we want the number of indices i < j with
# (time[i] + time[j]) % 60 == 0.
# 
# 
# 
# Example 1:
# 
# 
# Input: [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60
# 
# 
# 
# Example 2:
# 
# 
# Input: [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible
# by 60.
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= time.length <= 60000
# 1 <= time[i] <= 500
# 
#


class Solution(object):
    def _numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        # Time Limit
        count = 0
        for i in range(len(time)):
            for j in range(i+1, len(time)):
                if not (time[i] + time[j]) % 60:
                    count += 1
        return count

    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        data = {}
        for t in time:
            t = t % 60
            data[t] = data.get(t, 0) + 1
        count = 0
        zero = data.get(0)
        if zero and zero > 1:
            count += zero * (zero - 1) / 2
        zero = data.get(30)
        if zero and zero > 1:
            count += zero * (zero - 1) / 2
        for i in range(1, 30):
            count += data.get(i, 0) * data.get(60-i, 0)
        return count
        # HashMap

