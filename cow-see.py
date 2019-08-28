# coding=utf-8

# http://poj.org/problem?id=3250
# 牛头向右，每头牛能看到多少牛


class Solution(object):

    def cow_see(self, cows):
        # 暴力
        # O(n^2)
        result = [0] * len(cows)
        for i in range(len(cows)-1):
            for j in range(i+1, len(cows)):
                if cows[j] <= cows[i]:
                    result[i] += 1
                else:
                    break
        return result

    def cow_see_stack(self, cows):
        # 单调栈
        # O(n)
        stack = []
        result = [0] * len(cows)
        cows.append(float("inf"))
        for i, c in enumerate(cows):
            while stack and cows[stack[-1]] < c:
                top = stack.pop()
                result[top] = i - top - 1
            stack.append(i)
        return result

    def cow_see_dp(self, cows):
        # 动态规划
        # O(n)
        # 动态规划做不了。。。
        result = [0] * len(cows)
        for i in range(len(cows)-2, -1, -1):
            if cows[i] >= cows[i+1]:
                result[i] = result[i+1]+1
        return result


if __name__ == '__main__':
    s = Solution()
    print s.cow_see([5,2,4,2,6,1])
    # print s.cow_see_dp([5,2,4,2,6,1])
    print s.cow_see_stack([5,2,4,2,6,1])
