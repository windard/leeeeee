# coding=utf-8
#
# @lc app=leetcode id=949 lang=python
#
# [949] Largest Time for Given Digits
#
# https://leetcode.com/problems/largest-time-for-given-digits/description/
#
# algorithms
# Easy (34.40%)
# Likes:    79
# Dislikes: 229
# Total Accepted:    10K
# Total Submissions: 29K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array of 4 digits, return the largest 24 hour time that can be
# made.
# 
# The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from
# 00:00, a time is larger if more time has elapsed since midnight.
# 
# Return the answer as a string of length 5.  If no valid time can be made,
# return an empty string.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3,4]
# Output: "23:41"
# 
# 
# 
# Example 2:
# 
# 
# Input: [5,5,5,5]
# Output: ""
# 
# 
# 
# 
# Note:
# 
# 
# A.length == 4
# 0 <= A[i] <= 9
# 
# 
# 
#


class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        A = map(str, A)
        if '2' in A:
            A.remove('2')
            mh = self.find_in_range(0, 3, A)
            if mh:
                fl = self.find_in_range(0, 5, A)
                if fl:
                    ml = self.find_in_range(0, 9, A)
                    if ml:
                        return '{}{}:{}{}'.format(2, mh, fl, ml)
                    else:
                        pass
                    A.append(fl)
                A.append(mh)
            A.append('2')
        if '1' in A:
            A.remove('1')
            mh = self.find_in_range(0, 9, A)
            if mh:
                fl = self.find_in_range(0, 5, A)
                if fl:
                    ml = self.find_in_range(0, 9, A)
                    if ml:
                        return '{}{}:{}{}'.format(1, mh, fl, ml)
                    else:
                        pass
                    A.append(fl)
                A.append(mh)
            A.append('1')
        if '0' in A:
            A.remove('0')
            mh = self.find_in_range(0, 9, A)
            if mh:
                fl = self.find_in_range(0, 5, A)
                if fl:
                    ml = self.find_in_range(0, 9, A)
                    if ml:
                        return '{}{}:{}{}'.format(0, mh, fl, ml)
                    else:
                        pass
                    A.append(fl)
                A.append(mh)
            A.append('0')
        return ""

    def find_in_range(self, a, b, nums):
        for i in range(b, a-1, -1):
            if str(i) in nums:
                nums.remove(str(i))
                return str(i)


# if __name__ == '__main__':
#     s = Solution()
#     print s.largestTimeFromDigits([0,0,0,0])
#     print s.largestTimeFromDigits([1,2,3,4])
