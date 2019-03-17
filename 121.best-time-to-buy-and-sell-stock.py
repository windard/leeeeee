#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (46.25%)
# Total Accepted:    449.2K
# Total Submissions: 967.6K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
# 
# If you were only permitted to complete at most one transaction (i.e., buy one
# and sell one share of the stock), design an algorithm to find the maximum
# profit.
# 
# Note that you cannot sell a stock before you buy one.
# 
# Example 1:
# 
# 
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.
# 
# 
# Example 2:
# 
# 
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
# 
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0
        res = 0
        min_price = prices[0]
        for i in prices:
            if i < min_price:
                min_price = i
            else:
                res = max(res, i - min_price)

        return res

    def _maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 当断不断
        # 必受其乱 
        # [2,1,2,0,1] 有问题
        if not prices:
            return 0
        before = 0
        after = len(prices) - 1
        min_price = prices[0]
        max_price = prices[-1]
        while before <= after:
            if prices[before] < min_price:
                min_price = prices[before]
                before += 1
            elif before == 0 or prices[before] < max_price:
                before += 1
            if prices[after] > max_price:
                max_price = prices[after]
                after -= 1
            elif after == len(prices) - 1 or prices[after] > min_price:
                after -= 1
        return max_price - min_price if max_price - min_price >= 0 else 0

# if __name__ == "__main__":
#     s = Solution()
#     print s.maxProfit([1,4,2])
#     print s.maxProfit([2,1,2,0,1])
#     print s.maxProfit([7,6,4,3,1])
#     print s.maxProfit([7,1,5,3,6,4])