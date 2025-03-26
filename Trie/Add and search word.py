class TrieNode:
    def __init__(self, data=None):
        self.data = data
        self.child = [None] * 26
        self.word_count = 0


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, data):
        if len(data) == 0:
            return
        currentNode = self.root
        for i in range(len(data)):
            char = data[i]
            index = ord(char) - 97

            if currentNode.child[index] is None:
                currentNode.child[index] = TrieNode(char)
            currentNode = currentNode.child[index]
        currentNode.word_count += 1
    
    def search(self, word):
        if len(word) == 0:
            return False
        res = self.__searchUtil(word, self.root, 0)
        return res

    def __searchUtil(self, word, currentNode, depth):
        if depth >= len(word):
            if currentNode is None:
                return False
            else:
               return True if currentNode.word_count > 0 else False 

        while depth < len(word):
            if word[depth] == '.':
                break
            index = ord(word[depth]) - 97
            curr = currentNode.child[index]

            if curr is None:
                return False

            if word[depth] != '.':
                if depth == len(word) - 1:
                    return True if curr.word_count > 0 else False
                else:
                    currentNode = curr
            depth += 1

        for child in currentNode.child:
            if child:
                res = self.__searchUtil(word, child, depth + 1)
                if res == True:
                    return True    
        return False

if __name__ == "__main__":
    tr = WordDictionary()
    tr.addWord("abc")
    tr.addWord("army")
    tr.addWord("ascii")
    tr.addWord("apple")
    tr.addWord("api")
    tr.addWord("ai")
    tr.addWord("xxx")

    print(tr.search('.'))