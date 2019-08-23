# coding=utf-8
#
# @lc app=leetcode id=836 lang=python
#
# [836] Rectangle Overlap
#
# https://leetcode.com/problems/rectangle-overlap/description/
#
# algorithms
# Easy (47.01%)
# Likes:    382
# Dislikes: 77
# Total Accepted:    28.8K
# Total Submissions: 61.3K
# Testcase Example:  '[0,0,2,2]\n[1,1,3,3]'
#
# A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the
# coordinates of its bottom-left corner, and (x2, y2) are the coordinates of
# its top-right corner.
# 
# Two rectangles overlap if the area of their intersection is positive.  To be
# clear, two rectangles that only touch at the corner or edges do not overlap.
# 
# Given two (axis-aligned) rectangles, return whether they overlap.
# 
# Example 1:
# 
# 
# Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# Output: false
# 
# 
# Notes:
# 
# 
# Both rectangles rec1 and rec2 are lists of 4 integers.
# All coordinates in rectangles will be between -10^9 and 10^9.
# 
# 
#


class Solution(object):
    def _isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        # 四种情况
        # 画一画就知道了
        # 还有两种全包围的情况
        # 还有四种半包围的情况
        # too complex and wrong answer

        if (rec1[0] <= rec2[0] < rec2[2] <= rec1[2] and rec1[1] <= rec2[1] < rec2[3] <= rec1[3]) or \
                (rec2[0] <= rec1[0] < rec1[2] <= rec2[2] and rec2[1] <= rec1[1] < rec1[3] <= rec2[3]) or \
                (rec2[0] <= rec1[0] <= rec2[2] and rec2[1] <= rec1[3] <= rec2[3]) or \
                (rec1[0] <= rec2[0] <= rec1[2] and rec1[1] <= rec2[3] <= rec1[3]) or \
                (rec1[0] <= rec2[0] <= rec1[2] and rec1[1] <= rec2[1] <= rec1[3]) or \
                (rec2[0] <= rec1[0] <= rec2[2] and rec2[1] <= rec1[1] <= rec2[3]) or \
                (rec1[0] <= rec2[0] < rec2[2] <= rec1[2] and rec1[1] < rec2[1] < rec1[3]) or \
                (rec2[0] <= rec1[0] < rec1[2] <= rec2[2] and rec2[1] < rec1[1] < rec2[3]) or \
                (rec1[1] <= rec2[1] < rec2[3] <= rec1[3] and rec2[0] < rec1[0] < rec2[2]) or \
                (rec2[1] <= rec1[1] < rec1[3] <= rec2[3] and rec1[0] < rec2[0] < rec1[2]):
            return True
        return False

    def __isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        hor = min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])
        ver = min(rec1[3], rec2[3]) - max(rec1[1], rec2[1])
        return hor > 0 and ver > 0

    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        # 或者求不相交的
        if rec1[0] >= rec2[2] or rec1[2] <= rec2[0] or rec1[1] >= rec2[3] or rec1[3] <= rec2[1]:
            return False
        return True


# if __name__ == '__main__':
#     s = Solution()
#     print s.isRectangleOverlap([0,0,2,2], [1,1,3,3])
#     print s.isRectangleOverlap([0,0,1,1], [1,0,2,1])
