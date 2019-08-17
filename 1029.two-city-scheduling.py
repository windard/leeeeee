# coding=utf-8
#
# @lc app=leetcode id=1029 lang=python
#
# [1029] Two City Scheduling
#
# https://leetcode.com/problems/two-city-scheduling/description/
#
# algorithms
# Easy (54.38%)
# Likes:    280
# Dislikes: 32
# Total Accepted:    12.3K
# Total Submissions: 22.6K
# Testcase Example:  '[[10,20],[30,200],[400,50],[30,20]]'
#
# There are 2N people a company is planning to interview. The cost of flying
# the i-th person to city A is costs[i][0], and the cost of flying the i-th
# person to city B is costs[i][1].
# 
# Return the minimum cost to fly every person to a city such that exactly N
# people arrive in each city.
# 
# 
# 
# Example 1:
# 
# 
# Input: [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation: 
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.
# 
# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people
# interviewing in each city.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= costs.length <= 100
# It is guaranteed that costs.length is even.
# 1 <= costs[i][0], costs[i][1] <= 1000
# 
#


class Solution(object):
    def _twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # 思路错误
        # 结果错误
        # [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
        order_a = sorted(costs, key=lambda x: x[0])
        order_b = sorted(costs, key=lambda x: x[1])
        N = len(costs) / 2
        used = []
        index_a = index_b = 0
        count = 0
        count_a = count_b = 0
        while count_a < N or count_b < N:

            while index_a < N * 2 and order_a[index_a] in used:
                index_a += 1
            while index_b < N * 2 and order_b[index_b] in used:
                index_b += 1

            if count_a >= N or index_a >= N * 2:
                count += order_b[index_b][1]
                used.append(order_b[index_b])
                index_b += 1
                count_b += 1
                continue
            elif count_b >= N or index_b >= N * 2:
                count += order_a[index_a][0]
                used.append(order_a[index_a])
                index_a += 1
                count_a += 1
                continue

            if order_a[index_a][0] < order_b[index_b][1]:
                count += order_a[index_a][0]
                used.append(order_a[index_a])
                index_a += 1
                count_a += 1
            else:
                count += order_b[index_b][1]
                used.append(order_b[index_b])
                index_b += 1
                count_b += 1

        return count

    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        order = sorted(costs, key=lambda x: x[0] - x[1])
        count = 0
        for i,v in enumerate(order):
            if i >= len(costs) / 2:
                count += order[i][1]
            else:
                count += order[i][0]
        return count
#
#
# if __name__ == '__main__':
#     s = Solution()
#     print s.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]])
#     print s.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]])
