# coding=utf-8
#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (26.07%)
# Total Accepted:    737K
# Total Submissions: 2.8M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
#
#
# Example 1:
#
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
#
# Example 2:
#
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
#
# Example 3:
#
#
# Input: "pwwkew"

#
#
#


class Solution(object):
    def _lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # O(n*n)
        st = ''
        length = 0
        for i in s:
            index = st.find(i)
            if index >= 0:
                if len(st) > length:
                    length = len(st)
                st = st[index+1:]
            st += i

        return len(st) if len(st) > length else length

    def __lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 遇见重复字符
        # 即非开始
        # 也非结束
        index = 0
        max_count = 0
        data = {}
        while index < len(s):
            if s[index] not in data:
                max_count = max(max_count, len(data)+1)
            else:
                data = {}
            data[s[index]] = index
            index += 1
        return max_count

    def ___lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 看似简单，写起来挺复杂的
        index = 0
        max_count = 0
        data = {}
        temp = ''
        while index < len(s):
            temp += s[index]
            if s[index] not in data:
                max_count = max(len(temp), max_count)
            else:
                pos = -(index-data[s[index]])
                for t in temp[:pos]:
                    del data[t]
                temp = temp[pos:]
            data[s[index]] = index
            index += 1
        return max_count

    def ____lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 滑动窗口
        # O(2*n)
        st = set()
        length = 0
        index = 0
        for i, v in enumerate(s):
            if v not in st:
                length = max(length, i - index + 1)
            else:

                while v in st:
                    st.remove(s[index])
                    index += 1
            st.add(v)
        return length

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 滑动窗口
        # O(n)
        data = {}
        count = 0
        index = 0
        i = 0
        while index < len(s):
            if s[index] in data:
                i = max(data[s[index]]+1, i)
            count = max(count, index - i + 1)
            data[s[index]] = index
            index += 1
        return count


# if __name__ == '__main__':
#     s = Solution()
#     print s.lengthOfLongestSubstring("abbca")
#     print s.lengthOfLongestSubstring("abcb")
#     print s.lengthOfLongestSubstring("aabaab!bb")
#     print s.lengthOfLongestSubstring("tmmzuxt")
#     print s.lengthOfLongestSubstring("dvdf")
#     print s.lengthOfLongestSubstring("abcabcbb")
#     print s.lengthOfLongestSubstring("bbbbb")
#     print s.lengthOfLongestSubstring("pwwkew")
#     print s.lengthOfLongestSubstring("abbccdde")
