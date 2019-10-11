# coding=utf-8
#
# @lc app=leetcode id=287 lang=python
#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (50.60%)
# Likes:    2807
# Dislikes: 322
# Total Accepted:    213.6K
# Total Submissions: 420.6K
# Testcase Example:  '[1,3,4,2,2]'
#
# Given an array nums containing n + 1 integers where each integer is between 1
# and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
# 
# Example 1:
# 
# 
# Input: [1,3,4,2,2]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [3,1,3,4,2]
# Output: 3
# 
# Note:
# 
# 
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n^2).
# There is only one duplicate number in the array, but it could be repeated
# more than once.
# 
# 
#


class Solution(object):
    def _findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n+1 个数 包含 1-n
        # 有且仅有一个数重复
        # a = reduce(lambda x,y: x ^ y, [1,2,3,4,4]+range(1, 5))
        # 但他重复可能不止一次
        # a = reduce(lambda x, y: x ^ y, [1,2,3,4,3,3])
        # 不能总想到 什么异或，广阔天地，大有所为
        # 比如哈希表,或者集合
        data = {}
        for num in nums:
            if num in data:
                return num
            data[num] = 1

    def __findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 再比如，先排序
        nums.sort()
        last = 0
        for n in nums:
            if last == n:
                return n
            else:
                last = n

    def ___findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 还比如，抽屉法，或者说，鸽子洞
        boxes = [0] * len(nums)
        for n in nums:
            if boxes[n-1]:
                return n
            else:
                boxes[n-1] = 1

    def ____findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 排序还能这样写
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

    def ______findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 抽屉法还能这么写
        for i in range(len(nums)):
            if nums[abs(nums[i])] < 0:
                return abs(nums[i])
            else:
                nums[abs(nums[i])] = -nums[abs(nums[i])]

    def _____findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 表演开始
        # 二分查找
        # O(nlogn)
        # 其实也不是二分的思路
        # 这是类似快排的思路
        # 但是说起来这个也不对
        # 因为他改了原数组
        if not len(nums) % 2:
            nums.append(len(nums))
        start = 1
        end = len(nums) - 1
        while start < end:
            mid = (start + end) / 2
            lower = upper = 0
            for num in nums:
                if start <= num <= mid:
                    lower += 1
                elif mid < num <= end:
                    upper += 1

            if lower > upper:
                end = mid
            else:
                start = mid + 1
        return start

    def _______findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 1
        end = len(nums) - 1
        while start < end:
            mid = (start + end) / 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1

            if count > mid:
                end = mid
            else:
                start = mid + 1
        return start

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 真正的见证奇迹
        # [1,3,4,2,2]
        # 确实是一个环
        # 虽然有的时候，环的大小为1
        start = end = 0
        while True:
            start = nums[start]
            end = nums[nums[end]]
            if start == end:
                break

        start = 0
        while nums[start] != nums[end]:
            end = nums[end]
            start = nums[start]
        return nums[start]


# if __name__ == '__main__':
#     s = Solution()
#     print s.findDuplicate([1,3,4,2,2])
#     print s.findDuplicate([3,1,3,4,2])
#     print s.findDuplicate([1,3,4,2,2,5,6])
#     print s.findDuplicate([3,1,1,4,2,5,6])
#     print s.findDuplicate([1,3,4,2,5,5,6])
#     print s.findDuplicate([3,1,1,4,2])
#     print s.findDuplicate([1,1,2,3])
#     print s.findDuplicate([1,2,2,3])
#     print s.findDuplicate([1,3,2,3])
#     print s.findDuplicate([1,1,2,3,4])
#     print s.findDuplicate([1,1,2,3,5,6])
#     print s.findDuplicate([1,5,2,3,4,6,6])
