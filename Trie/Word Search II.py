from typing import List, Optional


class TrieNode:
    def __init__(self, value=None, word_count=0):
        self.value : str = value
        self.children: List[Optional[TrieNode]] = [None] * 26
        self.word_count: int = word_count
        self.hasChild: bool = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = ord(char) - 97
            if curr.children[index] is None:
                curr.children[index] = TrieNode(char)

            curr.hasChild = True
            curr = curr.children[index]
        curr.word_count += 1
class Solution:
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    def inBoundary(self, board, x, y):
        rows, cols = len(board), len(board[0])
        if 0<=x<rows and 0<=y<cols:
            return True
        else:
            return False
    
    def checkWord(self, board, x, y, word, root):
        if not self.inBoundary(board, x, y):
            return

        if root.word_count > 0:
            self.ans.append(word)

        # making board[x][y] visited
        # board[x][y] = chr(ord(board[x][y]) ^ 256)
        original_char = board[x][y]
        board[x][y] = '#'
        
        for del_x, del_y in zip(Solution.dx, Solution.dy):
            new_x = x + del_x
            new_y = y + del_y
            child  = root.children[ord(board[x][y]) - 97]
            if child:
                self.checkWord(board, new_x, new_y, word + original_char, child)

        # making board[x][y] again unvisited
        # board[x][y] = chr(ord(board[x][y]) ^ 256)
        board[x][y] = original_char

        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        trieObj = Trie()

        for word in words:
            trieObj.insert(word)

        self.ans = []
        for x in range(rows):
            for y in range(cols):
                child = trieObj.root.children[ord(board[x][y]) - 97]
                if child:
                    self.checkWord(board, x, y, '', child)
        return self.ans
        
if __name__ == '__main__':
    sol = Solution()
    print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))