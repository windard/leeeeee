# coding=utf-8
#
# @lc app=leetcode id=239 lang=python
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (37.13%)
# Total Accepted:    150.3K
# Total Submissions: 398.4K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# Given an array nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.
# 
# Example:
# 
# 
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7] 
# Explanation: 
# 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty
# array.
# 
# Follow up:
# Could you solve it in linear time?
#


class Solution(object):
    def _maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Accept 
        if not nums:
            return
        ns = nums[:k]        
        res = []
        res.append(max(ns))
        index = k
        while index < len(nums):
            ns.pop(0)
            ns.append(nums[index])
            res.append(max(ns))
            index += 1
        return res

    def __maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Time Limit
        if not nums:
            return
        
        res = []
        min_num = -float("inf")
        for i in range(min(k, len(nums))):
            min_num = max(min_num, nums[i])
        res.append(min_num)

        for i in range(k, len(nums)):
            min_num = -float("inf")
            for j in range(i-k+1, i+1):
                min_num = max(min_num, nums[j])
            res.append(min_num)
        return res

    def ___maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Accept 
        if not nums:
            return
        
        res = []
        dqueue = [x[0] for x in sorted(enumerate(nums[:k]), key=lambda x:x[1])]
        res.append(nums[dqueue[-1]])

        for i in range(k, len(nums)):
            dqueue.remove(i-k)
            for index, j in enumerate(dqueue):
                if nums[i] < nums[j]:
                    dqueue.insert(index, i)
                    break
            else:
                dqueue.append(i)
            res.append(nums[dqueue[-1]])
        return res

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return
        
        res = []
        dqueue = [0]
        for i in range(min(len(nums), k)):
            if nums[i] < nums[dqueue[-1]]:
                dqueue.append(i)
            else:
                while dqueue:
                    if nums[i] >= nums[dqueue[-1]]:
                        dqueue.pop()
                    else:
                        break
                dqueue.append(i)
        res.append(nums[dqueue[0]])

        for i in range(k, len(nums)):
            if nums[i] < nums[dqueue[-1]]:
                dqueue.append(i)
            else:
                while dqueue:
                    if nums[i] >= nums[dqueue[-1]]:
                        dqueue.pop()
                    else:
                        break
                dqueue.append(i)

            while dqueue:
                if dqueue[0] <= i-k:
                    dqueue.pop(0)
                else:
                    break

            res.append(nums[dqueue[0]])

        return res

# if __name__ == "__main__":
#     s = Solution()
#     print s.maxSlidingWindow([7, 2, 4], 2)
#     print s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
