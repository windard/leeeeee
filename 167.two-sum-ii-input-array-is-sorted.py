#
# @lc app=leetcode id=167 lang=python
#
# [167] Two Sum II - Input array is sorted
#
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
#
# algorithms
# Easy (49.36%)
# Likes:    887
# Dislikes: 375
# Total Accepted:    248.1K
# Total Submissions: 492.1K
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers that is already sorted in ascending order, find
# two numbers such that they add up to a specific target number.
# 
# The function twoSum should return indices of the two numbers such that they
# add up to the target, where index1 must be less than index2.
# 
# Note:
# 
# 
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may
# not use the same element twice.
# 
# 
# Example:
# 
# 
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
# 
#
class Solution(object):
    def _twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time Limit
        length = len(numbers)
        i = j = 0
        while i < length:
            if (target > 0 and numbers[i] >= target):
                break
            j = i + 1
            while j < length:
                if target > 0 and (numbers[i] + numbers[j]) > target:
                    break
                elif (numbers[i] + numbers[j]) == target:
                    return i+1, j+1
                j += 1
            i += 1

    def __twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return i+1, j+1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
    
    def ___twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Still Time Limit
        data = {}
        for key, value in enumerate(numbers):
            if key in data:
                continue
            left = target - value
            for k, v in enumerate(numbers[key+1:]):
                if v == left:
                    return key+1, k+key+2
            data[key] = 1

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Great Thought
        data = {}
        for key, value in enumerate(numbers):
            left = target - value
            if left in data:
                return data[left]+1, key+1

            data[value] = key

# if __name__ == "__main__":
#     s = Solution()
#     print s.twoSum([2, 3, 4], 6)
#     print s.twoSum([-1, 0], -1)
#     print s.twoSum([0, 0, 3 , 4], 0)
