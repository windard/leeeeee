# coding=utf-8
#
# @lc app=leetcode id=93 lang=python
#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (32.16%)
# Likes:    757
# Dislikes: 316
# Total Accepted:    150.1K
# Total Submissions: 465.5K
# Testcase Example:  '"25525511135"'
#
# Given a string containing only digits, restore it by returning all possible
# valid IP address combinations.
# 
# Example:
# 
# 
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
# 
# 
#


class Solution(object):
    def _restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # Wrong Answer
        # 0279245587303 is sooooo long
        result = self.depth(s)
        return map(lambda x: ".".join(x), filter(lambda x: len(x) > 3, result))

    def depth(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        if not s:
            return result

        first = self.depth(s[1:])

        if first:
            for f in first:
                if len(f) > 3:
                    continue
                result.append([s[:1]]+f)
        else:
            result.append([s[:1]])

        if len(s) > 1:
            if 9 < int(s[:2]) < 100:
                second = self.depth(s[2:])
                if second:
                    for e in second:
                        if len(e) > 3:
                            continue
                        result.append([s[:2]]+e)
                else:
                    result.append([s[:2]])
        if len(s) > 2:
            if 99 < int(s[:3]) < 256:
                third = self.depth(s[3:])
                if third:
                    for t in third:
                        if len(t) > 3:
                            continue
                        result.append([s[:3]]+t)
                else:
                    result.append([s[:3]])
        return result

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # 回溯
        # 加约束条件
        # 递归

        result = []

        def backtrack(nums, path):
            if len(path) == 4:
                if not nums:
                    result.append(".".join(reversed(path)))
                return
            if not nums:
                return
            backtrack(nums[1:], [nums[:1]]+path)
            if len(nums) > 1:
                if 9 < int(nums[:2]) < 100:
                    backtrack(nums[2:], [nums[:2]]+path)
            if len(nums) > 2:
                if 99 < int(nums[:3]) < 256:
                    backtrack(nums[3:], [nums[:3]]+path)

        backtrack(s, [])
        return result


# if __name__ == '__main__':
#     s = Solution()
#     print s.restoreIpAddresses("010010")
#     print s.restoreIpAddresses("0279245587303")
#     print s.restoreIpAddresses("0000")
#     print s.restoreIpAddresses("1111")
#     print s.restoreIpAddresses("25525511135")
