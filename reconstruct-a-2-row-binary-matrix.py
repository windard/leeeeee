# coding=utf-8


class Solution(object):
    def _reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        if upper + lower != sum(colsum):
            return []
        # 只求一个答案的话，用回溯
        # Time Limit
        result = []
        answer = []
        global flag
        flag = False

        def backtrack(u, l, index):
            global flag
            if flag:
                return
            count = 0
            while index < len(colsum) and colsum[index] in [0,2]:
                if colsum[index] == 0:
                    result.append([0,0])
                    count += 1
                elif colsum[index] == 2:
                    result.append([1,1])
                    u -= 1
                    l -= 1
                    count += 1
                index += 1
            if index >= len(colsum):
                if u == 0 and l == 0:
                    flag = True
                    answer.append([c[0] for c in result])
                    answer.append([c[1] for c in result])
                    return
            else:
                if l > 0:
                    result.append([0, 1])
                    backtrack(u, l-1, index+1)
                    result.pop()
                if not flag and u > 0:
                    result.append([1, 0])
                    backtrack(u-1, l, index+1)
                    result.pop()
            for i in range(count):
                result.pop()
        backtrack(upper, lower, 0)
        return answer

    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        # 只求最后结果的话，可以用dp
        # 但是如果还需要过程
        # 其实也没有那么复杂
        # 就先把 0 和 2 处理完之后
        # 就按照 1 把 upper 和 lower 都填上即可
        if upper + lower != sum(colsum):
            return []

        result = [[0]*len(colsum) for _ in range(2)]
        for index, col in enumerate(colsum):
            if col == 2:
                result[0][index] = 1
                result[1][index] = 1
                upper -= 1
                lower -= 1

        for index, col in enumerate(colsum):
            if col == 1:
                if upper:
                    result[0][index] = 1
                    upper -= 1
                elif lower:
                    result[1][index] = 1
                    lower -= 1
                else:
                    return []
        return result if upper == 0 == lower else []


if __name__ == '__main__':
    s = Solution()
    print s.reconstructMatrix(2,1, [1,1,1])
    print s.reconstructMatrix(2,3, [2,2,1,1])
    print s.reconstructMatrix(5,5, [2,1,2,0,1,0,1,2,0,1])
    print s.reconstructMatrix(4,5, [2,2,2,1,1,1])
    print s.reconstructMatrix(99, 102, [2,1,1,1,1,2,0,2,2,2,0,1,0,0,2,1,1,1,2,2,1,2,1,1,1,1,2,0,1,2,1,1,2,2,1,0,2,0,1,0,0,1,0,1,0,1,2,1,0,1,1,0,2,1,1,0,1,0,1,0,1,0,1,1,2,1,1,2,2,1,1,2,2,2,0,1,1,0,0,1,1,1,1,0,0,2,1,1,1,2,1,1,2,1,0,1,2,0,1,1,2,2,2,1,1,2,2,2,0,2,1,2,2,1,0,1,1,1,1,0,1,1,1,2,0,1,0,2,1,2,1,1,2,1,1,2,1,1,1,1,0,2,0,1,0,0,1,1,1,0,1,1,0,0,2,0,0,1,1,1,0,0,2,2,1,1,1,1,1,1,0,2,1,1,0,1,2,1,2,0,1,0,1,1,1,0,1,1,0,0,0,0,1,2,2,2,1,1,0,2])
