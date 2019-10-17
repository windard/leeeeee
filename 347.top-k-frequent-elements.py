# coding=utf-8
#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (53.49%)
# Likes:    1724
# Dislikes: 110
# Total Accepted:    230.5K
# Total Submissions: 411.1K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given a non-empty array of integers, return the k most frequent elements.
# 
# Example 1:
# 
# 
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Note: 
# 
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is
# the array's size.
# 
# 
#


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or not k:
            return []
        # 只能先假设没有重复频率的数
        from heapq import nlargest
        from collections import defaultdict
        frequency = {}
        data = defaultdict(list)
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        for key, value in frequency.items():
            data[value].append(key)

        result = []
        topn = nlargest(k, frequency.values())
        for i, v in enumerate(topn):
            if i < k - 1 and topn[i] != topn[i+1]:
                result.extend(data[v])
            elif i == k - 1:
                result.extend(data[v])
        return result


# if __name__ == '__main__':
#     s = Solution()
#     print s.topKFrequent([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], 10)
#     print s.topKFrequent([], 0)
#     print s.topKFrequent([1], 1)
#     print s.topKFrequent([1,2], 2)
#     print s.topKFrequent([1,1,1,2,2,3], 2)
