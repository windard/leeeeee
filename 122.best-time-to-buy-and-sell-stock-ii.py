#
# @lc app=leetcode id=122 lang=python
#
# [122] Best Time to Buy and Sell Stock II
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
#
# algorithms
# Easy (50.92%)
# Total Accepted:    298.3K
# Total Submissions: 584K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (i.e., buy one and sell one share of the stock
# multiple times).
# 
# Note: You may not engage in multiple transactions at the same time (i.e., you
# must sell the stock before you buy again).
# 
# Example 1:
# 
# 
# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit =
# 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 =
# 3.
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you
# are
# engaging multiple transactions at the same time. You must sell before buying
# again.
# 
# 
# Example 3:
# 
# 
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 在价格跌之前卖
        # 在价格涨之前买
        # 人生如果能先知先觉就好了
        # 贪婪比动态规划好
        # 贪婪能取得所有的获利
        # 动态规划能取得最大的获利
        flag = 0
        last = None
        goal = None
        res = 0
        for value in prices:
            if last != None:
                if value < last:
                    if flag > 0 and goal != None:
                        res += last - goal
                        flag = -1
                else:
                    if flag <= 0:
                        goal = last
                        flag = 1
            last = value
        if flag > 0 and goal != None:
            res += last - goal
            flag = -1
        return res

# if __name__ == "__main__":
#     s = Solution()
#     print s.maxProfit([3,3,5,0,0,3,1,4])

