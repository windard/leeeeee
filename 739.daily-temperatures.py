# coding=utf-8
#
# @lc app=leetcode id=739 lang=python
#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (60.44%)
# Likes:    1665
# Dislikes: 49
# Total Accepted:    94.6K
# Total Submissions: 155.5K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# 
# Given a list of daily temperatures T, return a list such that, for each day
# in the input, tells you how many days you would have to wait until a warmer
# temperature.  If there is no future day for which this is possible, put 0
# instead.
# 
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76,
# 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
# 
# 
# Note:
# The length of temperatures will be in the range [1, 30000].
# Each temperature will be an integer in the range [30, 100].
# 
#

# @lc code=start


class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        # 单调栈
        # 单调递减的单调栈
        # 争取一次过
        if not T:
            return []
        temperature = []
        result = [0] * len(T)
        for i, t in enumerate(T):
            if not i:
                temperature.append(i)
            else:
                while temperature:
                    top = temperature[-1]
                    if T[top] >= t:
                        break
                    else:
                        result[top] = i - top
                        temperature.pop()
                temperature.append(i)

        return result

        
# @lc code=end

