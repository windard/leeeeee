#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (25.31%)
# Total Accepted:    374.1K
# Total Submissions: 1.5M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
# Example 1:
#
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
#
#
# Example 2:
#
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5
#
#
#
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        length = len(nums1) + len(nums2)
        if length == 2:
            return sum(nums1 + nums2) / 2.0
        elif length == 1:
            return (nums1 + nums2)[0]
        elif length == 0:
            return 0

        if length % 2 != 0:
            mid = (length + 1 ) / 2
            flag = False
        else:
            mid = length / 2
            flag = True

        start = 0
        ii = 0
        ji = 0
        now = None

        while 1:

            if start == mid:
                if flag == False:
                    return now
                else:
                    if ii >= len(nums1):
                        next_one = nums2[ji]
                    elif ji >= len(nums2):
                        next_one = nums1[ii]
                    else:
                        if nums1[ii] < nums2[ji]:
                            next_one = nums1[ii]
                        else:
                            next_one = nums2[ji]
                    return (now + next_one) / 2.0
            else:
                if ii >= len(nums1):
                    now = nums2[ji]
                    ji += 1
                    start += 1
                elif ji >= len(nums2):
                    now = nums1[ii]
                    ii += 1
                    start += 1
                else:
                    if nums1[ii] < nums2[ji]:
                        now = nums1[ii]
                        ii += 1
                        start += 1
                    else:
                        now = nums2[ji]
                        ji += 1
                        start += 1

    def _findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        length = len(nums)
        if length % 2 == 1:
            return nums[length / 2]
        else:
            return (nums[length / 2] + nums[length / 2 - 1]) / 2.0


