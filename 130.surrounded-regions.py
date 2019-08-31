# coding=utf-8
#
# @lc app=leetcode id=130 lang=python
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (23.59%)
# Likes:    875
# Dislikes: 457
# Total Accepted:    157.2K
# Total Submissions: 664.2K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
# 
# Example:
# 
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# After running your function, the board should be:
# 
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# Explanation:
# 
# Surrounded regions shouldn’t be on the border, which means that any 'O' on
# the border of the board are not flipped to 'X'. Any 'O' that is not on the
# border and it is not connected to an 'O' on the border will be flipped to
# 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
# 
#


class Solution(object):
    def _solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # Time Limit
        # 四边环绕，不是八边环绕
        # 但是环绕可以连起来
        # 不一定是单个环绕
        # 可以是整体环绕
        # 不能单个计算
        # 类似于围棋的环绕

        free = set()
        searched = set()

        # 不能从左边找到右边
        # 然后从右边找到左边
        def freedom(x, y):
            if (x, y) in free:
                return True
            if x == 0 or y == 0 or x == len(board)-1 or y == len(board[0])-1:
                free.add((x, y))
                return True
            if (x, y) in searched:
                return False
            searched.add((x, y))
            if board[x-1][y] == 'O':
                if freedom(x-1, y):
                    free.add((x, y))
                    return True
            if board[x+1][y] == 'O':
                if freedom(x+1, y):
                    free.add((x, y))
                    return True
            if board[x][y-1] == 'O':
                if freedom(x, y-1):
                    free.add((x, y))
                    return True
            if board[x][y+1] == 'O':
                if freedom(x, y+1):
                    free.add((x, y))
                    return True
            searched.remove((x, y))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    if not freedom(i, j):
                        board[i][j] = 'X'

    def __solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # 其实是一道遍历题
        # 应该优先使用广度遍历的
        # 使用深度遍历的话容易栈溢出
        # 所以需要设置很多的条件来结束
        # 不如换个思路
        # 从边上往里找，能访问到的都是活棋
        # 不能访问到的都是死棋
        # 分别从四边开始
        # 也有两个思路，深度遍历，或者广度遍历
        # 或者直接从上往下
        if not board:
            return

        def sign_sharp(x, y):
            if 0 <= x < len(board) and 0 <= y < len(board[0]):
                if board[x][y] == 'O':
                    board[x][y] = '#'
                    sign_sharp(x-1, y)
                    sign_sharp(x+1, y)
                    sign_sharp(x, y-1)
                    sign_sharp(x, y+1)

        for i in range(len(board)):
            if board[i][0] == 'O':
                sign_sharp(i, 0)
            if board[i][len(board[0])-1] == 'O':
                sign_sharp(i, len(board[0])-1)

        for j in range(len(board[0])):
            if board[0][j] == 'O':
                sign_sharp(0, j)
            if board[len(board)-1][j] == 'O':
                sign_sharp(len(board)-1, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # 非递归的深度优先遍历
        # 广度优先遍历，调换一下入栈和出栈的顺序即可
        if not board:
            return

        def sign_sharp(x, y):
            stack = [(x, y)]
            while stack:
                x, y = stack.pop()
                if 0 <= x < len(board) and 0 <= y < len(board[0]):
                    if board[x][y] == 'O':
                        board[x][y] = '#'
                        stack.append((x+1, y))
                        stack.append((x-1, y))
                        stack.append((x, y+1))
                        stack.append((x, y-1))

        for i in range(len(board)):
            if board[i][0] == 'O':
                sign_sharp(i, 0)
            if board[i][len(board[0])-1] == 'O':
                sign_sharp(i, len(board[0])-1)

        for j in range(len(board[0])):
            if board[0][j] == 'O':
                sign_sharp(0, j)
            if board[len(board)-1][j] == 'O':
                sign_sharp(len(board)-1, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'


# if __name__ == '__main__':
#     s = Solution()
#     a = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
#     b = [["O","X","O","O","O","X"],["O","O","X","X","X","O"],["X","X","X","X","X","O"],["O","O","O","O","X","X"],["X","X","O","O","X","O"],["O","O","X","X","X","X"]]
#     s.solve(b)
#     s.solve(a)
#     print a
#     print b
