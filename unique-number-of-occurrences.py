# coding=utf-8


class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        from collections import Counter
        c = Counter(arr)
        return len(set(c.values())) == len(c.values())


if __name__ == '__main__':
    s = Solution()
    # False
    print s.uniqueOccurrences([1,2])
    # True
    print s.uniqueOccurrences([1,2,2,1,1,3])
    # True
    print s.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])