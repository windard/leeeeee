# coding=utf-8


class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        length = 8
        queens = set(map(tuple, queens))

        attached = []
        k = king
        # 往右
        for i in range(k[0]+1, length):
            if (i, k[1]) in queens:
                attached.append([i, k[1]])
                break
        # 往左
        for i in range(k[0]-1, -1, -1):
            if (i, k[1]) in queens:
                attached.append([i, k[1]])
                break
        # 往上
        for i in range(k[1]+1, length):
            if (k[0], i) in queens:
                attached.append([k[0], i])
                break
        # 往下
        for i in range(k[1]-1, -1, -1):
            if (k[0], i) in queens:
                attached.append([k[0], i])
                break
        # 左上
        for i in range(length):
            if k[0] + i < length and k[1] + i < length:
                if (k[0]+i, k[1]+i) in queens:
                    attached.append([k[0]+i, k[1]+i])
                    break
            else:
                break
        # 左下
        for i in range(length):
            if k[0] - i >= 0 and k[1] - i >= 0:
                if (k[0]-i, k[1]-i) in queens:
                    attached.append([k[0]-i, k[1]-i])
                    break
            else:
                break
        # 右上
        for i in range(length):
            if k[0] + i < length and k[1] - i >= 0:
                if (k[0]+i, k[1]-i) in queens:
                    attached.append([k[0]+i, k[1]-i])
                    break
            else:
                break
        # 右下
        for i in range(length):
            if k[0] - i >= 0 and k[1] + i < length:
                if (k[0]-i, k[1]+i) in queens:
                    attached.append([k[0]-i, k[1]+i])
                    break
            else:
                break

        return attached


if __name__ == '__main__':
    s = Solution()
    print s.queensAttacktheKing([[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], [0,0])
    print s.queensAttacktheKing([[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], [3,3])
    print s.queensAttacktheKing([[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], [3,4])
