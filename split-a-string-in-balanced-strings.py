# coding=utf-8


class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        ln = rn = 0
        result = []
        current = ''
        for n in s:
            if n == 'L':
                ln += 1
            else:
                rn += 1
            current += n
            if ln == rn:
                result.append(current)
                current = ''
                ln = rn = 0
        return len(result)


if __name__ == '__main__':
    s = Solution()
    print s.balancedStringSplit("RLRRLLRLRL")
    print s.balancedStringSplit("RLLLLRRRLR")
    print s.balancedStringSplit("LLLLRRRR")
