# coding=utf-8
#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (34.85%)
# Likes:    2390
# Dislikes: 185
# Total Accepted:    386.1K
# Total Submissions: 1.1M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
# 
# Example 1:
# 
# 
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#


class Solution(object):
    def _merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # Wrong Answer
        # [[1,4],[0,0]]
        nums = []
        for interval in intervals:
            if len(nums) < interval[1]:
                nums += [0] * (interval[1] - len(nums))
            for i in range(interval[0], interval[1]):
                nums[i] = 1
        
        result = []
        index = 0
        start = 0
        flag = False
        while index < len(nums):
            if nums[index]:
                if not flag:
                    flag = True
                    start = index
            else:
                if flag:
                    result.append([start, index])
                    flag = False
            index += 1
        if flag:
            result.append([start, index])
        return result

    def __merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # Brute Force
        # O(n^2)

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # 先排序，再合并区间
        result = []
        intervals = sorted(intervals, key=lambda x: x[0])
        for interval in intervals:
            if result and result[-1][1] >= interval[0]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        return result


# if __name__ == '__main__':
#     s = Solution()
#     print s.merge([[1,3],[2,6],[8,10],[15,18]])
#     print s.merge([[1,4],[4,5]])
#     print s.merge([[1,4],[5,6]])
#     print s.merge([[1,4],[0,0]])
