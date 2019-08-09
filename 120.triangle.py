#
# @lc app=leetcode id=120 lang=python
#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (38.36%)
# Likes:    1235
# Dislikes: 139
# Total Accepted:    192.6K
# Total Submissions: 478.8K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you
# may move to adjacent numbers on the row below.
# 
# For example, given the following triangle
# 
# 
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
# 
# 
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# 
# Note:
# 
# Bonus point if you are able to do this using only O(n) extra space, where n
# is the total number of rows in the triangle.
# 
#
class Solution(object):
    def _minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # Not Dynamic Programming
        result = []
        for row in triangle:
            if not result:
                result.append(row)
                continue
            last_row = result[-1]
            new_row = []
            for index,value in enumerate(row):
                small_row = []
                if index != 0:
                    small_row.append(value+last_row[index-1])
                if index != len(row) - 1:
                    small_row.append(value+last_row[index])
                new_row.append(min(small_row))
            result.append(new_row)
        return min(result[-1])

    def __minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # Some Dynamic
        dp = [[float("inf")]*(len(triangle)+1) for _ in range(len(triangle)+1)]
        dp[0][0] = 0
        for i in range(len(triangle)+1):
            for j in range(i):
                dp[i][j] = min(triangle[i-1][j] + dp[i-1][j-1], triangle[i-1][j] + dp[i-1][j])
        return min(dp[-1])

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [[float("inf")]*(len(triangle)) for _ in range(len(triangle))]
        for i in range(len(triangle)):
            for j in range(i+1):
                if i > 0:
                    dp[i][j] = min(triangle[i][j] + dp[i-1][j-1], triangle[i][j] + dp[i-1][j])
                else:
                    dp[i][j] = triangle[i][j]
        return min(dp[-1])

# if __name__ == "__main__":
#     s = Solution()
#     print s.minimumTotal([[2],[3,4],[5,6,7],[4,1,8,3]])
