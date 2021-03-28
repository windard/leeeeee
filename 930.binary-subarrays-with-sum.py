# coding=utf-8
#
# @lc app=leetcode id=930 lang=python
#
# [930] Binary Subarrays With Sum
#
# https://leetcode.com/problems/binary-subarrays-with-sum/description/
#
# algorithms
# Medium (40.34%)
# Total Accepted:    30K
# Total Submissions: 67.2K
# Testcase Example:  '[1,0,1,0,1]\n2'
#
# In an array A of 0s and 1s, how many non-empty subarrays have sum S?
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [1,0,1,0,1], S = 2
# Output: 4
# Explanation: 
# The 4 subarrays are bolded below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# 
# 
# 
# 
# Note:
# 
# 
# A.length <= 30000
# 0 <= S <= A.length
# A[i] is either 0 or 1.
# 
#

from functools import reduce


class Solution(object):
    def numSubarraysWithSum2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # OOM
        # 真的伤心，效率差太多了，Golang 这样写就没问题
        # TwoSum 或者 滑动窗口，应该都可以，O(n)
        count_nums = reduce(lambda x, y: x + [x[-1] + y], nums, [0])
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if count_nums[j] - count_nums[i] == k:
                    count += 1
                elif count_nums[j] - count_nums[i] > k:
                    break
        return count

    def numSubarraysWithSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # TwoSum Again
        pre_sum = {0: 1}
        count = 0
        total = 0
        for num in nums:
            total += num
            if total - k in pre_sum:
                count += pre_sum[total - k]

            pre_sum[total] = pre_sum.get(total, 0) + 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.numSubarraysWithSum([1, 0, 1, 0, 1], 2))
