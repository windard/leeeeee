# coding=utf-8
#
# @lc app=leetcode id=435 lang=python
#
# [435] Non-overlapping Intervals
#
# https://leetcode.com/problems/non-overlapping-intervals/description/
#
# algorithms
# Medium (41.83%)
# Likes:    565
# Dislikes: 25
# Total Accepted:    45.4K
# Total Submissions: 108.4K
# Testcase Example:  '[[1,2]]'
#
# Given a collection of intervals, find the minimum number of intervals you
# need to remove to make the rest of the intervals non-overlapping.
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of intervals are
# non-overlapping.
# 
# 
# Example 2:
# 
# 
# Input: [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of intervals
# non-overlapping.
# 
# 
# Example 3:
# 
# 
# Input: [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're
# already non-overlapping.
# 
# 
# 
# 
# Note:
# 
# 
# You may assume the interval's end point is always bigger than its start
# point.
# Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap
# each other.
# 
# 
#


class Solution(object):
    def __eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # dp
        # 应该是存储最多可以共存的区间数
        # Time Limit
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        nums = [0] * len(intervals)
        for i in range(len(intervals)):
            count = 0
            for j in range(i):
                if intervals[i][0] >= intervals[j][1]:
                    count = max(count, nums[j])
            nums[i] = max(count + 1, max(nums))
        return len(intervals) - nums[-1]

    def ___eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # dp 错误
        flag = [0] * len(intervals)
        for i in range(1, len(intervals)):
            count = float("inf")
            for j in range(i):
                if intervals[i][0] < intervals[j][1]:
                    count = min(flag[j]+1, count)
                else:
                    count = min(flag[j], count)
            flag[i] = count
        return flag[-1]

    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[1])
        print intervals
        last = count = 0
        index = 1
        while index < len(intervals):
            if intervals[last][1] > intervals[index][0]:
                count += 1
            else:
                last = index
            index += 1
        return count

    def _eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # Wrong Answer
        intervals.sort(key=lambda x: x[1])
        intervals.sort(key=lambda x: x[0])
        # print intervals
        last = 0
        index = 1
        count = 0
        while index < len(intervals):
            if intervals[last][0] == intervals[index][0]:
                count += 1
            elif intervals[last][1] > intervals[index][0]:
                count += 1
            else:
                last = index
            index += 1
        return count


# if __name__ == '__main__':
#     s = Solution()
#     print s.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]])
#     print s.eraseOverlapIntervals([[-100,-87],[-99,-44],[-98,-19],[-97,-33],[-96,-60],[-95,-17],[-94,-44],[-93,-9],[-92,-63],[-91,-76],[-90,-44],[-89,-18],[-88,10],[-87,-39],[-86,7],[-85,-76],[-84,-51],[-83,-48],[-82,-36],[-81,-63],[-80,-71],[-79,-4],[-78,-63],[-77,-14],[-76,-10],[-75,-36],[-74,31],[-73,11],[-72,-50],[-71,-30],[-70,33],[-69,-37],[-68,-50],[-67,6],[-66,-50],[-65,-26],[-64,21],[-63,-8],[-62,23],[-61,-34],[-60,13],[-59,19],[-58,41],[-57,-15],[-56,35],[-55,-4],[-54,-20],[-53,44],[-52,48],[-51,12],[-50,-43],[-49,10],[-48,-34],[-47,3],[-46,28],[-45,51],[-44,-14],[-43,59],[-42,-6],[-41,-32],[-40,-12],[-39,33],[-38,17],[-37,-7],[-36,-29],[-35,24],[-34,49],[-33,-19],[-32,2],[-31,8],[-30,74],[-29,58],[-28,13],[-27,-8],[-26,45],[-25,-5],[-24,45],[-23,19],[-22,9],[-21,54],[-20,1],[-19,81],[-18,17],[-17,-10],[-16,7],[-15,86],[-14,-3],[-13,-3],[-12,45],[-11,93],[-10,84],[-9,20],[-8,3],[-7,81],[-6,52],[-5,67],[-4,18],[-3,40],[-2,42],[-1,49],[0,7],[1,104],[2,79],[3,37],[4,47],[5,69],[6,89],[7,110],[8,108],[9,19],[10,25],[11,48],[12,63],[13,94],[14,55],[15,119],[16,64],[17,122],[18,92],[19,37],[20,86],[21,84],[22,122],[23,37],[24,125],[25,99],[26,45],[27,63],[28,40],[29,97],[30,78],[31,102],[32,120],[33,91],[34,107],[35,62],[36,137],[37,55],[38,115],[39,46],[40,136],[41,78],[42,86],[43,106],[44,66],[45,141],[46,92],[47,132],[48,89],[49,61],[50,128],[51,155],[52,153],[53,78],[54,114],[55,84],[56,151],[57,123],[58,69],[59,91],[60,89],[61,73],[62,81],[63,139],[64,108],[65,165],[66,92],[67,117],[68,140],[69,109],[70,102],[71,171],[72,141],[73,117],[74,124],[75,171],[76,132],[77,142],[78,107],[79,132],[80,171],[81,104],[82,160],[83,128],[84,137],[85,176],[86,188],[87,178],[88,117],[89,115],[90,140],[91,165],[92,133],[93,114],[94,125],[95,135],[96,144],[97,114],[98,183],[99,157]])
#     print s.eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]])
#     print s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])
#     print s.eraseOverlapIntervals([[1,3],[2,3],[3,4],[1,2]])
