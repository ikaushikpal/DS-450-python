class Solution:
    def __init__(self):
        self.xMoves = [0, 0, 1, -1, 1, 1, -1, -1]
        self.yMoves = [1, -1, 0, 0, 1, -1, 1, -1]
    
    def inBound(self, x, y):
        if 0<=x<self.N and 0<=y<self.M:
            return True
        return False
        
    def search(self, x, y, i, word, seen):
        if i == len(word):
            return True

        if self.grid[x][y] != word[i]:
            return False

        if self.dp[i][x][y] != -1:
            return self.dp[i][x][y]
            
        seen.add((x, y))
        for delX, delY in zip(self.xMoves, self.yMoves):
            newX, newY = x + delX, y + delY
            if not self.inBound(newX, newY):
                continue
            
            if (newX, newY) in seen:
                continue
            
            if self.search(newX, newY, i+1, word, seen):
                self.dp[i][x][y] = 1
                return True
                
        self.dp[i][x][y] = 0
        return False
        
    def searchWord(self, grid, word):
        self.N, self.M = len(grid), len(grid[0])
        self.grid = grid
        self.dp = [[[-1]*self.M for _ in range(self.N)] for _ in range(len(word))]
        ans = []

        for i in range(self.N):
            for j in range(self.M):
                if self.search(i, j, 0, word, set()):
                    ans.append((i, j))
        return ans
    
sol = Solution()
print(sol.searchWord(grid = [['a','b','c'],['d','r','f'],['g','h','i']], word = "abc"))
print(sol.searchWord(grid = [['a','b','a','b'],['a','b','e','b'],['e','b','e','b']], word = "abe"))