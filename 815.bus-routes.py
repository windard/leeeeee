# coding=utf-8
#
# @lc app=leetcode id=815 lang=python
#
# [815] Bus Routes
#
# https://leetcode.com/problems/bus-routes/description/
#
# algorithms
# Hard (40.48%)
# Likes:    470
# Dislikes: 18
# Total Accepted:    23.9K
# Total Submissions: 58.8K
# Testcase Example:  '[[1,2,7],[3,6,7]]\n1\n6'
#
# We have a list of bus routes. Each routes[i] is a bus route that the i-th bus
# repeats forever. For example if routes[0] = [1, 5, 7], this means that the
# first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->...
# forever.
# 
# We start at bus stop S (initially not on a bus), and we want to go to bus
# stop T. Travelling by buses only, what is the least number of buses we must
# take to reach our destination? Return -1 if it is not possible.
# 
# 
# Example:
# Input: 
# routes = [[1, 2, 7], [3, 6, 7]]
# S = 1
# T = 6
# Output: 2
# Explanation: 
# The best strategy is take the first bus to the bus stop 7, then take the
# second bus to the bus stop 6.
# 
# 
# Note: 
# 
# 
# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 500.
# 0 <= routes[i][j] < 10 ^ 6.
# 
# 
#


class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        # BFS
        # 广度优先遍历
        # DP
        # 动态规划也可以做
        if S == T:
            return 0
        from collections import defaultdict
        station_to_bus = defaultdict(list)
        for key, route in enumerate(routes):
            for station in route:
                station_to_bus[station].append(key)

        start_bus = station_to_bus.get(S)
        end_bus = station_to_bus.get(T)
        if not start_bus or not end_bus:
            return -1
        start_bus = set(start_bus)
        end_bus = set(end_bus)

        count = 1
        if start_bus & end_bus:
            return count
        visited_stations = set()
        while True:
            visited_bus = set()
            for bus in start_bus:
                for station in routes[bus]:
                    visited_stations.add(station)
            for station in visited_stations:
                for bus in station_to_bus[station]:
                    visited_bus.add(bus)
            count += 1
            if visited_bus & end_bus:
                return count
            if visited_bus == start_bus:
                return -1
            start_bus = visited_bus


# if __name__ == '__main__':
#     s = Solution()
#     print s.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6)
#     print s.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 7)
