#
# @lc app=leetcode id=88 lang=python
#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (34.87%)
# Total Accepted:    337K
# Total Submissions: 962.2K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
# 
# Note:
# 
# 
# The number of elements initialized in nums1 and nums2 are m and n
# respectively.
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
# 
# 
# Example:
# 
# 
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# Output: [1,2,2,3,5,6]
# 
# 
#
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while j < n:
            if i >= m:
                self.insertAndBack(nums1, i, nums2[j])
                m += 1
                i += 1
                j += 1
                continue
            if nums1[i] < nums2[j]:
                i += 1
            else:
                self.insertAndBack(nums1, i, nums2[j])
                m += 1
                i += 1
                j += 1

    def insertAndBack(self, nums, index, num):
        for i in range(len(nums)-1, index, -1):
            nums[i] = nums[i-1]
        nums[index] = num

# if __name__ == "__main__":
#     s = Solution()
#     a = [1,2,3,0,0,0]
#     b = [2,5,6]
#     s.merge(a, 3, b, 3)
#     print a
