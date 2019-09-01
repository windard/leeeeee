# coding=utf-8
import math


class Solution(object):
    def prime_arrangements(self, n):
        from math import factorial
        self.count = 0
        primes = set()
        index = 2
        while index <= n:
            for p in primes:
                if not index % p:
                    break
            else:
                primes.add(index)
            index += 1
        prime_length = len(primes)
        no_prime_length = n - prime_length
        return factorial(prime_length) * factorial(no_prime_length) % (10**9+7)

    def __prime_arrangements(self, n):
        # Time Limit
        # 不能硬上，应该是算出来的
        self.count = 0
        primes = set()
        index = 2
        while index <= n:
            for p in primes:
                if not index % p:
                    break
            else:
                primes.add(index)
            index += 1

        def trackback(nodes, path):
            if path:
                poi = len(path)
                if poi in primes and path[-1] not in primes:
                    return
            if not nodes:
                self.count += 1

            for i, node in enumerate(nodes):
                trackback(nodes[:i]+nodes[i+1:], path+[node])

        trackback(range(1, n+1), [])
        return self.count % (10**9+7)

    def _prime_arrangements(self, n):
        # 理解错题意

        output = []

        def check_prime(nodes):
            print nodes
            num = int(''.join(map(str, nodes)))
            i = 2
            while i <= math.sqrt(num):
                if not num % i:
                    return False
                i += 1
            return True

        def backtrack(nums, nodes):
            if not nums:
                if check_prime(nodes):
                    output.append(nodes)
            for i, v in enumerate(nums):
                backtrack(nums[:i]+nums[i+1:], nodes+[v])
        backtrack(range(1, n+1), [])
        return len(output)


if __name__ == '__main__':
    s = Solution()
    print s.prime_arrangements(5)
    print s.prime_arrangements(100)
