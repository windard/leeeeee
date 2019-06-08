#
# @lc app=leetcode id=204 lang=python
#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (28.26%)
# Total Accepted:    220K
# Total Submissions: 773.3K
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
# 
# Example:
# 
# 
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# 
# 
#
import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        l = range(n)
        l[1] = 0
        res = 0
        for v in l:
            if v == 0:
                continue
            res += 1
            for i in xrange(v, n, v):
                l[i] = 0
        return res

    def ____countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time Limit
        # 思路是对的
        # 方法不对
        if n <= 2:
            return 0
        answer = range(3, n+1, 2)
        primes = 1
        while answer:
            primes += 1
            prime = answer.pop(0)
            for i in answer:
                if i % prime == 0:
                    answer.remove(i)

        return primes

    def ___countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 时间换空间
        # Set is unordered
        # List is ordered
        # Time Limit
        if n <= 2:
            return 0
        primes = [2]
        index = 3
        res = 1
        while index < n:
            for key in primes:
                if key > math.sqrt(index):
                    res += 1
                    primes.append(index)
                    break
                if index % key == 0:
                    break
            index += 2
        return res

    def __countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time Limit 
        # 499979 
        # 1500000
        res = []
        if n > 2:
            res.append(2)
        for i in range(3, n, 2):
            if i in [2,3]:
                res.append(i)
                continue
            for j in res:
                if j > math.sqrt(n):
                    res.append(i)
                    break
                if i % j == 0:
                    break
            else:
                res.append(i)
        return len(res)

    def _countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time Limit 
        # 499979
        res = []
        for i in range(2, n):
            if self.isPrime(i):
                res.append(i)
        return len(res)
    
    def isPrime(self, n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        i = 3
        if n % 2 == 0:
            return False
        while i <= n / 2:
            if n % i == 0:
                return False
            i += 2
        return True

# if __name__ == "__main__":
#     s = Solution()
#     print s.countPrimes(10)         # 4
#     print s.countPrimes(100)        # 25
#     print s.countPrimes(400000)     # 33860
#     print s.countPrimes(999983)     # 78497
#     print s.countPrimes(1500000)    # 114155
