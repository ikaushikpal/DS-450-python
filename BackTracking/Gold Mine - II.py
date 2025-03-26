class Solution:
    def getMaxGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        self.res = 0

        for i in range(m):
            for j in range(n):
                self.dfs(grid, visited, i, j, 0)
        return self.res
    
    def dfs(self, grid, visited, i, j, gold):
        if (i < 0 or i >= len(grid)) or (j < 0 or j >= len(grid[0])) or grid[i][j] == 0 or visited[i][j]:
            return

        gold += grid[i][j]
        visited[i][j] = True
        self.res = max(self.res, gold)

        self.dfs(grid, visited, i - 1, j, gold) # up
        self.dfs(grid, visited, i, j + 1, gold) # right
        self.dfs(grid, visited, i + 1, j, gold) # down
        self.dfs(grid, visited, i, j - 1, gold) # left


if __name__ == '__main__':
    sol = Solution()
    grid = [[1,0,7],
            [2,0,6],
            [3,4,5],
            [0,3,0],
            [9,0,20]]
    print(sol.getMaxGold(grid))