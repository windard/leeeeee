#
# @lc app=leetcode id=541 lang=python
#
# [541] Reverse String II
#
# https://leetcode.com/problems/reverse-string-ii/description/
#
# algorithms
# Easy (45.04%)
# Likes:    247
# Dislikes: 749
# Total Accepted:    60.3K
# Total Submissions: 132.3K
# Testcase Example:  '"abcdefg"\n2'
#
# 
# Given a string and an integer k, you need to reverse the first k characters
# for every 2k characters counting from the start of the string. If there are
# less than k characters left, reverse all of them. If there are less than 2k
# but greater than or equal to k characters, then reverse the first k
# characters and left the other as original.
# 
# 
# Example:
# 
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# 
# 
# 
# Restrictions: 
# 
# ⁠The string consists of lower English letters only.
# ⁠Length of the given string and k will in the range [1, 10000]
# 
#
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        index = 0
        s = list(s)
        while index < len(s):
            s[index:index+k] = s[index:index+k][::-1]
            index += k*2
        
        return ''.join(s)
    
# if __name__ == "__main__":
#     s = Solution()
#     print s.reverseStr("abcdefg", 2)
#     print s.reverseStr("abcdefg", 3)
#     print s.reverseStr("abcdefg", 4)
