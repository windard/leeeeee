# coding=utf-8


class Solution(object):
    def _maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # BF 暴力
        # Double Point
        # 都不好做，用 dp 吧
        # Memory Error
        max_count = -float("inf")
        dp = [[0] * len(arr) for _ in range(len(arr))]
        for i in range(len(arr)):
            dp[i][i] = (arr[i], arr[i])
            max_count = max(max_count, dp[i][i][0])
            for j in range(i):
                min_index = dp[i-1][j][1]
                count = dp[i-1][j][0]
                if i-1 != j:
                    count = dp[i-1][j][0] + min_index
                if arr[i] < min_index:
                    min_index = arr[i]
                dp[i][j] = (count + arr[i] - min_index, min_index)
                max_count = max(max_count, dp[i][j][0])
        return max_count

    def __maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # 用贪心
        # 或者用单行 dp
        # Time Limit
        # O(n^2)
        dp = [0] * len(arr)
        max_count = -float("inf")
        for i in range(len(arr)):
            dp[i] = (arr[i], arr[i])
            max_count = max(max_count, dp[i][0])
            for j in range(i):
                min_index = dp[j][1]
                count = dp[j][0]
                if i-1 != j:
                    count = dp[j][0] + min_index
                if arr[i] < min_index:
                    min_index = arr[i]
                dp[j] = (count + arr[i] - min_index, min_index)
                max_count = max(max_count, dp[j][0])
        return max_count

    def ___maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # 真的要上贪心了。
        # O(n)
        # 跟之前的求最大值一样的思路
        # Total Wrong
        last_value = min_value = -float("inf")
        max_value = -float("inf")
        for v in arr:
            if last_value >= 0:
                count = last_value + min_value
                new_min_value = min(v, min_value)
                new_last_value = count + v - new_min_value
                max_value = max(new_last_value, max_value)
                if v and new_last_value + new_min_value < v:
                    last_value = 0
                    min_value = v
                else:
                    last_value = new_last_value
                    min_value = new_min_value
            else:
                last_value = 0
                min_value = v
                max_value = max(v, max_value)
        return max_value

    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # copy one
        # should same with @53
        # unbelievable
        l = r = ans = -float('inf')
        for i in range(len(arr)):
            l = max(l+arr[i], r)
            r = max(r+arr[i], arr[i])
            ans = max(ans, max(l, r))
        return ans


if __name__ == '__main__':
    s = Solution()
    print s.maximumSum([-8,7,-12,-1,0,11,-2,-3,4,-13,2,3,-6])  # 17
    print s.maximumSum([11,-10,-11,8,7,-6,9,4,11,6,5,0])  # 50
    print s.maximumSum([1,-4,-5,-2,5,0,-1,2])             # 7
    print s.maximumSum([1,-2,0,3])                        # 4
    print s.maximumSum([1,-2,-2,3])                       # 3
    print s.maximumSum([-1,-1,-1,-1])                     # -1
