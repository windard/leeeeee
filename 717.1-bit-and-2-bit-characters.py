#
# @lc app=leetcode id=717 lang=python
#
# [717] 1-bit and 2-bit Characters
#
# https://leetcode.com/problems/1-bit-and-2-bit-characters/description/
#
# algorithms
# Easy (49.25%)
# Likes:    278
# Dislikes: 705
# Total Accepted:    44.9K
# Total Submissions: 91.1K
# Testcase Example:  '[1,0,0]'
#
# We have two special characters. The first character can be represented by one
# bit 0. The second character can be represented by two bits (10 or 11).  
# 
# Now given a string represented by several bits. Return whether the last
# character must be a one-bit character or not. The given string will always
# end with a zero.
# 
# Example 1:
# 
# Input: 
# bits = [1, 0, 0]
# Output: True
# Explanation: 
# The only way to decode it is two-bit character and one-bit character. So the
# last character is one-bit character.
# 
# 
# 
# Example 2:
# 
# Input: 
# bits = [1, 1, 1, 0]
# Output: False
# Explanation: 
# The only way to decode it is two-bit character and two-bit character. So the
# last character is NOT one-bit character.
# 
# 
# 
# Note:
# 1 .
# bits[i] is always 0 or 1.
# 
#


class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        # hard to understand
        index = 0
        while index < len(bits) - 1:
            if bits[index] == 1:
                index += 2
            else:
                index += 1
        return index == len(bits) - 1
