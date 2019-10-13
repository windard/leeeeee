# coding=utf-8
#
# @lc app=leetcode id=134 lang=python
#
# [134] Gas Station
#
# https://leetcode.com/problems/gas-station/description/
#
# algorithms
# Medium (34.65%)
# Likes:    864
# Dislikes: 305
# Total Accepted:    156.1K
# Total Submissions: 448.3K
# Testcase Example:  '[1,2,3,4,5]\n[3,4,5,1,2]'
#
# There are N gas stations along a circular route, where the amount of gas at
# station i is gas[i].
# 
# You have a car with an unlimited gas tank and it costs cost[i] of gas to
# travel from station i to its next station (i+1). You begin the journey with
# an empty tank at one of the gas stations.
# 
# Return the starting gas station's index if you can travel around the circuit
# once in the clockwise direction, otherwise return -1.
# 
# Note:
# 
# 
# If there exists a solution, it is guaranteed to be unique.
# Both input arrays are non-empty and have the same length.
# Each element in the input arrays is a non-negative integer.
# 
# 
# Example 1:
# 
# 
# Input: 
# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]
# 
# Output: 3
# 
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 +
# 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to
# station 3.
# Therefore, return 3 as the starting index.
# 
# 
# Example 2:
# 
# 
# Input: 
# gas  = [2,3,4]
# cost = [3,4,3]
# 
# Output: -1
# 
# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to
# the next station.
# Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 =
# 4
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you
# only have 3.
# Therefore, you can't travel around the circuit once no matter where you
# start.
# 
# 
#


class Solution(object):
    def _canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # O(n^2)
        if sum(gas) < sum(cost):
            return -1
        fuel = map(lambda x: x[0]-x[1], zip(gas, cost))
        for index, f in enumerate(fuel):
            if f >= 0:
                if self.check_arrive(index, gas, cost):
                    return index
        return -1

    def check_arrive(self, index, gas, cost):
        length = len(gas)
        start = index
        total = gas[start]
        total -= cost[start]
        start = (start + 1) % length
        while start != index:
            total += gas[start]
            total -= cost[start]
            if total < 0:
                return False
            start = (start + 1) % length

        return True

    def __canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # O(n)
        # Wrong Answer
        # 可能会陷入死循环
        length = len(gas)
        total = 0
        index = 0
        target = len(gas) - 1
        while True:
            total += gas[index]
            total -= cost[index]
            if total < 0:
                target = index
                total = 0
            index = (index + 1) % length
            if index == target:
                total += gas[index]
                total -= cost[index]

                if total < 0:
                    return -1
                else:
                    return (target + 1) % length

    def __canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # Same With @53
        # 可以化简为 求最大子数组问题？
        total = 0
        box = 0
        result = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if box > 0:
                box += gas[i] - cost[i]
            else:
                box = gas[i] - cost[i]
                result = i
        return result if total >= 0 else -1

    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # 可是这到底是为什么呢？
        box = total = 0
        result = 0
        length = len(gas)
        for i in range(length):
            total += gas[i] - cost[i]
            box += gas[i] - cost[i]
            if box < 0:
                box = 0
                result = (i + 1) % length
        return result if total >= 0 else -1

#
# if __name__ == '__main__':
#     s = Solution()
#     print s.canCompleteCircuit([1,2,3,4,3,2,4,1,5,3,2,4], [1,1,1,3,2,4,3,6,7,4,3,1])
#     print s.canCompleteCircuit([2], [2])
#     print s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])
#     print s.canCompleteCircuit([2,3,4], [3,4,3])
