class Solution:

    def __init__(self, board):
        self.N = len(board)
        self.result = []
        self.board = board


    def availablePositions(self, x, y, prevPosition):
        available = []
        
        if prevPosition != 'U' and x+1 < self.N:
            available.append((x+1, y, 'D'))

        if prevPosition != 'R' and y-1 >= 0:
            available.append((x, y-1, 'L'))
        
        if prevPosition != 'L' and y+1 < self.N:
            available.append((x, y+1, 'R'))
        
        if prevPosition != 'D' and x-1 >= 0:
            available.append((x-1, y, 'U'))
            
        return available


    def ratMazeUtil(self, x, y, currentString):
        if  len(currentString):
            prevPosition = currentString[-1]
        else:
            prevPosition = ''

        if x == self.N-1 and y == self.N-1:
            self.result.append(currentString)
            return
        
        if x >= self.N or y >= self.N:
            return
        self.visited[x][y] =True
        available = self.availablePositions(x, y, prevPosition)

        for x_, y_, move in available:
            if self.board[x_][y_] == 1 and self.visited[x_][y_] == False:
                self.ratMazeUtil(x_, y_,currentString + move)

        self.visited[x][y] = False


    def ratMaze(self):
        if self.board[0][0] == 0:
            return []

        self.visited = [[False] * self.N for x in range(self.N)]
        self.result = []
        self.ratMazeUtil(0, 0, '')
        
        return self.result


if __name__ == '__main__':
    board =[[1, 0, 0, 0],
            [1, 1, 0, 1],
            [1, 1, 0, 0],
            [0, 1, 1, 1]]
    
    sol = Solution(board)
    print(sol.ratMaze())
