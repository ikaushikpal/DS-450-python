from typing import List, Optional


class TrieNode:
    def __init__(self, value=None, word_count=0):
        self.value= value
        self.children= [None] * 2
        self.word_count= word_count

class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.ans = []

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = ord(char) - ord('0')
            if curr.children[index] is None:
                curr.children[index] = TrieNode(char)
            curr = curr.children[index]
        curr.word_count += 1

    def search(self, root, word):
        if root is None:
            return
        
        if root.word_count > 0:
            self.ans.append(word + '$')
            return
        
        for child in root.children:
            if child:
                self.search(child, word + child.value + ' ')
        

def uniqueRow(row, col, matrix):
    trieObj = Trie()
    for i in range(row):
        trieObj.insert(''.join(list(map(str, matrix[i]))))
    
    trieObj.search(trieObj.root, '')
    return ''.join(trieObj.ans)


if __name__ == '__main__':
    mat = [[1,1,0,1],[1,0,0,1],[1,1,0,1]]
    print(uniqueRow(3, 4, mat))