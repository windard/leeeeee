#
# @lc app=leetcode id=468 lang=python
#
# [468] Validate IP Address
#
# https://leetcode.com/problems/validate-ip-address/description/
#
# algorithms
# Medium (20.96%)
# Likes:    137
# Dislikes: 809
# Total Accepted:    30.4K
# Total Submissions: 141.2K
# Testcase Example:  '"172.16.254.1"'
#
# 
# Write a function to check whether an input string is a valid IPv4 address or
# IPv6 address or neither.
# 
# 
# 
# IPv4 addresses are canonically represented in dot-decimal notation, which
# consists of four decimal numbers, each ranging from 0 to 255, separated by
# dots ("."), e.g.,172.16.254.1;
# 
# 
# 
# Besides, leading zeros in the IPv4 is invalid. For example, the address
# 172.16.254.01 is invalid.
# 
# 
# 
# IPv6 addresses are represented as eight groups of four hexadecimal digits,
# each group representing 16 bits. The groups are separated by colons (":").
# For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid
# one. Also, we could omit some leading zeros among four hexadecimal digits and
# some low-case characters in the address to upper-case ones, so
# 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading
# zeros and using upper cases).
# 
# 
# 
# 
# However, we don't replace a consecutive group of zero value with a single
# empty group using two consecutive colons (::) to pursue simplicity. For
# example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.
# 
# 
# 
# Besides, extra leading zeros in the IPv6 is also invalid. For example, the
# address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.
# 
# 
# 
# Note:
# You may assume there is no extra space or special characters in the input
# string.
# 
# 
# Example 1:
# 
# Input: "172.16.254.1"
# 
# Output: "IPv4"
# 
# Explanation: This is a valid IPv4 address, return "IPv4".
# 
# 
# 
# 
# Example 2:
# 
# Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"
# 
# Output: "IPv6"
# 
# Explanation: This is a valid IPv6 address, return "IPv6".
# 
# 
# 
# Example 3:
# 
# Input: "256.256.256.256"
# 
# Output: "Neither"
# 
# Explanation: This is neither a IPv4 address nor a IPv6 address.
# 
# 
#

import re


class Solution(object):
    def _validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        # not include in standard library
        import ipaddress

        try:
            ip = ipaddress.ip_address(IP)
            if isinstance(ip, ipaddress.IPv4Address):
                return "IPv4"
            else:
                return "IPv6"
        except:
            return "Neither"

    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if self.validateIPv4Address(IP):
            return "IPv4"
        elif self.validateIPv6Address(IP):
            return "IPv6"
        return "Neither"

    def validateIPv4Address(self, IP):
        pattern = re.compile(r'^'
                             r'(1[\d]{0,2}|[1-9]?\d|2[0-4]\d|25[0-5])'
                             r'(\.(?:1[\d]{0,2}|[1-9]?\d|2[0-4]\d|25[0-5])){3}'
                             r'$')
        return bool(re.match(pattern, IP))

    def validateIPv6Address(self, IP):
        pattern = re.compile(r"^([0-9a-fA-F][0-9a-fA-F]{0,3}|0{1-4})"
                             r"(:[0-9a-fA-F][0-9a-fA-F]{0,3}|0{1-4}){7}$")
        return bool(re.match(pattern, IP))


# if __name__ == '__main__':
#     s = Solution()
#     print s.validIPAddress("127.0.0.1")
#     print s.validIPAddress("172.16.254.1")
#     print s.validIPAddress("172.16.254.01")
#     print s.validIPAddress("2001:0db8:85a3:0000:0000:8a2e:0370:7334")
#     print s.validIPAddress("2001:db8:85a3:0:0:8A2E:0370:7334")
#     print s.validIPAddress("2001:0db8:85a3::8A2E:0370:7334")
#     print s.validIPAddress("02001:0db8:85a3:0000:0000:8a2e:0370:7334")
