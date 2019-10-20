# coding=utf-8
#
# @lc app=leetcode id=229 lang=python
#
# [229] Majority Element II
#
# https://leetcode.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (32.78%)
# Likes:    1061
# Dislikes: 124
# Total Accepted:    115K
# Total Submissions: 345K
# Testcase Example:  '[3,2,3]'
#
# Given an integer array of size n, find all elements that appear more than ⌊
# n/3 ⌋ times.
# 
# Note: The algorithm should run in linear time and in O(1) space.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: [3]
# 
# Example 2:
# 
# 
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]
# 
#

# @lc code=start


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 继续使用摩尔投票
        ma = mb = 0
        mac = mbc = 0
        for num in nums:
            if mac != 0 and ma == num:
                mac += 1
            elif mbc != 0 and mb == num:
                mbc += 1
            elif mac == 0:
                ma = num
                mac += 1
            elif mbc == 0:
                mb = num
                mbc += 1
            else:
                mac -= 1
                mbc -= 1

        # 此时只能求出来最大的两个数
        # 具体是否大于 n/3 还需要再计算
        ca = cb = 0
        for num in nums:
            if num == ma:
                ca += 1
            elif num == mb:
                cb += 1
        result = []
        if ca > len(nums) / 3:
            result.append(ma)
        if cb > len(nums) / 3:
            result.append(mb)
        return result

# @lc code=end


# if __name__ == '__main__':
#     s = Solution()
#     print s.majorityElement([1,2,2,3,2,1,1,3])
#     print s.majorityElement([1,1,1,3,3,2,2,2])
