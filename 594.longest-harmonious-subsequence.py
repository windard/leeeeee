#
# @lc app=leetcode id=594 lang=python
#
# [594] Longest Harmonious Subsequence
#
# https://leetcode.com/problems/longest-harmonious-subsequence/description/
#
# algorithms
# Easy (43.06%)
# Likes:    415
# Dislikes: 56
# Total Accepted:    36.8K
# Total Submissions: 83.9K
# Testcase Example:  '[1,3,2,2,5,2,3,7]'
#
# We define a harmonious array is an array where the difference between its
# maximum value and its minimum value is exactly 1.
# 
# Now, given an integer array, you need to find the length of its longest
# harmonious subsequence among all its possible subsequences.
# 
# Example 1:
# 
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# 
# 
# 
# Note:
# The length of the input array will not exceed 20,000.
# 
# 
# 
#
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        data = {}
        for n in nums:
            data[n] = data.get(n, 0) + 1
        
        max_length = 0
        for key in data:
            max_length = max(max_length, data[key]+data.get(key+1, -float("inf")))
        
        return max_length


# if __name__ == "__main__":
#     s = Solution()
#     print s.findLHS([1,1,1,1])
