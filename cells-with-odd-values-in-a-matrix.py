# coding=utf-8


class Solution(object):
    def _oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        # Brute Force
        source = [[0] * m for _ in range(n)]
        rows = {}
        columns = {}
        for indic in indices:
            rows[indic[0]] = rows.get(indic[0], 0) + 1
            columns[indic[1]] = columns.get(indic[1], 0) + 1

        count = 0

        for i in range(n):
            for j in range(m):
                source[i][j] += rows.get(i, 0)
                source[i][j] += columns.get(j, 0)
                if source[i][j] % 2:
                    count += 1
        return count

    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        # Brute Force
        rows = {}
        columns = {}
        for indic in indices:
            rows[indic[0]] = rows.get(indic[0], 0) + 1
            columns[indic[1]] = columns.get(indic[1], 0) + 1

        count = 0

        for i in range(n):
            for j in range(m):
                if (rows.get(i, 0) + columns.get(j, 0)) % 2:
                    count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    print s.oddCells(2,3, [[0,1],[1,1]])
    print s.oddCells(2,2, [[1,1],[0,0]])
