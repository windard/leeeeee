# coding=utf-8
#
# @lc app=leetcode id=846 lang=python
#
# [846] Hand of Straights
#
# https://leetcode.com/problems/hand-of-straights/description/
#
# algorithms
# Medium (48.44%)
# Total Accepted:    16.6K
# Total Submissions: 34.4K
# Testcase Example:  '[1,2,3,6,2,3,4,7,8]\n3'
#
# Alice has a hand of cards, given as an array of integers.
# 
# Now she wants to rearrange the cards into groups so that each group is size
# W, and consists of W consecutive cards.
# 
# Return true if and only if she can.
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
# 
# Example 2:
# 
# 
# Input: hand = [1,2,3,4,5], W = 4
# Output: false
# Explanation: Alice's hand can't be rearranged into groups of 4.
# 
# 
# 
# Note:
# 
# 
# 1 <= hand.length <= 10000
# 0 <= hand[i] <= 10^9
# 1 <= W <= hand.length
# 
# 
#


class Solution(object):
    def _isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        # Wrong Answer
        # 每组为W张连续牌组成，牌数不限
        i = 0
        count = 0
        while i < len(hand):
            j = i
            length = 0
            value = hand[i]
            gap = None
            while j < len(hand):
                if hand[j] == value and gap == None:
                    length = 1
                if hand[j] == value + 1:
                    if gap == None:
                        gap = 1
                        length += 1
                        value += 1
                    elif gap == 1:
                        length += 1
                        value += 1
                elif hand[j] == value - 1:
                    if gap == None:
                        gap = -1
                        length += 1
                        value -= 1
                    elif gap == -1:
                        length += 1
                        value -= 1
                if length >= W:
                    count += 1
                    break
                j += 1
            if count >= W:
                return True
            i += 1
        return False

    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if len(hand) < W:
            return False
        if len(hand) / W != len(hand) / float(W):
            return False
        data = {}
        for h in hand:
            data[h] = data.get(h, 0) + 1
        while data:
            n = min(data.keys())
            # 一次减一张的地方可以优化
            # 一次减去第一张牌的量也可
            for i in range(W):
                if data.get(n+i, 0) > 0:
                    data[n+i] -= 1
                    if data[n+i] == 0:
                        del data[n+i]
                else:
                    return False
        return True


# if __name__ == "__main__":
#     s = Solution()
#     print s.isNStraightHand([1], 1)
#     print s.isNStraightHand([2, 1], 2)
#     print s.isNStraightHand([1,2,3,6,2,3,4,7,8], 3)
#     print s.isNStraightHand([1,2,3,6,2,3,4,7,8], 4)
#     print s.isNStraightHand([1,2,3,4,5], 4)
