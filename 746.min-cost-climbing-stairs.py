#
# @lc app=leetcode id=746 lang=python
#
# [746] Min Cost Climbing Stairs
#
# https://leetcode.com/problems/min-cost-climbing-stairs/description/
#
# algorithms
# Easy (45.67%)
# Total Accepted:    64.9K
# Total Submissions: 141.6K
# Testcase Example:  '[0,0,0,0]'
#
# 
# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0
# indexed).
# 
# Once you pay the cost, you can either climb one or two steps. You need to
# find minimum cost to reach the top of the floor, and you can either start
# from the step with index 0, or the step with index 1.
# 
# 
# Example 1:
# 
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: Cheapest is start on cost[1], pay that cost and go to the
# top.
# 
# 
# 
# Example 2:
# 
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: Cheapest is start on cost[0], and only step on 1s, skipping
# cost[3].
# 
# 
# 
# Note:
# 
# cost will have a length in the range [2, 1000].
# Every cost[i] will be an integer in the range [0, 999].
# 
# 
#
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # dp
        cost_list = [0] * (len(cost)+1)
        for i in range(2, len(cost_list)):
            cost_list[i] = min(cost[i-1]+cost_list[i-1], cost[i-2]+cost_list[i-2])
        return cost_list[len(cost)]

    def __minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # Time Limit 
        # need Cache
        return self.minCost(cost, len(cost))

    def minCost(self, cost, n):
        if n < 2:
            return 0
        return min(self.minCost(cost, n-2)+cost[n-2], self.minCost(cost, n-1)+cost[n-1])

    def _minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # [1,100,110,1] 
        # Wrong Answer [1,0,2,2]
        n = -1
        s = 0
        size = len(cost)
        cost.extend([0, 0, 0, 0, 0])
        while n < size:
            s1 = cost[n + 1] + min(cost[n+1+1], cost[n+1+2])
            s2 = cost[n + 2] + min(cost[n+2+1], cost[n+2+2])
            if s1 < s2:
                n += 1
                s += cost[n]
            else:
                n += 2
                s += cost[n]
        return s

# if __name__ == "__main__":
#     s = Solution()
#     print s.minCostClimbingStairs([1,100,110,1])
#     print s.minCostClimbingStairs([1,0,2,2])
#     print s.minCostClimbingStairs([10, 15, 20])
#     print s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])