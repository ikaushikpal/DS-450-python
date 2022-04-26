class TrieNode:
    def __init__(self, value=None, word_count=0):
        self.value = value
        self.children = [None] * 26
        self.word_count = word_count


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = ord(char) - 97
            if curr.children[index] is None:
                curr.children[index] = TrieNode(char)
            curr = curr.children[index]
        curr.word_count += 1

    def search_util(self, root, word):
        if root is None:
            return False

        for i, char in enumerate(word):
            index = ord(char) - 97
            if char != '.':
                if root.children[index] is None:
                    return False
                root = root.children[index]
            else:
                for child in root.children:
                    if child:
                        if self.search_util(child, word[i+1:]):
                            return True
                return False

        if root.word_count > 0:
            return True
        else:
            return False

    def search(self, word: str) -> bool: 
        return self.search_util(self.root, word)

        
if __name__ == '__main__':
    wd = WordDictionary()
    print(wd.addWord("bad"))
    print(wd.addWord("dad"))
    print(wd.addWord("mad"))
    print(wd.search("pad"))
    print(wd.search("bad"))
    print(wd.search(".ad"))
    print(wd.search("b.."))