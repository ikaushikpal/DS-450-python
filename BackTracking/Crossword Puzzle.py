from typing import List


class Solution:
    EMPTY_CELL = '-'
    BLOCKED_CELL = '.'

    def crosswordPuzzle(self, board:List[List[str]], words:List[str]) -> None:
        """
        Do not return anything, modify board in-place instead and print solutions if exist
        rtype: None
        """
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.words = words
        self.countSolution = 0
        
        self.crosswordPuzzleHelper(0)

        if self.countSolution == 0:
            print("No solution exists")
        
    def crosswordPuzzleHelper(self, wordIndex:int) -> None:
        '''
        Helper function to solve the crossword puzzle
        :rtype: None
        '''
        if wordIndex == len(self.words):
            # we found one solution
            self.countSolution += 1
            self.printBoard()
            return

        word = self.words[wordIndex]

        for i in range(self.rows):
            for j in range(self.cols):
                # checking if cell is empty or not
                # or current word's first character is already placed in that cell
                if self.board[i][j] == Solution.EMPTY_CELL or self.board[i][j] == word[0]:
                    if self.canPlaceWordHorizontally(word, i, j):
                        visited = self.placeWordHorizontally(word, i, j)
                        self.crosswordPuzzleHelper(wordIndex+1)
                        self.removeWordHorizontally(visited, i, j)

                    if self.canPlaceWordVertically(word, i, j):
                        visited = self.placeWordVertically(word, i, j)
                        self.crosswordPuzzleHelper(wordIndex+1)
                        self.removeWordVertically(visited, i, j)

    def printBoard(self):
        print(f'Solution {self.countSolution}\n')

        for row in self.board:
            print(*row)

        print('=' * 50)
    
    def canPlaceWordHorizontally(self, word:str, x:int, y:int) -> bool:
        '''
        Check if we can place the word horizontally
        :rtype: bool
        '''
        n = len(word)
        # first check if this cell (x, y) is staring cell of the word or not
        # to check that need to check if (x, y-1) cell is empty or not
        if y-1 >= 0 and self.board[x][y-1] != Solution.BLOCKED_CELL:
            return False
        
        # Now need to check if we there is space to place word or not
        # to check that we need to check if (x, y+n) cell is empty or not
        # we are looking for prefect fit, no cell extra or no cell less
        if  y+n < self.cols and self.board[x][y+n] != Solution.BLOCKED_CELL:
            return False

        # overflowing check
        # if y+n > self.cols:
        #     return False

        # Now need to check throw that there is empty cell in between or not
        # and also need to check if any character is already placed in that cell
        # and that character should not be same as any character in current word
        for i in range(n):
            newY = y + i

            if newY >= self.cols:
                return False

            if self.board[x][newY] != Solution.EMPTY_CELL and self.board[x][newY] != word[i]:
                return False
        
        return True

    def placeWordHorizontally(self, word:str, x:int, y:int) -> List[bool]:
        '''
        Place the word horizontally directly in the board
        :rtype: List[bool]
        '''

        n = len(word)
        # the job of visited is to keep track of which cell is visited ny current word
        # meaning there can other character/(s) already placed 
        # To separate current word's character from other words's character(s) 
        # if visited[i] == True, that means that current word's character is placed in i'th cell
        # else other word(s) character is placed in i'th cell
        visited = [False] * n

        for i in range(n):
            newY = y + i
            character = word[i]

            if self.board[x][newY] == Solution.EMPTY_CELL:
                # we are placing current word's character in board[x][newY] cell
                visited[i] = True
                self.board[x][newY] = character

        return visited

    def removeWordHorizontally(self, visited:List[bool], x:int, y:int) -> None:
        '''
        Remove the current word's characters horizontally from the board
        :rtype: None
        '''

        n = len(visited)
        for i in range(n):
            newY = y + i
            # only removing which are placed by current word
            if visited[i]:
                self.board[x][newY] = Solution.EMPTY_CELL

    def canPlaceWordVertically(self, word:str, x:int, y:int) -> bool:
        '''
        Check if we can place the word Vertically
        :rtype: bool
        '''
        n = len(word)
        # first check if this cell (x, y) is staring cell of the word or not
        # to check that need to check if (x-1, y) cell is empty or not
        if x-1 >= 0 and self.board[x-1][y] != Solution.BLOCKED_CELL:
            return False
        # Now need to check if we there is space to place word or not
        # to check that we need to check if (x+n, y) cell is empty or not or even exist
        # we are looking for prefect fit, no cell extra or no cell less
        if  x+n < self.rows and self.board[x+n][y] != Solution.BLOCKED_CELL:
            return False

        # overflowing check
        # if x+n > self.rows:
        #     return False

        # Now need to check throw that there is empty cell in between or not
        # and also need to check if any character is already placed in that cell
        # and that character should not be same as any character in current word
        for i in range(n):
            newX = x + i
            if newX >= self.rows:
                return False

            if self.board[newX][y] != Solution.EMPTY_CELL and self.board[newX][y] != word[i]:
                return False
        
        return True

    
    def placeWordVertically(self, word:str, x:int, y:int) -> List[bool]:
        '''
        Place the word Vertically directly in the board
        :rtype: List[bool]
        '''

        n = len(word)
        # the job of visited is to keep track of which cell is visited ny current word
        # meaning there can other character/(s) already placed 
        # To separate current word's character from other words's character(s) 
        # if visited[i] == True, that means that current word's character is placed in i'th cell
        # else other word(s) character is placed in i'th cell
        visited = [False] * n

        for i in range(n):
            newX = x + i
            character = word[i]

            if self.board[newX][y] == Solution.EMPTY_CELL:
                # we are placing current word's character in board[newX][y] cell
                visited[i] = True
                self.board[newX][y] = character

        return visited

    def removeWordVertically(self, visited:List[bool], x:int, y:int) -> None:
        '''
        Remove the current word's characters Vertically from the board
        :rtype: None
        '''

        n = len(visited)
        for i in range(n):
            newX = x + i
            # only removing which are placed by current word
            if visited[i]:
                self.board[newX][y] = Solution.EMPTY_CELL
    

if __name__ == '__main__':
    # . = Empty Cell
    # + = Blocked Cell
    
    sol = Solution()
    board = [['.', '-', '.'],
             ['-', '-', '-'],
             ['.', '-', '.']]
    words = ['ant', 'and']

    sol.crosswordPuzzle(board, words)

    board = [['.','-','.','.','.','.','.','.','.','.'],
            ['.','-','.','.','.','.','.','.','.','.'],
            ['.','-','.','.','.','.','.','.','.','.'],
            ['.','-','-','-','-','-','.','.','.','.'],
            ['.','-','.','.','.','-','.','.','.','.'],
            ['.','-','.','.','.','-','.','.','.','.'],
            ['.','.','.','.','.','-','.','.','.','.'],
            ['.','.','-','-','-','-','-','-','.','.'],
            ['.','.','.','.','.','-','.','.','.','.'],
            ['.','.','.','.','.','-','.','.','.','.']]

    words = ['LONDON', 'DELHI', 'ICELAND', 'ANKARA']

    sol.crosswordPuzzle(board, words)
