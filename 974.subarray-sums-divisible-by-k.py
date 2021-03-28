# coding=utf-8
#
# @lc app=leetcode id=974 lang=python
#
# [974] Subarray Sums Divisible by K
#
# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
#
# algorithms
# Medium (47.31%)
# Total Accepted:    56.2K
# Total Submissions: 110.2K
# Testcase Example:  '[4,5,0,-2,-3,1]\n5'
#
# Given an array A of integers, return the number of (contiguous, non-empty)
# subarrays that have a sum divisible by K.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [4,5,0,-2,-3,1], K = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by K = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2,
# -3]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 30000
# -10000 <= A[i] <= 10000
# 2 <= K <= 10000
# 
# 
#
from functools import reduce


class Solution(object):
    def subarraysDivByK2(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # 和 523 比较类似，<del>不过那道题是 K 为因子，这道题是 K 为除数<del>
        # 和 523 一模一样，但是 OOM 了，😂
        pre_sum = reduce(lambda x, y: x + [x[-1] + y], A, [0])

        count = 0
        for i in range(len(pre_sum)):
            for j in range(i + 1, len(pre_sum)):
                div = pre_sum[j] - pre_sum[i]
                # if div in (0, 1):
                #     count += 1
                #     continue
                # if K % div == 0:
                #     count += 1
                if div % K == 0:
                    count += 1
        return count

    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # 那就用和 523 一样的办法来做
        # 使用 dict 保存取余的结果对应的数量
        # 在累加的时候，可以只加余数，来防止整数溢出
        pre_sum_div = {0: 1}
        total = count = 0
        for num in A:
            total += num
            div = total % K
            if div in pre_sum_div:
                count += pre_sum_div[div]
            pre_sum_div[div] = pre_sum_div.get(div, 0) + 1
        return count


if __name__ == '__main__':
    s = Solution()
    # print(s.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))
    print(s.subarraysDivByK([-1, 2, 9], 2))
