# Design a map that allows you to do the following:

# Maps a string key to a given value.
# Returns the sum of the values that have a key with a prefix equal to a given string.
# Implement the MapSum class:

# MapSum() Initializes the MapSum object.
# void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
# int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.
 

# Example 1:

# Input
# ["MapSum", "insert", "sum", "insert", "sum"]
# [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
# Output
# [null, null, 3, null, 5]

# Explanation
# MapSum mapSum = new MapSum();
# mapSum.insert("apple", 3);  
# mapSum.sum("ap");           // return 3 (apple = 3)
# mapSum.insert("app", 2);    
# mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)


from typing import List, Optional


class TrieNode:
    def __init__(self, value=None):
        self.value : str = value
        self.children: List[Optional[TrieNode]] = [None] * 26
        self.val: int = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for char in key:
            index = ord(char) - 97
            if curr.children[index] is None:
                curr.children[index] = TrieNode(char)
            curr = curr.children[index]

        curr.val  = val

    def search(self, root: Optional[TrieNode]) -> int:
        if root is None:
            return 0

        ans = root.val
        for child in root.children:
            ans += self.search(child)

        return ans

        
class MapSum:

    def __init__(self):
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.trie.insert(key, val)

    def sum(self, prefix: str) -> int:
        curr = self.trie.root
        for i, char in enumerate(prefix):
            index = ord(char) - 97
            child = curr.children[index]
            if not child:
                return 0
            curr = child
        
        return self.trie.search(curr)


if __name__ == '__main__':
    sol = MapSum()
    print(sol.insert("apple", 3)) 
    print(sol.sum('ap'))
    print(sol.insert("app", 2)) 
    print(sol.sum('ap'))