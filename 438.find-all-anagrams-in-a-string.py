# coding=utf-8
# @lc app=leetcode id=438 lang=python
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Easy (36.02%)
# Total Accepted:    104.8K
# Total Submissions: 290.1K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given a string s and a non-empty string p, find all the start indices of p's
# anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both
# strings s and p will not be larger than 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
#
#
# Example 2:
#
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#
#
#

import collections
import string

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # fast
        # very unimaginable solution
        # 用比特位
        # 使用比特位进行字符串比较也是一个好主意
        bit_map = dict(zip(string.lowercase, map(lambda i:2**i, range(1, 27))))
        flag = 0
        res = []
        for i in range(len(s)):
            flag += bit_map[p[0]]
            flag -= bit_map[s[i]]
            if flag == 0 and i >= len(p)-1:
                res.append(i - len(p) + 1)
            p = p[1:]+s[i]
        return res

    def findAnagramss(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # faster
        res = []

        pd = {}
        for i in p:
            pd[i] = pd.get(i, 0) + 1

        sd = {}
        len_p = len(p)
        for i in range(len(s)):
            sd[s[i]] = sd.get(s[i], 0) + 1
            if i >= len_p:
                sd[s[i-len_p]] -= 1
                if sd[s[i-len_p]] == 0:
                    del sd[s[i-len_p]]
            if sd == pd:
                res.append(i - len_p + 1)
        return res

    def findAnagramsss(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # faster too
        res = []

        pd = {}
        for i in p:
            pd[i] = pd.get(i, 0) + 1

        sd = {}
        len_s = len(s)
        len_p = len(p)
        last_index = -len_p
        for i in range(len_s):
            sd[s[i]] = sd.get(s[i], 0) + 1
            if i >= len_p:
                sd[s[i-len_p]] -= 1
                if sd[s[i-len_p]] == 0:
                    del sd[s[i-len_p]]
            if i - last_index < len_p and i < len_s - len_p:
                bp = {}
                ap = {}
                for j in range(last_index, i):
                    bp[s[j]] = bp.get(s[j], 0) + 1
                for j in range(len_p+last_index, i+len_p):
                    ap[s[j]] = ap.get(s[j], 0) + 1
                if bp == ap:
                    last_index = i
                    res.append(i)
                    continue
            if sd == pd:
                last_index = i - len_p + 1
                res.append(last_index)
        return res

    def diff(self, s, p):
        # return s == p
        # 多一个方法调用，就要慢一些
        sd = {}
        if not isinstance(s, dict):
            for i in s:
                sd[i] = sd.get(i, 0) + 1
        else:
            sd = s
        
        pd = {}
        if not isinstance(p, dict):
            for i in p:
                pd[i] = pd.get(i, 0) + 1
        else:
            pd = p
        
        return sd == pd

    def findAnagramssss(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # slow too mach
        rest = []
        length_p = len(p)
        last_index = -length_p
        for i in range(len(s)-length_p+1):
            if i - last_index < length_p:
                if self.__checkMatch(s[last_index:i], s[last_index+length_p:length_p+i]):
                    rest.append(i)
                    last_index = i
            elif self.__checkMatch(p, s[i:i + len(p)]):
                rest.append(i)
                last_index = i
        return rest

    def checkMatch(self, s, p):
        # abb & aab
        for i in s:
            if i not in p:
                return False
        for i in p:
            if i not in s:
                return False
        return True

    def _checkMatch(self, s, p):
        # time limit O(n^2)
        if len(s) != len(p):
            return False
        s = list(s)
        p = list(p)
        for k,v in enumerate(s):
            if p[k] != v:
                return False
        return True

    def __checkMatch(self, s, p):
        # time limit O(n^3)
        if len(s) != len(p):
            return False
        p = list(p)
        for i in s:
            try:
                p.remove(i)
            except ValueError:
                return False
        return True

    def match(self, s, p):
        # time limit
        sl = {}
        pl = {}
        for i in s:
            if i in sl.keys():
                sl[i] += 1
            else:
                sl[i] = 1
        for i in p:
            if i in pl.keys():
                pl[i] += 1
            else:
                pl[i] = 1
        return pl == sl

    def compare(self, s, p):
        # time limit
        # slower than match
        s = collections.Counter(s)
        p = collections.Counter(p)
        return s == p

    def copy(self, s, p):
        ns, np = len(s), len(p)
        d = {}
        for c in p:
            d[c] = d.get(c, 0) + 1
        res = []
        i = 0
        for j in xrange(ns):
            if s[j] not in d:
                for k in xrange(i, j):
                    d[s[k]] += 1
                i = j + 1
            elif d[s[j]] == 0:
                while s[i] != s[j]:
                    d[s[i]] += 1
                    i += 1
                i += 1
            else:
                d[s[j]] -= 1
                if j - i + 1 == np:
                    res.append(i)
                    d[s[i]] += 1
                    i += 1
        return res

    def copy_again(self, s, p):
        pmap = {}
        for i in p:
            pmap[i] = pmap.get(i,0) + 1
        plenth = len(p)

        rlist = []
        rmap = {}

        for i , v in enumerate(s):
            rmap[v] = rmap.get(v,0) + 1
            if rmap == pmap:
                rlist.append(i-plenth+1)
            if i - plenth + 1 >= 0:
                rmap[s[i-plenth + 1]] = rmap.get(s[i-plenth + 1]) - 1
                if rmap[s[i-plenth + 1]] == 0:
                    del rmap[s[i-plenth + 1]]
               
        return rlist

if __name__ == "__main__":
    s = Solution()
    import time
    a = time.time()
    s.findAnagrams('a'*20001, 'a'*10000)
    print time.time()-a
    b = time.time()
    s.findAnagramss('a'*20001, 'a'*10000)
    print time.time() -b
    c = time.time()
    s.findAnagramsss('a'*20001, 'a'*10000)
    print time.time()-c
    d = time.time()
    s.findAnagramssss('a'*20001, 'a'*10000)
    print time.time() -d
