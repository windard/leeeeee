# coding=utf-8
#
# @lc app=leetcode id=84 lang=python
#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (31.91%)
# Likes:    2208
# Dislikes: 59
# Total Accepted:    191.2K
# Total Submissions: 596.7K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
# 
# 
# 
# 
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].
# 
# 
# 
# 
# The largest rectangle is shown in the shaded area, which has area = 10
# unit.
# 
# 
# 
# Example:
# 
# 
# Input: [2,1,5,6,2,3]
# Output: 10
# 
# 
#


class Solution(object):
    def _largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Brute Force
        # Time Limit
        # O(n^3)
        max_count = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)+1):
                area = min(heights[i:j]) * (j-i)
                max_count = max(area, max_count)
        return max_count

    def _____largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Another Brute Force
        # Time Limit
        # O(n^2)
        # Still Time Limit
        max_count = 0
        for i, v in enumerate(heights):
            length = 1
            for j in range(i-1, -1, -1):
                if heights[j] >= v:
                    length += 1
                else:
                    break
            for j in range(i+1, len(heights)):
                if heights[j] >= v:
                    length += 1
                else:
                    break
            max_count = max(v * length, max_count)
        return max_count

    def __largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 分治递归
        # Memory Error
        if not heights:
            return 0
        length = min(heights)
        count = len(heights) * length
        index = heights.index(length)
        return max(count,
                   self.largestRectangleArea(heights[:index]),
                   self.largestRectangleArea(heights[index+1:]))

    def ___largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 单调栈
        # 单调递增的时候入栈，单调递减的时候出栈，出一次栈，加一个深度
        # Wrong Answer
        # [2,1,2]
        stack = []
        max_count = 0
        heights.append(0)

        for height in heights:
            if not stack or stack[-1] <= height:
                stack.append(height)
            else:
                length = 0
                while stack and stack[-1] > height:
                    length += 1
                    h = stack.pop()
                    max_count = max(h*length, max_count)
                stack.append(height)
        return max_count

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 单调栈
        # 还是用单调递增的栈
        # 当递减的时候，将栈顶元素出栈，记为顶点
        # 计算 顶点与现在栈顶的距离，求出面积
        # 为了解决开头和结尾的特殊情况，可以在栈顶和栈尾各加上一个0，不影响计算
        # 将索引下标入栈，而非将值入栈

        heights = [0] + heights + [0]
        stack = []
        max_count = 0

        for i in range(len(heights)):
            if not stack:
                stack.append(i)
                continue

            while stack and heights[i] <= heights[stack[-1]]:
                top = stack.pop()
                length = 0
                if stack:
                    length = i - stack[-1] - 1
                max_count = max(heights[top] * length, max_count)
            stack.append(i)

        return max_count


# if __name__ == '__main__':
#     s = Solution()
#     print s.largestRectangleArea([2,1,5,6,2,3])
#     print s.largestRectangleArea([2,0,2])
#     print s.largestRectangleArea([2,1,1])
