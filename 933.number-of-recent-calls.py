# coding=utf-8
#
# @lc app=leetcode id=933 lang=python
#
# [933] Number of Recent Calls
#
# https://leetcode.com/problems/number-of-recent-calls/description/
#
# algorithms
# Easy (69.42%)
# Likes:    152
# Dislikes: 788
# Total Accepted:    27K
# Total Submissions: 38.8K
# Testcase Example:  '["RecentCounter","ping","ping","ping","ping"]\n[[],[1],[100],[3001],[3002]]'
#
# Write a class RecentCounter to count recent requests.
# 
# It has only one method: ping(int t), where t represents some time in
# milliseconds.
# 
# Return the number of pings that have been made from 3000 milliseconds ago
# until now.
# 
# Any ping with time in [t - 3000, t] will count, including the current ping.
# 
# It is guaranteed that every call to ping uses a strictly larger value of t
# than before.
# 
# 
# 
# Example 1:
# 
# 
# Input: inputs = ["RecentCounter","ping","ping","ping","ping"], inputs =
# [[],[1],[100],[3001],[3002]]
# Output: [null,1,2,3,3]
# 
# 
# 
# Note:
# 
# 
# Each test case will have at most 10000 calls to ping.
# Each test case will call ping with strictly increasing values of t.
# Each call to ping will have 1 <= t <= 10^9.
# 
# 
# 
# 
# 
#
class RecentCounter(object):

    def __init__(self):
        self.times = []
        self.count = 0

    def _ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        # Time Limit
        self.times.append(t)
        self.times = filter(lambda x: t-x<=3000, self.times)
        return len(self.times)

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.times.append(t)
        self.count += 1
        while True:
            if t - self.times[0] <= 3000:
                break
            self.times.pop(0)
            self.count -= 1
        return self.count


# Your RecentCounter object will be instantiated and called as such:
# if __name__ == "__main__":
#     obj = RecentCounter()
#     print obj.ping(642)
#     print obj.ping(1849)
#     print obj.ping(4921)

