# coding=utf-8
#
# @lc app=leetcode id=1089 lang=python
#
# [1089] Duplicate Zeros
#
# https://leetcode.com/problems/duplicate-zeros/description/
#
# algorithms
# Easy (58.99%)
# Likes:    118
# Dislikes: 94
# Total Accepted:    15.1K
# Total Submissions: 25.6K
# Testcase Example:  '[1,0,2,3,0,4,5,0]'
#
# Given a fixed length array arr of integers, duplicate each occurrence of
# zero, shifting the remaining elements to the right.
# 
# Note that elements beyond the length of the original array are not written.
# 
# Do the above modifications to the input array in place, do not return
# anything from your function.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to:
# [1,0,0,2,3,0,0,4]
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3]
# Output: null
# Explanation: After calling your function, the input array is modified to:
# [1,2,3]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= arr.length <= 10000
# 0 <= arr[i] <= 9
# 
#


class Solution(object):
    def _duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        # Don't Growth More Length
        index = 0
        actual = 0
        length = len(arr)
        while index < length:
            if arr[actual] == 0:
                arr.insert(actual+1, 0)
                index += 1
                actual += 2
            else:
                index += 1
                actual += 1

    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        # Don't Growth More Length
        actual = 0
        length = len(arr)
        while actual < length:
            if arr[actual] == 0:
                arr.insert(actual+1, 0)
                actual += 2
                arr.pop()
            else:
                actual += 1


# if __name__ == "__main__":
#     s = Solution()
#     a = [1,0,2,3,0,4,5,0]
#     s.duplicateZeros(a)
#     print a
