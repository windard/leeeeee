# coding=utf-8


class Solution(object):
    def fraction(self, cont):
        """
        :type cont: List[int]
        :rtype: List[int]
        """
        a, b = cont[-1], 1
        for c in cont[::-1][1:]:
            a, b = self.add(c, b, a)
        return a, b

    def add(self, a, b, c):
        b += a * c
        d = self.gcd(b, c)
        return b / d, c / d

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a


if __name__ == '__main__':
    s = Solution()
    print s.add(1, 1, 3)
    print s.add(1, 3, 1)
    print s.fraction([3, 2, 0, 2])
    print s.fraction([0, 0, 3])
    print s.fraction([5])
