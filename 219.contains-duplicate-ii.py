#
# @lc app=leetcode id=219 lang=python
#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (34.71%)
# Total Accepted:    191.8K
# Total Submissions: 547.1K
# Testcase Example:  '[1,2,3,1]\n3'
#
# Given an array of integers and an integer k, find out whether there are two
# distinct indices i and j in the array such that nums[i] = nums[j] and the
# absolute difference between i and j is at most k.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1], k = 3
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,0,1,1], k = 1
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
# 
# 
# 
# 
# 
#
class Solution(object):
    def _containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Time Limited
        if not nums:
            return False
        if k < 1:
            return False
        max_length = max(len(nums) - k, len(nums))
        for i in range(max_length):
            for j in range(i+1, min(i + k + 1, len(nums))):
                if nums[i] == nums[j]:
                    return True
        return False

    def __containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i in range(0, min(k+1, len(nums))):
            new = d.get(nums[i], 0) + 1
            if new > 1:
                return True
            d[nums[i]] = new
        
        if k + 1 >= len(nums):
            return False

        for i in range(k+1, len(nums)):
            del d[nums[i-k-1]]
            new = d.get(nums[i], 0) + 1
            if new > 1:
                return True
            d[nums[i]] = new
        
        return False

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Time Limit
        d = nums[:k+1]

        if len(set(d)) != len(d):
            return True

        if k + 1 >= len(nums):
            return False
    
        for i in range(k+1, len(nums)):
            d.remove(nums[i-k-1])
            d.append(nums[i])

            if len(set(d)) != len(d):
                return True

        return False

# if __name__ == "__main__":
#     s = Solution()
#     print s.containsNearbyDuplicate([1,2,3,1,2,3], 2)
