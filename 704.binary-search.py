#
# @lc app=leetcode id=704 lang=python
#
# [704] Binary Search
#
# https://leetcode.com/problems/binary-search/description/
#
# algorithms
# Easy (45.32%)
# Likes:    290
# Dislikes: 32
# Total Accepted:    62.1K
# Total Submissions: 127.6K
# Testcase Example:  '[-1,0,3,5,9,12]\n9'
#
# Given a sorted (in ascending order) integer array nums of n elements and a
# target value, write a function to search target in nums. If target exists,
# then return its index, otherwise return -1.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
# 
# 
# 
# 
# Note:
# 
# 
# You may assume that all elements in nums are unique.
# n will be in the range [1, 10000].
# The value of each element in nums will be in the range [-9999, 9999].
# 
# 
#
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            middle = (start + end) / 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                end = middle - 1
            else:
                start = middle + 1

        return -1

# if __name__ == "__main__":
#     s = Solution()
#     print s.search([-1,0,3,5,9,12], 9)
#     print s.search([-1,0,3,5,9,12], 2)
#     print s.search([-1,0,3,5,9,12], 13)
