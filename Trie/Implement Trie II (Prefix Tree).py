# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string wordinto the trie.
# int countWordsEqualTo(String word) Returns the number of instances of the string word in the trie.
# int countWordsStartingWith(String prefix)Returns the number of strings in the trie that have the string prefix as a prefix.
# void erase(String word) Erases the string wordfrom the trie.

# Example 1:
# Input
# ["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsStartingWith"]
# [[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"], ["app"], ["apple"], ["app"]]
# Output
# [null, null, null, 2, 2, null, 1, 1, null, 0]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");               // Inserts "apple".
# trie.insert("apple");               // Inserts another "apple".
# trie.countWordsEqualTo("apple");    // There are two instances of "apple" so return 2.
# trie.countWordsStartingWith("app"); // "app" is a prefix of "apple" so return 2.
# trie.erase("apple");                // Erases one "apple".
# trie.countWordsEqualTo("apple");    // Now there is only one instance of "apple" so return 1.
# trie.countWordsStartingWith("app"); // return 1
# trie.erase("apple");                // Erases "apple". Now the trie is empty.
# trie.countWordsStartingWith("app"); // return 0
from typing import Optional


class TrieNode:
    def __init__(self, value=None, word_count=0, prefix_count=0):
        self.value = value
        self.children = [None] * 26
        self.word_count = word_count
        self.prefix_count = prefix_count

    def __str__(self) -> str:
        return f"{self.value}-{self.word_count}-{self.prefix_count}"

    def __repr__(self) -> str:
        return self.__str__()
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = ord(char) - 97
            if curr.children[index] is None:
                curr.children[index] = TrieNode(char)

            curr.prefix_count += 1
            curr = curr.children[index]
        curr.word_count += 1

    def countWordsEqualTo(self, word: str) -> bool: 
        curr = self.root
        for char in word:
            index = ord(char) - 97
            if curr.children[index] is None:
                return 0
            curr = curr.children[index]

        return curr.word_count

    def countWordsStartingWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            index = ord(char) - 97
            if curr.children[index] is None:
                return 0
            curr = curr.children[index]
        return curr.prefix_count
    
    def erase_util(self, root: Optional[TrieNode], word: str):
        if root is None:
            return None

        if len(word) == 0:
            root.word_count -= 0

            if root.word_count > 0:
                return root

            if root.prefix_count > 0:
                return root
            else:
                del root
                return None
        
        index = ord(word[0]) - 97
        if not root.children[index]:
            return root
        else:
            child = self.erase_util(root.children[index], word[1:])
            root.prefix_count -= 1
            root.children[index] = child
            return root
        

    def erase(self, word: str) -> None:
        self.root = self.erase_util(self.root, word)
        self.root.prefix_count -= 1


if __name__ == '__main__':
    trie = Trie()
    print(trie.insert("apple"))               # Inserts "apple".
    print(trie.insert("apple"))               # Inserts another "apple".
    print(trie.countWordsEqualTo("apple"))    # There are two instances of "apple" so return 2.
    print(trie.countWordsStartingWith("app")) # "app" is a prefix of "apple" so return 2.
    print(trie.erase("apple"))                # Erases one "apple".
    print(trie.countWordsEqualTo("apple"))    # Now there is only one instance of "apple" so 
    print(trie.countWordsStartingWith("app")) # return 1
    print(trie.erase("apple"))                # Erases "apple". Now the trie is empty.
    print(trie.countWordsStartingWith("app")) # return 0