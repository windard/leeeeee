# coding=utf-8


class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        need = {}
        for i in 'balloon':
            need[i] = need.get(i, 0) + 1

        max_count = float("inf")
        data = {}
        for i in text:
            data[i] = data.get(i, 0) + 1

        for k, v in need.items():
            count = data.get(k, 0) / v
            max_count = min(max_count, count)

        return max_count


if __name__ == '__main__':
    s = Solution()
    print s.maxNumberOfBalloons("")
    print s.maxNumberOfBalloons("loonbalxballpoon")
    print s.maxNumberOfBalloons("leetcode")
    print s.maxNumberOfBalloons("nlaebolko")
