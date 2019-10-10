# coding=utf-8


class Solution(object):
    def game(self, guess, answer):
        """
        :type guess: List[int]
        :type answer: List[int]
        :rtype: int
        """
        return len(filter(lambda x: x[0] == x[1], zip(guess, answer)))


if __name__ == '__main__':
    s = Solution()
    print s.game([1,2,3], [1,2,3])
    print s.game([2,2,3], [3,2,1])
