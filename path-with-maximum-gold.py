# coding=utf-8

from copy import deepcopy
import sys


class TailRecurseException:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tail_call_optimized(g):
    def func(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back \
            and f.f_back.f_back.f_code == f.f_code:
            # 抛出异常
            raise TailRecurseException(args, kwargs)
        else:
            while 1:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException, e:
                    args = e.args
                    kwargs = e.kwargs
    func.__doc__ = g.__doc__
    return func


class Solution(object):
    def _getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 深度优先遍历 + 部分剪枝
        # 回溯
        # Time Limit
        if not grid or not grid[0]:
            return 0

        self.max_count = 0

        # @tail_call_optimized
        def backtrack(m, n, count, golds):
            self.max_count = max(self.max_count, count)
            if m and golds[m-1][n]:
                coin = golds[m-1][n]
                new_grid = deepcopy(golds)
                new_grid[m-1][n] = 0
                backtrack(m-1, n, count+coin, new_grid)
            if n and golds[m][n-1]:
                coin = golds[m][n-1]
                new_grid = deepcopy(golds)
                new_grid[m][n-1] = 0
                backtrack(m, n-1, count+coin, new_grid)
            if m < len(grid) - 1 and golds[m+1][n]:
                coin = golds[m+1][n]
                new_grid = deepcopy(golds)
                new_grid[m+1][n] = 0
                backtrack(m+1, n, count+coin, new_grid)
            if n < len(golds[0]) - 1 and golds[m][n+1]:
                coin = golds[m][n+1]
                new_grid = deepcopy(golds)
                new_grid[m][n+1] = 0
                backtrack(m, n+1, count+coin, new_grid)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    coin = grid[i][j]
                    new_grid = deepcopy(grid)
                    new_grid[i][j] = 0
                    backtrack(i, j, coin, new_grid)

        return self.max_count

    def __getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 可以用贪心策略 剪枝
        # 不然太复杂了
        # Wrong Answer
        if not grid or not grid[0]:
            return 0

        self.max_count = 0

        def backtrack(m, n, count, golds):
            self.max_count = max(self.max_count, count)
            left = right = up = down = 0
            if m and golds[m-1][n]:
                up = golds[m-1][n]
            if n and golds[m][n-1]:
                left = golds[m][n-1]
            if m < len(grid) - 1 and golds[m+1][n]:
                down = golds[m+1][n]
            if n < len(golds[0]) - 1 and golds[m][n+1]:
                right = golds[m][n+1]

            max_pos = sorted([[left, 0], [right, 1], [up, 2], [down, 3]],
                             key=lambda x: x[0], reverse=True)[0]

            if max_pos[0] == 0:
                return

            if max_pos[1] == 0:
                coin = golds[m][n-1]
                new_grid = deepcopy(golds)
                new_grid[m][n-1] = 0
                backtrack(m, n-1, count+coin, new_grid)
            elif max_pos[1] == 1:
                coin = golds[m][n+1]
                new_grid = deepcopy(golds)
                new_grid[m][n+1] = 0
                backtrack(m, n+1, count+coin, new_grid)
            elif max_pos[1] == 2:
                coin = golds[m-1][n]
                new_grid = deepcopy(golds)
                new_grid[m-1][n] = 0
                backtrack(m-1, n, count+coin, new_grid)
            else:
                coin = golds[m+1][n]
                new_grid = deepcopy(golds)
                new_grid[m+1][n] = 0
                backtrack(m+1, n, count+coin, new_grid)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    coin = grid[i][j]
                    new_grid = deepcopy(grid)
                    new_grid[i][j] = 0
                    backtrack(i, j, coin, new_grid)

        return self.max_count

    def ___getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 不能用贪心算法
        # 只取到了当前最优解
        # 换个思路，虽然当前取的少，但是可以取的久吖
        # 多取几个，总数就取的多了
        # 按照第一个算法的两种优化思路
        # 1. 尾递归优化
        # 2. 确定查找方向，所有的人，只往右下寻找即可
        # 第二种方案 Wrong Answer
        # 不能确定方向，挖矿路线可以九曲连环
        # 第一种方案 Wrong Answer
        # 并不是完全的尾递归，会有误差
        if not grid or not grid[0]:
            return 0

        self.max_count = 0

        def backtrack(m, n, count, golds):
            self.max_count = max(self.max_count, count)
            if m < len(grid) - 1 and golds[m+1][n]:
                coin = golds[m+1][n]
                new_grid = deepcopy(golds)
                new_grid[m+1][n] = 0
                backtrack(m+1, n, count+coin, new_grid)
            if n < len(golds[0]) - 1 and golds[m][n+1]:
                coin = golds[m][n+1]
                new_grid = deepcopy(golds)
                new_grid[m][n+1] = 0
                backtrack(m, n+1, count+coin, new_grid)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    coin = grid[i][j]
                    new_grid = deepcopy(grid)
                    new_grid[i][j] = 0
                    backtrack(i, j, coin, new_grid)

        return self.max_count

    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 回溯的精髓
        # 回溯看起来是多线程的，实际上是单线程的
        # 回溯可以用来记录查找路径
        # 回溯无需额外申请空间，因为都会回溯
        # 还有就是 global ，就应该是 global 的
        if not grid or not grid[0]:
            return 0

        global max_count
        max_count = 0

        def backtrack(m, n, count, golds):
            global max_count
            max_count = max(max_count, count)
            if m and golds[m-1][n]:
                coin = golds[m-1][n]
                golds[m-1][n] = 0
                backtrack(m-1, n, count+coin, golds)
                golds[m - 1][n] = coin
            if n and golds[m][n-1]:
                coin = golds[m][n-1]
                golds[m][n-1] = 0
                backtrack(m, n-1, count+coin, golds)
                golds[m][n - 1] = coin
            if m < len(grid) - 1 and golds[m+1][n]:
                coin = golds[m+1][n]
                golds[m+1][n] = 0
                backtrack(m+1, n, count+coin, golds)
                golds[m + 1][n] = coin
            if n < len(golds[0]) - 1 and golds[m][n+1]:
                coin = golds[m][n+1]
                golds[m][n+1] = 0
                backtrack(m, n+1, count+coin, golds)
                golds[m][n + 1] = coin

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    coin = grid[i][j]
                    grid[i][j] = 0
                    backtrack(i, j, coin, grid)
                    grid[i][j] = coin

        return max_count


if __name__ == '__main__':
    s = Solution()
    print s.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]])
    print s.getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]])
    print s.getMaximumGold([[3,31,23,3,15,20,12],[0,8,11,25,0,31,20],[39,30,16,11,2,29,34],[13,38,35,3,0,14,9]])
    print s.getMaximumGold([[1,0,7,0,0,0],[2,0,6,0,1,0],[3,5,6,7,4,2],[4,3,1,0,2,0],[3,0,5,0,20,0]])
