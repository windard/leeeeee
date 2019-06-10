#
# @lc app=leetcode id=485 lang=python
#
# [485] Max Consecutive Ones
#
# https://leetcode.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (54.51%)
# Likes:    364
# Dislikes: 312
# Total Accepted:    138.6K
# Total Submissions: 251.7K
# Testcase Example:  '[1,0,1,1,0,1]'
#
# Given a binary array, find the maximum number of consecutive 1s in this
# array.
# 
# Example 1:
# 
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive
# 1s.
# ⁠   The maximum number of consecutive 1s is 3.
# 
# 
# 
# Note:
# 
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
# 
# 
#
class Solution(object):
    def _findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = longest = 0
        for num in nums:
            if num == 1:
                length += 1
            else:
                longest = longest if longest > length else length
                length = 0
        return longest if longest > length else length

    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = longest = 0
        for num in nums:
            if num == 1:
                length += 1
            else:
                longest = max(longest, length)
                length = 0
        return max(longest, length)

# if __name__ == "__main__":
#     s = Solution()
#     print s.findMaxConsecutiveOnes([1,1,0,1,1,1])
