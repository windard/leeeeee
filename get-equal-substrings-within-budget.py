# coding=utf-8


class Solution(object):
    def _equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        # max sub string
        # 字符串匹配 + 字符串转换
        # O(m*n)
        # 估计会超时
        # 题意理解错了，不是字符串匹配，不能移动，就是一对一
        max_length = 0
        for i in range(len(s)):
            cost = 0
            length = 0
            for j in range(len(t)):
                if i+j < len(s):
                    c = abs(ord(s[i+j]) - ord(t[j]))
                    if c + cost > maxCost:
                        cost = c
                        length = 1
                    else:
                        cost += c
                        length += 1
                    max_length = max(length, max_length)
        return max_length

    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        # 一对一
        # O(n)
        # 字符串长度相同
        # 滑动窗口问题
        # 双指针
        if not s:
            return 0
        ts = map(lambda x: abs(ord(x[0]) - ord(x[1])), zip(list(s), list(t)))
        max_length = 0
        start = end = cost = 0
        while end < len(ts):
            if cost + ts[end] <= maxCost:
                cost += ts[end]
                end += 1
                max_length = max(max_length, end - start)
            else:
                if start < end:
                    cost -= ts[start]
                    start += 1
                else:
                    start = end = end + 1
        return max_length


if __name__ == '__main__':
    s = Solution()
    print s.equalSubstring("abcd", "bcdf", 3)
    print s.equalSubstring("abcd", "cdef", 3)
    print s.equalSubstring("abcd", "acde", 0)
