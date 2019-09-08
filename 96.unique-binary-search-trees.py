# coding=utf-8
#
# @lc app=leetcode id=96 lang=python
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (45.13%)
# Likes:    1713
# Dislikes: 68
# Total Accepted:    201.3K
# Total Submissions: 434.2K
# Testcase Example:  '3'
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1 ... n?
# 
# Example:
# 
# 
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
# 
#


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 卡塔兰数
        # C(0) = 1
        # C(n+1) = 2*(2*n+1)/(n+2)C(n)
        ans = 1
        for i in range(0, n):
            ans = (2.0 * (2*i + 1) / (i+2)) * ans
        return int(ans)


# if __name__ == '__main__':
#     s = Solution()
#     for i in range(10):
#         print i, s.numTrees(i)
