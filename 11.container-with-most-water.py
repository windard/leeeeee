#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (42.07%)
# Total Accepted:    310.8K
# Total Submissions: 737K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container and n is at least 2.
# 
# 
# 
# 
# 
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In
# this case, the max area of water (blue section) the container can contain is
# 49. 
# 
# 
# 
# Example:
# 
# 
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
# 
#

import itertools

class Solution(object):
    def _maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Time Limit
        point_map = zip(range(len(height)), height)
        max_area = 0
        for a,b in itertools.combinations(point_map, 2):
            area = abs(a[0]-b[0]) * min(a[1], b[1])
            max_area = area if area > max_area else max_area
        return max_area

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = ans = 0
        right = len(height) - 1
        while left < right:
            ans = max(ans, (right - left) * min(height[left], height[right]))

            if (height[left] < height[right]):
                left += 1
            else:
                right -= 1
        return ans
