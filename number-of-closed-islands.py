# coding=utf-8


class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 先从四周出发，将与外界互通的陆地也改成海洋 0->1
        if not grid or not grid[0]:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not i or i == len(grid) - 1:
                    self.convert_land_to_ocean(i, j, grid)
                elif not j or j == len(grid[0]) - 1:
                    self.convert_land_to_ocean(i, j, grid)

        # 计算孤岛数量，并将其相连陆地翻转
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]:
                    count += 1
                    self.convert_land_to_ocean(i, j, grid)
        return count

    def convert_land_to_ocean(self, i, j, grid):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            if grid[i][j] == 0:
                grid[i][j] = 1
                self.convert_land_to_ocean(i, j+1, grid)
                self.convert_land_to_ocean(i, j-1, grid)
                self.convert_land_to_ocean(i+1, j, grid)
                self.convert_land_to_ocean(i-1, j, grid)


if __name__ == '__main__':
    s = Solution()
    print s.closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]])
    print s.closedIsland([[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]])
    print s.closedIsland([[1,1,1,1,1,1,1],
             [1,0,0,0,0,0,1],
             [1,0,1,1,1,0,1],
             [1,0,1,0,1,0,1],
             [1,0,1,1,1,0,1],
             [1,0,0,0,0,0,1],
             [1,1,1,1,1,1,1]])
