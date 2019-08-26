# coding=utf-8
#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (51.03%)
# Likes:    2192
# Dislikes: 54
# Total Accepted:    396.6K
# Total Submissions: 731K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: nums = [1,2,3]
# Output:
# [
# ⁠[3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#


class Solution(object):
    def _subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # DFS
        # 组合
        # 结果正确，顺序不对
        result = temp = [[]]
        last = []
        while temp:
            temp = []
            for num in nums:
                if not last:
                    temp.append(last + [num])
                else:
                    for l in last:
                        if num > max(l):
                            temp.append(l + [num])
            last = temp
            result.extend(last)
        return result

    def __subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        length = len(nums)
        data = {value:2**key for key,value in enumerate(nums)}
        for i in range(2**length):
            temp = []
            for key,value in data.items():
                if value & i != 0:
                    temp.append(key)
            result.append(temp)
        return result

    def ___subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        length = len(nums)
        for i in range(1<<length):
            temp = []
            for key,value in enumerate(nums):
                if 1<<key & i != 0:
                    temp.append(value)
            result.append(temp)
        return result

    def ____subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Best of All
        result = [[]]
        for n in nums:
            current = result[:]
            for t in current:
                result.append(t+[n])
        return result

    def _____subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.helper(nums, 0, [[]])
    
    def helper(self, nums, index, result):
        if index >= len(nums):
            return result
        temp = result[:]
        for t in temp:
            result.append(t+[nums[index]])
        return self.helper(nums, index+1, result)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        start = 0
        e = len(nums)
        result = []

        def backtrack(s, p):
            result.append(p)

            for i in range(s, e):
                backtrack(i+1, p+[nums[i]])

        backtrack(start, [])
        return result


# if __name__ == "__main__":
#     s = Solution()
#     print s.subsets([1,2,3])
