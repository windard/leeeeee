# coding=utf-8
#
# @lc app=leetcode id=984 lang=python
#
# [984] String Without AAA or BBB
#
# https://leetcode.com/problems/string-without-aaa-or-bbb/description/
#
# algorithms
# Easy (32.33%)
# Likes:    112
# Dislikes: 178
# Total Accepted:    11K
# Total Submissions: 32K
# Testcase Example:  '1\n2'
#
# Given two integers A and B, return any string S such that:
# 
# 
# S has length A + B and contains exactly A 'a' letters, and exactly B 'b'
# letters;
# The substring 'aaa' does not occur in S;
# The substring 'bbb' does not occur in S.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: A = 1, B = 2
# Output: "abb"
# Explanation: "abb", "bab" and "bba" are all correct answers.
# 
# 
# 
# Example 2:
# 
# 
# Input: A = 4, B = 1
# Output: "aabaa"
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= A <= 100
# 0 <= B <= 100
# It is guaranteed such an S exists for the given A and B.
# 
# 
#


class Solution(object):
    def _strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        # Wrong With 1,3
        flag = True
        a_index = 0
        b_index = 0
        result = ""
        while a_index < A or b_index < B:
            if flag:
                if A - a_index >= 2:
                    result += "aa"
                elif A - a_index >= 1:
                    result += "a"
                a_index += 2

            else:
                if B - b_index >= 2:
                    result += "bb"
                elif B - b_index >= 1:
                    result += "b"
                b_index += 2
            flag = not flag

        return result

    def _strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        # Still Wrong
        flag = True
        a_index = 0
        b_index = 0
        result = ""
        while a_index < A or b_index < B:
            if flag:
                if a_index < A:
                    result += "a"
                a_index += 1
            else:
                if b_index < B:
                    result += "b"
                b_index += 1
            flag = not flag

        return result

    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        if A > B:
            preview = A * 'a'
            fix = 'b'
            last = A / 2
            remain = B
        else:
            preview = B * 'b'
            fix = 'a'
            last = B / 2
            remain = A
        result = ""
        for i in range(0, len(preview), 2):
            result += preview[i:i+2]
            if remain >= 2 and remain > last:
                result += fix * 2
                remain -= 2
                last -= 1
            elif remain >= 1:
                result += fix * 1
                remain -= 1
        return result


# if __name__ == '__main__':
#     s = Solution()
#     # print s.strWithout3a3b(1, 2)
#     # print s.strWithout3a3b(4, 1)
#     # print s.strWithout3a3b(0, 0)
#     # print s.strWithout3a3b(1, 0)
#     # print s.strWithout3a3b(1, 3)
#     # print s.strWithout3a3b(5, 10)
#     print s.strWithout3a3b(8, 12)
#     print s.strWithout3a3b(6, 12)
#     print s.strWithout3a3b(12, 6)

