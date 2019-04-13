#
# @lc app=leetcode id=405 lang=python
#
# [405] Convert a Number to Hexadecimal
#
# https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/
#
# algorithms
# Easy (41.68%)
# Total Accepted:    45.5K
# Total Submissions: 108.9K
# Testcase Example:  '26'
#
# 
# Given an integer, write an algorithm to convert it to hexadecimal. For
# negative integer, two’s complement method is used.
# 
# 
# Note:
# 
# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number is
# zero, it is represented by a single zero character '0'; otherwise, the first
# character in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed
# integer.
# You must not use any method provided by the library which converts/formats
# the number to hex directly.
# 
# 
# 
# Example 1:
# 
# Input:
# 26
# 
# Output:
# "1a"
# 
# 
# 
# Example 2:
# 
# Input:
# -1
# 
# Output:
# "ffffffff"
# 
# 
#

hex_map = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        flag = False
        if num < 0:
            flag = True
            num = - num
        h = ''
        # while num:
        #     h += hex_map[num % 16]
        #     num = num / 16
        while num:
            h = hex_map[num % 2] + h
            num = num / 2
        
        h = h.zfill(8 * 4)
        b = ''
        
        if flag:
            for i in h:
                b += '0' if i == '1' else '1'
            b = bin(int(b, 2) + 1)[2:]
        else:
            b = h
        b = b.lstrip("0")
        r = ''
        while b:
            t = b[-4:]
            b = b[:-4]
            r = hex_map[int(t, 2)] + r
        
        return r if r else '0'

# if __name__ == "__main__":
#     s = Solution()
#     print s.toHex(26)
#     print s.toHex(-1)
