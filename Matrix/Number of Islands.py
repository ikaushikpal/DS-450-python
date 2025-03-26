from typing import List


class Solution:
    def __init__(self):
        self.dir_x = [-1, +1, 0, 0]
        self.dir_y = [0, 0, -1, +1]

    def check_valid(self, x ,y ):
        if 0<=x<self.row and 0<=y<self.col:
            return True
        return False

    def dfs(self, x, y):
        self.visited[x][y] = True

        for del_x, del_y in zip(self.dir_x, self.dir_y):
            new_x = x + del_x
            new_y = y + del_y

            if self.check_valid(new_x, new_y) and self.grid[new_x][new_y] == '1' and not self.visited[new_x][new_y]:
                self.dfs(new_x, new_y)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.row = len(grid)
        self.col = len(grid[0])
        self.grid = grid
        self.visited = [[False]*self.col for _ in range(self.row)]
        count_islands = 0

        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j] == '1' and not self.visited[i][j]:
                    count_islands += 1
                    self.dfs(i, j)

        return count_islands


if __name__ == '__main__':
    grid1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    grid2 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    grid3 = [["1","1","1"],["0","1","0"],["1","1","1"]]

    sol = Solution()
    print(sol.numIslands(grid1))
    print(sol.numIslands(grid2))
    print(sol.numIslands(grid3))