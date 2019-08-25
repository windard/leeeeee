# coding=utf-8
#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (49.18%)
# Likes:    2294
# Dislikes: 188
# Total Accepted:    418.1K
# Total Submissions: 848.1K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# Example 1:
# 
# 
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# 
# 
# Example 2:
# 
# 
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
#


class Solution(object):
    def _findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # python 排序算法太牛逼
        # AC
        # O(n^n)
        return sorted(nums)[-k]

    def __findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 堆排序
        # O(NlogK)
        from heapq import nlargest
        return nlargest(k, nums)[-1]

    def _findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 标准解法，二分查找
        # maximum recursion 递归次数太多
        # 但是我这是尾递归应该有优化的。
        chose = 0
        left_count = 0
        for index, left in enumerate(nums):
            if left < nums[chose]:
                nums[index], nums[chose] = nums[chose], nums[index]
                chose = index
                left_count += 1

        right = len(nums) - left_count
        # 此时的 num[chose] 是第 right 大数
        if k == right:
            return nums[chose]
        elif k < right:
            return self.findKthLargest(nums[chose+1:], k)
        else:
            return self.findKthLargest(nums[:chose], k-right)

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start = 0
        end = len(nums)
        target = k

        while True:
            chose = start
            left_count = 0
            index = start+1
            count = 1
            last_poi = end - 1
            while count < end - start:
                if nums[index] <= nums[chose]:
                    nums[index], nums[chose] = nums[chose], nums[index]
                    chose = index
                    left_count += 1
                    index += 1
                elif nums[index] > nums[chose]:
                    nums[index], nums[last_poi] = nums[last_poi], nums[index]
                    last_poi -= 1
                count += 1

            right = end - start - left_count
            if right == target:
                return nums[chose]
            elif right > target:
                start = chose+1
            else:
                end = chose
                target = target - right


# if __name__ == '__main__':
#     s = Solution()
#     print s.findKthLargest([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], 20)  # 2
#     print s.findKthLargest([3,2,3,1,2,4,5,5,6], 9)      # 1
#     print s.findKthLargest([5,2,4,1,3,6,0], 4)          # 3
#     print s.findKthLargest([2, 1], 2)                   # 1
#     print s.findKthLargest([3,2,1,5,6,4], 2)            # 5
#     print s.findKthLargest([3,2,3,1,2,4,5,5,6], 4)      # 4
