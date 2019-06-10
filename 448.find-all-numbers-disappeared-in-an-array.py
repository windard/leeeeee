#
# @lc app=leetcode id=448 lang=python
#
# [448] Find All Numbers Disappeared in an Array
#
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
#
# algorithms
# Easy (52.75%)
# Likes:    1641
# Dislikes: 157
# Total Accepted:    154.6K
# Total Submissions: 289.2K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
# elements appear twice and others appear once.
# 
# Find all the elements of [1, n] inclusive that do not appear in this array.
# 
# Could you do it without extra space and in O(n) runtime? You may assume the
# returned list does not count as extra space.
# 
# Example:
# 
# Input:
# [4,3,2,7,8,2,3,1]
# 
# Output:
# [5,6]
# 
# 
#
class Solution(object):
    def _findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        length = len(nums)
        nums = set(nums)
        for num in range(1, length+1):
            if num not in nums:
                res.append(num)
        return res

    def __findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Time Limit
        res = []
        for num in range(1, len(nums)+1):
            if num not in set(nums):
                res.append(num)
        return res

    def ___findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Accept
        return set(nums) ^ set(range(1, len(nums)+1))

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 又难理解又难写
        for num in nums:
            nums[abs(num)-1] = - abs(nums[abs(num)-1])
        return [key+1 for key, num in enumerate(nums) if num > 0]

# if __name__ == "__main__":
#     s = Solution()
#     print s.findDisappearedNumbers([2, 2])
#     print s.findDisappearedNumbers([1,1])
#     print s.findDisappearedNumbers([4,3,2,7,8,2,3,1])
