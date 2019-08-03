#
# @lc app=leetcode id=319 lang=python
#
# [319] Bulb Switcher
#
# https://leetcode.com/problems/bulb-switcher/description/
#
# algorithms
# Medium (43.64%)
# Likes:    287
# Dislikes: 652
# Total Accepted:    61.5K
# Total Submissions: 139.3K
# Testcase Example:  '3'
#
# There are n bulbs that are initially off. You first turn on all the bulbs.
# Then, you turn off every second bulb. On the third round, you toggle every
# third bulb (turning on if it's off or turning off if it's on). For the i-th
# round, you toggle every i bulb. For the n-th round, you only toggle the last
# bulb. Find how many bulbs are on after n rounds.
# 
# Example:
# 
# 
# Input: 3
# Output: 1 
# Explanation: 
# At first, the three bulbs are [off, off, off].
# After first round, the three bulbs are [on, on, on].
# After second round, the three bulbs are [on, off, on].
# After third round, the three bulbs are [on, off, off]. 
# 
# So you should return 1, because there is only one bulb is on.
# 
# 
#

import math

class Solution(object):
    def _bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time Limit
        lights = [True] * n
        for i in range(1, n):
            for j in range(i, n, i+1):
                lights[j] = not lights[j]
        return sum(filter(bool, lights))

    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 偶数次的操作，结果就是关闭
        # 1*15 = 15*1
        # 即第一轮的第15个，和第15轮的第一个都是同一个灯，最终被关闭
        # 4*4 = 4*4 = 16
        # 只有第十六个灯，才会亮到最后
        # 对于16个灯来说，同样的 1*1=1 2*2=4 3*3=9 也会亮到最后
        # 亮灯的有 1，4，9，16 四个灯

        return int(math.sqrt(n))

# if __name__ == "__main__":
#     s = Solution()
#     print s.bulbSwitch(3)
