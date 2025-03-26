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
        count_area = 1

        for del_x, del_y in zip(self.dir_x, self.dir_y):
            new_x = x + del_x
            new_y = y + del_y

            if self.check_valid(new_x, new_y) and self.grid[new_x][new_y] == 1 and not self.visited[new_x][new_y]:
                count_area += self.dfs(new_x, new_y)
        
        return count_area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.row = len(grid)
        self.col = len(grid[0])
        self.grid = grid
        self.visited = [[False]*self.col for _ in range(self.row)]
        max_area = 0

        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j] == 1 and not self.visited[i][j]:
                    max_area = max(max_area, self.dfs(i, j))

        return max_area


if __name__ == '__main__':
    grid1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    grid2 = [[0,0,0,0,0,0,0,0]]

    sol = Solution()
    print(sol.maxAreaOfIsland(grid1))
    print(sol.maxAreaOfIsland(grid2))