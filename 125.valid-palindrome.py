#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (30.25%)
# Total Accepted:    328.2K
# Total Submissions: 1.1M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
# 
# Example 1:
# 
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "race a car"
# Output: false
# 
# 
#
import string

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        valid_string = string.lowercase + string.uppercase + string.ascii_letters + string.digits
        while i < j:
            while s[i] not in valid_string:
                i += 1
                if i >= len(s):
                    return True
            while s[j] not in valid_string:
                j -= 1
                if j < 0:
                    return True
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True

# if __name__ == "__main__":
#     s = Solution()
#     s.isPalindrome("A man, a plan, a canal: Panama")