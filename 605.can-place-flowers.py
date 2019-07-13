#
# @lc app=leetcode id=605 lang=python
#
# [605] Can Place Flowers
#
# https://leetcode.com/problems/can-place-flowers/description/
#
# algorithms
# Easy (30.67%)
# Likes:    478
# Dislikes: 269
# Total Accepted:    63.5K
# Total Submissions: 204.8K
# Testcase Example:  '[1,0,0,0,1]\n1'
#
# Suppose you have a long flowerbed in which some of the plots are planted and
# some are not. However, flowers cannot be planted in adjacent plots - they
# would compete for water and both would die.
# 
# Given a flowerbed (represented as an array containing 0 and 1, where 0 means
# empty and 1 means not empty), and a number n, return if n new flowers can be
# planted in it without violating the no-adjacent-flowers rule.
# 
# Example 1:
# 
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False
# 
# 
# 
# Note:
# 
# The input array won't violate no-adjacent-flowers rule.
# The input array size is in the range of [1, 20000].
# n is a non-negative integer which won't exceed the input array size.
# 
# 
#

# [1, 0, 0, 1, 0]
# [0, 1, 0, 0, 1]
# [0, 0, 0, 0, 1]
# [1, 0, 1, 0, 0]

class Solution(object):
    def _canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        index = 0
        f = 0
        if f >= n:
            return True
        if sum(flowerbed[:2]) == 0:
            f += 1
            flowerbed[0] = 1
            if f >= n:
                return True
        index += 1
        while index < len(flowerbed) -2:
            if sum(flowerbed[index:index+3]) == 0:
                flowerbed[index+1] = 1
                f += 1
                if f >= n:
                    return True
                index += 2
            else:
                index += 1
        if sum(flowerbed[-2:]) == 0:
            f += 1
            flowerbed[-1] = 1
            if f >= n:
                return True
        return False

    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # fill up with 0
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        index = 0
        f = 0
        if f >= n:
            return True
        while index < len(flowerbed) -2:
            if sum(flowerbed[index:index+3]) == 0:
                flowerbed[index+1] = 1
                f += 1
                if f >= n:
                    return True
                index += 2
            else:
                index += 1
        return False

# if __name__ == "__main__":
#     s = Solution()
#     print s.canPlaceFlowers([1,0,0,0,0,0,1], 2)
#     print s.canPlaceFlowers([1,0,1,0,1,0,1], 0)
#     print s.canPlaceFlowers([1, 0, 1, 0, 0], 1)

