class TrieNode:
    def __init__(self, data=None):
        self.data = data
        self.child = [None] * 26
        self.word_count = 0
        self.prefix_count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, data):
        if len(data) == 0:
            return
        currentNode = self.root
        for i in range(len(data)):
            char = data[i]
            index = ord(char) - 97

            if currentNode.child[index] is None:
                currentNode.child[index] = TrieNode(char)
            currentNode = currentNode.child[index]
            currentNode.prefix_count += 1

        currentNode.word_count += 1       

    def givePrefixCount(self, key):
        if len(key) == 0:
            return 0
        currentNode = self.root
        for i in range(len(key)):
            char = key[i]
            index = ord(char) - 97
            if currentNode.child[index] is None:
                return 0
            else:
                currentNode = currentNode.child[index]
        return currentNode.prefix_count


if __name__ == "__main__":
    tr = Trie()
    # tr.insert("abc")
    tr.insert("abac")
    tr.insert("abaa")
    tr.insert("abab")
    tr.insert("aabc")

    print(f"prefix count of ab = {tr.givePrefixCount('ab')}")
    print(f"prefix count of aba = {tr.givePrefixCount('aba')}")
    print(f"prefix count of abaa = {tr.givePrefixCount('abaa')}")
    print(f"prefix count of abc = {tr.givePrefixCount('abc')}")
    print(f"prefix count of aa = {tr.givePrefixCount('aa')}")
 
