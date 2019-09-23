# coding=utf-8


class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        # 使用二分
        # 最大值为 2*10**9
        left = 1
        right = 2 * 10**9
        while left <= right:
            mid = (left + right) / 2
            count = self.count(mid, a, b, c)
            if count > n:
                right = mid - 1
            elif count < n:
                left = mid + 1
            else:
                if self.count(mid - 1, a, b, c) == n:
                    right = mid
                else:
                    return mid

    def __nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        # clear to the true answer
        common = reduce(self.lcm, [a, b, c])
        # common_nums = []
        # length = 0
        # i = 1
        # while i <= common:
        # for i in range(1, common):
        #     if not i % a or not i % b or not i % c:
        #         common_nums.append(i)
        #         length += 1
        #     i += 1
        length = common / a + common / b + common / c - \
                 common / (a * b) - common / (a * c) - common / (b * c)
        step, left = divmod(n, length)
        length = 0
        l_a = l_b = l_c = 1
        ugly = 0
        while length < left:
            ugly = min(a * l_a, b * l_b, c * l_c)
            length += 1
            while a * l_a <= ugly:
                l_a += 1
            while b * l_b <= ugly:
                l_b += 1
            while c * l_c <= ugly:
                l_c += 1
        return step * common + ugly

    def count(self, n, a, b, c):
        return n / a + n / b + n / c - \
               n / self.lcm(a, b) - n / self.lcm(a, c) - n / self.lcm(b, c) + \
               n / reduce(self.lcm, [a, b, c])

    def gcd(self, a, b):
        a, b = max(a, b), min(a, b)
        while b:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        return a * b / self.gcd(a, b)

    def _nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        # 与之前的定义不一样
        # 之前的定义是只能被这些因子整除
        # 现在的定义是可以被这些因子整除
        # Time Limit
        l_a = l_b = l_c = 1
        uglys = []
        length = 0
        while length < n:
            ugly = min(a * l_a, b * l_b, c * l_c)
            uglys.append(ugly)
            length += 1
            while a * l_a <= ugly:
                l_a += 1
            while b * l_b <= ugly:
                l_b += 1
            while c * l_c <= ugly:
                l_c += 1
        return uglys[-1]


# if __name__ == '__main__':
#     s = Solution()
#     print s.nthUglyNumber(3, 2, 3, 5)
#     print s.nthUglyNumber(4, 2, 3, 4)
#     print s.nthUglyNumber(5, 2, 11, 13)
#     print s.nthUglyNumber(1000000000, 2, 217983653, 336916467)
