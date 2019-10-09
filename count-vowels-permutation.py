# coding=utf-8


class Solution(object):
    def _countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 继续回溯

        a = ['a', 'ae']
        e = ['e', 'ea', 'ei']
        i = ['i', 'ia', 'ie', 'io', 'iu']
        o = ['o', 'oi', 'ou']
        u = ['u', 'ua']
        vowels = filter(lambda x: len(x) < 2, a+e+i+o+u)
        groups = filter(lambda x: len(x) > 1, a+e+i+o+u)

        global count
        count = 0

        def backtrack(sources):
            global count
            if len(sources) == n:
                count += 1
                count %= 10**9 + 7
                return

            for group in groups:
                if group.startswith(sources[-1]):
                    backtrack(sources+group[1])

        for v in vowels:
            backtrack(v)

        return count

    def __countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        # little improve
        # but still time limit

        groups = {
            'a': ['e'],
            'e': ['a', 'i'],
            'i': ['a', 'e', 'o', 'u'],
            'o': ['i', 'u'],
            'u': ['a']
        }

        global count
        count = 0

        def backtrack(sources, vowel):
            global count
            if len(sources) == n:
                count += 1
                return

            for g in groups.get(vowel):
                backtrack(sources+g, g)

        for v in groups.keys():
            backtrack(v, v)

        return count % (10**9 + 7)

    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        # to be honest
        # this is dynamic program
        groups = {
            'a': ['e'],
            'e': ['a', 'i'],
            'i': ['a', 'e', 'o', 'u'],
            'o': ['i', 'u'],
            'u': ['a']
        }
        counts = [[] for _ in range(n)]
        counts[0] = [1, 1, 1, 1, 1]
        index = 1
        while index < n:
            a, e, i, o, u = counts[index-1]
            counts[index] = [e+i+u, a+i, e+o, i, i+o]
            index += 1
        return sum(counts[-1]) % (10**9 + 7)


if __name__ == '__main__':
    s = Solution()
    print s.countVowelPermutation(1)
    print s.countVowelPermutation(2)
    print s.countVowelPermutation(5)
    print s.countVowelPermutation(144)
