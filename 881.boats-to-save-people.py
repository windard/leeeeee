#
# @lc app=leetcode id=881 lang=python
#
# [881] Boats to Save People
#
# https://leetcode.com/problems/boats-to-save-people/description/
#
# algorithms
# Medium (42.90%)
# Total Accepted:    12.4K
# Total Submissions: 28.9K
# Testcase Example:  '[1,2]\n3'
#
# The i-th person has weight people[i], and each boat can carry a maximum
# weight of limit.
# 
# Each boat carries at most 2 people at the same time, provided the sum of the
# weight of those people is at most limit.
# 
# Return the minimum number of boats to carry every given person.  (It is
# guaranteed each person can be carried by a boat.)
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)
# 
# 
# 
# Example 2:
# 
# 
# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)
# 
# 
# 
# Example 3:
# 
# 
# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)
# 
# Note:
# 
# 
# 1 <= people.length <= 50000
# 1 <= people[i] <= limit <= 30000
# 
# 
# 
# 
# 
#
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        # 两人乘船问题就是贪心算法
        # 三人或更多，则是回溯加贪心算法
        people.sort()
        first = 0
        last = len(people) - 1
        times = 0
        while first <= last:
            if last == first:
                times += 1
                break
            if people[first] + people[last] <= limit:
                times += 1
                first += 1
                last  -= 1
            elif people[first] > limit:
                times += last - first
            else:
                times += 1
                last -= 1
        return times
