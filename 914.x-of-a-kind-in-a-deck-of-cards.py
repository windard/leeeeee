# coding=utf-8
#
# @lc app=leetcode id=914 lang=python
#
# [914] X of a Kind in a Deck of Cards
#
# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/description/
#
# algorithms
# Easy (33.91%)
# Likes:    256
# Dislikes: 64
# Total Accepted:    21.8K
# Total Submissions: 64.4K
# Testcase Example:  '[1,2,3,4,4,3,2,1]'
#
# In a deck of cards, each card has an integer written on it.
# 
# Return true if and only if you can choose X >= 2 such that it is possible to
# split the entire deck into 1 or more groups of cards, where:
# 
# 
# Each group has exactly X cards.
# All the cards in each group have the same integer.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,1,1,2,2,2,3,3]
# Output: false
# Explanation: No possible partition.
# 
# 
# 
# Example 3:
# 
# 
# Input: [1]
# Output: false
# Explanation: No possible partition.
# 
# 
# 
# Example 4:
# 
# 
# Input: [1,1]
# Output: true
# Explanation: Possible partition [1,1]
# 
# 
# 
# Example 5:
# 
# 
# Input: [1,1,2,2,2,2]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[2,2]
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= deck.length <= 10000
# 0 <= deck[i] < 10000
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#


class Solution(object):
    def _hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        # Wrong Answer
        # [1,1,2,2,2,2]
        # 可以是最小因子的倍数
        data = {}
        for d in deck:
            data[d] = data.get(d, 0) + 1
        return len(set(data.values())) == 1 and data.values()[0] > 1

    def __hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        # Still Wrong
        # [1,1,1,1,2,2,2,2,2,2]
        # 可以有最小公因数
        # too complex
        data = {}
        for d in deck:
            data[d] = data.get(d, 0) + 1

        min_factor = None
        values = data.values()
        if not values:
            return False
        if values:
            if min(values) < 2:
                return False
        for i in range(len(values)-1):
            factor = self.gcd(values[i], values[i+1])
            if factor < 2:
                return False
            if not min_factor:
                min_factor = factor
            else:
                if min_factor < factor:
                    if factor % min_factor:
                        return False
                elif min_factor > factor:
                    if min_factor % factor:
                        return False
                    else:
                        min_factor = factor

        return True

    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        data = {}
        for d in deck:
            data[d] = data.get(d, 0) + 1

        min_value = min(data.values())
        for value in data.values():
            if self.gcd(value, min_value) < 2:
                return False
        return True

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a


# if __name__ == '__main__':
#     s = Solution()
#     print s.hasGroupsSizeX([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,7,7,7,8,8,8,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,13,13,13,13,13,13,13,13,14,14,14,14,14,14,14,14,15,15,15,15,15,15,15,15,15,15,15,15,16,16,16,16,17,17,17,17,18,18,18,18,19,19,19,19])
    # print s.hasGroupsSizeX([1,2,3,4,4,3,2,1])
    # print s.hasGroupsSizeX([1,1,2,2,2,2])
    # print s.hasGroupsSizeX([2,2])
    # print s.hasGroupsSizeX([1])
    # print s.hasGroupsSizeX([1,1,1,1,2,2,2,2,2,2])
    # print s.gcd(1, 3)
    # print s.gcd(2, 3)
    # print s.gcd(3, 6)
    # print s.gcd(6, 8)
    # print s.gcd(6, 6)
