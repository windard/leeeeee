# coding=utf-8
#
# @lc app=leetcode id=57 lang=python
#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Hard (31.61%)
# Likes:    955
# Dislikes: 124
# Total Accepted:    189.9K
# Total Submissions: 600.2K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
# 
# You may assume that the intervals were initially sorted according to their
# start times.
# 
# Example 1:
# 
# 
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with
# [3,5],[6,7],[8,10].
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#


class Solution(object):
    def _insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        index = 0
        count = 0
        length = len(intervals)
        while count < length:
            if intervals[index][1] < newInterval[0]:
                index += 1
                count += 1
            else:
                if newInterval[1] < intervals[index][0]:
                    intervals.insert(index, newInterval)
                    return intervals
                intervals[index][0] = min(intervals[index][0], newInterval[0])
                intervals[index][1] = max(intervals[index][1], newInterval[1])
                arrive = index
                count += 1
                index += 1
                while count < length:
                    if intervals[index][0] <= intervals[arrive][1]:
                        intervals[arrive][1] = max(intervals[arrive][1], intervals[index][1])
                        intervals.pop(index)
                        count += 1
                    else:
                        break
                return intervals
        intervals.append(newInterval)
        return intervals

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # 不用考虑各种各样的情况
        # 先插入，再排序，再归并
        # 化简为 @56
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x: x[0])

        result = []
        for interval in intervals:
            if result and result[-1][1] >= interval[0]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        return result

# if __name__ == '__main__':
#     s = Solution()
#     print s.insert([[1,3],[6,9]], [2,5])
#     print s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
#     print s.insert([[1,5],[6,8]], [5,6])
#     print s.insert([[1,5]], [0,3])
#     print s.insert([[1,5]], [0,0])
