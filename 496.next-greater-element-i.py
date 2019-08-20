# coding=utf-8
#
# @lc app=leetcode id=496 lang=python
#
# [496] Next Greater Element I
#
# https://leetcode.com/problems/next-greater-element-i/description/
#
# algorithms
# Easy (58.75%)
# Likes:    794
# Dislikes: 1301
# Total Accepted:    97.2K
# Total Submissions: 163.1K
# Testcase Example:  '[4,1,2]\n[1,3,4,2]'
#
# 
# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s
# elements are subset of nums2. Find all the next greater numbers for nums1's
# elements in the corresponding places of nums2. 
# 
# 
# 
# The Next Greater Number of a number x in nums1 is the first greater number to
# its right in nums2. If it does not exist, output -1 for this number.
# 
# 
# Example 1:
# 
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
# Output: [-1,3,-1]
# Explanation:
# ⁠   For number 4 in the first array, you cannot find the next greater number
# for it in the second array, so output -1.
# ⁠   For number 1 in the first array, the next greater number for it in the
# second array is 3.
# ⁠   For number 2 in the first array, there is no next greater number for it
# in the second array, so output -1.
# 
# 
# 
# Example 2:
# 
# Input: nums1 = [2,4], nums2 = [1,2,3,4].
# Output: [3,-1]
# Explanation:
# ⁠   For number 2 in the first array, the next greater number for it in the
# second array is 3.
# ⁠   For number 4 in the first array, there is no next greater number for it
# in the second array, so output -1.
# 
# 
# 
# 
# Note:
# 
# All elements in nums1 and nums2 are unique.
# The length of both nums1 and nums2 would not exceed 1000.
# 
# 
#


class Solution(object):
    def _nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for n in nums1:
            start = nums2.index(n)
            for i in range(start+1, len(nums2)):
                if nums2[i] > n:
                    result.append(nums2[i])
                    break
            else:
                result.append(-1)
        return result

    def __nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 明白了，一个栈
        # O(m+n)
        stack = []
        data = {}
        for nums in nums2[::-1]:
            while stack:
                value = stack.pop()
                if value > nums:
                    data[nums] = value
                    stack.append(value)
                    break
            else:
                data[nums] = -1
            stack.append(nums)

        return [data[n] for n in nums1]

    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 还能更巧妙
        # 不过不是这道题的
        # result = [-1] * len(nums2)
        # stack = []
        # for i in range(len(nums2)-1, -1, -1):
        #     while stack:
        #         if stack[-1] < nums2[i]:
        #             stack.pop()
        #         else:
        #             result[i] = stack[-1]
        #             break
        #     stack.append(nums2[i])
        #
        # return result


# if __name__ == '__main__':
#     s = Solution()
#     print s.nextGreaterElement([4,1,2], [1,3,4,2])
#     print s.nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7])
