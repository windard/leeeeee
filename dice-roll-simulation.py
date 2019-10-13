# coding=utf-8


class Solution(object):
    def _dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        # Too Complex And Wrong
        total = 6 ** n
        # for roll in rollMax:
        #     if roll < n:
                # Wrong Answer
                # total -= 6 ** (n - roll - 1)
                # Wrong Answer
                # for i in range(roll, n):
                #     total -= 6 ** (i-1)
                # 这样计算会 Time Limit
        data = {}
        for roll in rollMax:
            data[roll] = data.get(roll, 0) + 1
        for roll, time in data.items():
            if roll < n:
                plus = 0
                for i in range(roll+1, n+1):
                    plus += (n - i + 1) * (5 ** (n - i))
                total -= plus * time
        return total % (10**9 + 7)

    def __dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        # 所有你解决不了的问题
        # 最后都是动态规划问题
        # 六维动态规划方程
        # 表示分别以对应数字开头的结果的n次抛出数量
        # Wrong Answer
        dp = [[[0] * n] for _ in range(6)]
        for i in range(n):
            for j in range(6):
                if not i:
                    dp[j][i] = 1
                else:
                    if rollMax[j] - i > 0:
                        dp[j][i] = 6 * dp[j][i-1]
                    else:

                        dp[j][i] = 5 * dp[j][i-1]

    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        # 动态转移方程
        # 是以该数字结尾的数量
        # dp[j][i] = sum()
        dp = [[0] * n for _ in range(6)]
        for i in range(n):
            for j in range(6):
                if not i:
                    dp[j][i] = 1
                else:
                    if rollMax[j] - i > 0:
                        dp[j][i] = sum([dp[m][i-1] for m in range(6)])
                    else:
                        for n in range(1, rollMax[j]+1):
                            dp[j][i] += sum([dp[m][i-n] for m in range(6) if m != j])
        return sum([dp[m][-1] for m in range(6)]) % (10**9 + 7)


if __name__ == '__main__':
    s = Solution()
    print s.dieSimulator(2, [1,1,2,2,2,3])
    print s.dieSimulator(2, [1,1,1,1,1,1])
    print s.dieSimulator(3, [1,1,1,2,2,3])
    print s.dieSimulator(4, [2,1,1,3,3,2])

    # result = []
    # for i in range(1, 7):
    #     for j in range(1, 7):
    #         for l in range(1, 7):
    #             for m in range(1,7):
    #                 result.append('{}{}{}{}'.format(i,j,l,m))
    # print len(result)
    # print len(filter(lambda x: '22' in x and '222' not in x, result))
    # print filter(lambda x: '22' in x and '222' not in x, result)
    # print len(filter(lambda x: '22' not in x, result))
    # print len(filter(lambda x: '222' in x, result))
    # print len(filter(lambda x: '2222' in x, result))
    # result = filter(lambda x: '22' not in x, result)
    # print len(result)
    # result = filter(lambda x: '33' not in x, result)
    # print len(result)
    # result = filter(lambda x: '111' not in x, result)
    # result = filter(lambda x: '666' not in x, result)
    # result = filter(lambda x: '4444' not in x, result)
    # result = filter(lambda x: '5555' not in x, result)
    # print len(result)
