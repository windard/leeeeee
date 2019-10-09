# coding=utf-8


class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        # 最长等差子序列
        last = {}
        for a in arr:
            if a - difference in last:
                last[a] = last[a - difference] + 1
                if a != a - difference:
                    del last[a - difference]
            elif a not in last:
                last[a] = 1
        return max(last.values())


if __name__ == '__main__':
    s = Solution()
    print s.longestSubsequence([1,5,7,8,5,3,4,2,1], -2)
    print s.longestSubsequence([3,3,3], 0)
    print s.longestSubsequence([1,2,3,4], 1)
    print s.longestSubsequence([1,3,5,7], 1)
    print s.longestSubsequence([1,5,7,8,5,3,4,2,1], -2)
    print s.longestSubsequence([4,12,10,0,-2,7,-8,9,-9,-12,-12,8,8], 0)
    print s.longestSubsequence([7,-2,8,10,6,18,9,-8,-5,18,13,-6,-17,-1,-6,-9,9,9], 1)
