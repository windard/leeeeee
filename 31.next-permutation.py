# coding=utf-8
#
# @lc app=leetcode id=31 lang=python
#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (30.05%)
# Likes:    1818
# Dislikes: 574
# Total Accepted:    243.1K
# Total Submissions: 794.9K
# Testcase Example:  '[1,2,3]'
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
# 
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
# 
# The replacement must be in-place and use only constant extra memory.
# 
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
# 
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#


class Solution(object):
    def _nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if i and nums[i-1] < nums[i]:
                break
        else:
            # 最大值
            for i in range(len(nums)/2):
                nums[i], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i]
            return

        for i in range(len(nums)-2, -1, -1):
            for j in range(i, len(nums)):
                if j < len(nums)-1 and nums[j] < nums[j+1]:
                    # 1,3,2,4
                    # 1,2,4,3
                    # 1,3,4,2
                    # 1,4,5,3,2
                    # 1,3,5,4,2
                    # 1,5,4,3,2
                    nj = min(filter(lambda x: x > nums[j], nums[j:]))
                    ni = nums[j:]
                    ni.remove(nj)
                    lj = sorted(ni)
                    nums[j] = nj
                    o = 0
                    for i in range(j+1, len(nums)):
                        nums[i] = lj[o]
                        o += 1
                    return

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Double Point
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        first = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                first = i
                break

        if first < 0:
            return reverse(0, len(nums)-1)

        second = first
        for i in range(len(nums)-1, first, -1):
            if nums[i] > nums[first]:
                second = i
                break

        nums[first], nums[second] = nums[second], nums[first]
        return reverse(first+1, len(nums)-1)


# if __name__ == '__main__':
#     s = Solution()
#     a = [3,2,1]
#     # a = [5,5,1,1]
#     # a = [1,2,3]
#     # a = [1,1,5]
#     print s.nextPermutation(a)
#     print a
