# coding=utf-8
#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (44.17%)
# Likes:    4141
# Dislikes: 76
# Total Accepted:    328.6K
# Total Submissions: 742.3K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
# 
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
# 
# Example:
# 
# 
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# 
#


class Solution(object):
    def _trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 暴力，按层来做
        # Time Limit
        # O(n*m)
        if not height:
            return 0
        count = 0
        for i in range(max(height)):
            start = False
            tmp = 0
            for h in height:
                if h > i:
                    if tmp:
                        count += tmp
                        tmp = 0
                    start = True
                else:
                    if start:
                        tmp += 1
        return count

    def __trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 暴力，按列来做
        # O(n*n)
        # Time Limit Again
        count = 0
        for i, v in enumerate(height):
            left = right = 0
            for h in height[:i]:
                left = max(left, h)
            for h in height[i+1:]:
                right = max(right, h)

            count += max(0, min(left, right) - v)
        return count

    def ___trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # dynamic programming
        # 动态存下 左边最高的栏 和 右边最高的栏
        # lefts[i] 存的是第 i+1 个位置，左边的最高栏数
        # right[i] 存的是第 i-1 个位置，右边的最高栏数
        lefts = [0] * len(height)
        rights = [0] * len(height)

        for i, v in enumerate(height):
            lefts[i] = max(lefts[i-1], v)

        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                rights[i] = height[i]
            else:
                rights[i] = max(rights[i+1], height[i])

        count = 0
        for i in range(1, len(height)-1):
            count += max(0, min(lefts[i-1], rights[i+1]) - height[i])

        return count

    def ____trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Double Point
        # 按列求，从两边往中间
        # 先设最大值为左右第一位
        # 从第二位开始，找到左右最大值相对较小的一方
        # 如果 目标位置 小于左右较小的一方，则可以填满水，计算差值
        # 如果 目标位置 大于左右较小的一方，则更新最值

        if not height:
            return 0
        left = 1
        right = len(height) - 2
        max_left = height[0]
        max_right = height[len(height)-1]
        count = 0

        for _ in range(1, len(height)-1):
            if max_left < max_right:
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    count += max_left - height[left]
                left += 1
            else:
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    count += max_right - height[right]
                right -= 1

        return count

    def _____trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 单调栈
        # 重点，难点
        # 从大到小，递减入栈，将栏数进栈
        # 如果 目标位置 大于栈顶，将栈顶出栈，设为 最低点
        # Wrong Answer
        # 会有遗漏
        stack = []
        count = 0

        for h in height:
            if not h:
                stack.append(h)
                continue

            while stack and h > stack[-1]:
                top = stack.pop()
                if not stack:
                    break
                else:
                    length = min(stack[-1], h)
                    count += length - top
            stack.append(h)

        return count

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 继续单调栈
        # 将 索引下标入栈
        # 单调栈，计算两堵墙之间的空隙
        # 先递减，在找墙
        stack = []
        count = 0

        for i in range(len(height)):
            if not i:
                stack.append(i)
                continue

            while height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                length = min(height[i], height[stack[-1]])
                count += (i - stack[-1] - 1) * (length - height[top])
            stack.append(i)

        return count


# if __name__ == '__main__':
#     s = Solution()
#     print s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
#     print s.trap([4,2,0,3,2,5])
