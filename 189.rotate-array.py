#
# @lc app=leetcode id=189 lang=python
#
# [189] Rotate Array
#
# https://leetcode.com/problems/rotate-array/description/
#
# algorithms
# Easy (28.98%)
# Total Accepted:    283.7K
# Total Submissions: 959.3K
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# Given an array, rotate the array to the right by k steps, where k is
# non-negative.
# 
# Example 1:
# 
# 
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# 
# 
# Example 2:
# 
# 
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# 
# 
# Note:
# 
# 
# Try to come up as many solutions as you can, there are at least 3 different
# ways to solve this problem.
# Could you do it in-place with O(1) extra space?
# 
#
class Solution(object):
    def _rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Accept
        k = k % len(nums)
        for _ in range(k):
            nums.insert(0, nums.pop())

    def __rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Time Limit
        k = k % len(nums)
        for _ in range(k):
            l = nums[-1]
            for i in range(len(nums)-1, 0, -1):
                nums[i], nums[i-1] = nums[i-1], nums[i]
            nums[0] = l

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if not k:
            return
        ns = (nums * 2) [len(nums)-k:2*len(nums)-k]
        for i in range(len(nums)):
            nums[i] = ns[i]

# if __name__ == "__main__":
#     s = Solution()
#     s.rotate([1,2,3,4,5,6,7], 3)
