# coding=utf-8
#
# @lc app=leetcode id=452 lang=python
#
# [452] Minimum Number of Arrows to Burst Balloons
#
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
#
# algorithms
# Medium (47.06%)
# Likes:    558
# Dislikes: 26
# Total Accepted:    43.5K
# Total Submissions: 92.2K
# Testcase Example:  '[[10,16],[2,8],[1,6],[7,12]]'
#
# There are a number of spherical balloons spread in two-dimensional space. For
# each balloon, provided input is the start and end coordinates of the
# horizontal diameter. Since it's horizontal, y-coordinates don't matter and
# hence the x-coordinates of start and end of the diameter suffice. Start is
# always smaller than end. There will be at most 10^4 balloons.
# 
# An arrow can be shot up exactly vertically from different points along the
# x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart
# ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An
# arrow once shot keeps travelling up infinitely. The problem is to find the
# minimum number of arrows that must be shot to burst all balloons.
# 
# Example:
# 
# 
# Input:
# [[10,16], [2,8], [1,6], [7,12]]
# 
# Output:
# 2
# 
# Explanation:
# One way is to shoot one arrow for example at x = 6 (bursting the balloons
# [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two
# balloons).
# 
# 
# 
# 
#


class Solution(object):
    def _findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # 类似于寻找最多上课时间段
        # 先排序，再寻找
        if len(points) < 2:
            return len(points)
        points.sort(key=lambda x:x[0])
        count = 0
        last = points[0]
        for point in points[1:]:
            if point[0] > last[1]:
                count += 1
                last = point
            else:
                last = [point[0], min(point[1], last[1])]
        return count + 1

    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # 所以可以根据段尾排序
        if len(points) < 2:
            return len(points)
        points.sort(key=lambda x:x[1])
        last = points[0][1]
        count = 1
        for point in points:
            if point[0] > last:
                count += 1
                last = point[1]
        return count


# if __name__ == '__main__':
#     s = Solution()
#     print s.findMinArrowShots([[1,5], [2,4], [5,6]])
#     print s.findMinArrowShots([[1,3], [2,6]])
#     print s.findMinArrowShots([[10,16], [2,8], [1,6], [7,12]])
