# Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

# A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

 

# Example 1:

# Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
# "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
# Example 2:

# Input: words = ["cat","dog","catdog"]
# Output: ["catdog"]



# from typing import List, Optional


# class TrieNode:
#     def __init__(self, value=None, word_count=0):
#         self.value : str = value
#         self.children: List[Optional[TrieNode]] = [None] * 26
#         self.word_count: int = word_count


# class Trie:

#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word: str) -> None:
#         curr = self.root
#         for char in word:
#             index = ord(char) - 97
#             if curr.children[index] is None:
#                 curr.children[index] = TrieNode(char)

#             curr = curr.children[index]
#         curr.word_count += 1

#     def search(self, root: Optional[TrieNode], s: str) -> str:
#         if root is None:
#             return False
        
#         if len(s) == 0:
#             return True
#         else:
#             for i, char in enumerate(s):
#                 index = ord(char) - 97
#                 child = root.children[index]
#                 if child:
#                     if child.word_count > 0:
#                         if self.search(self.root, s[i+1:]):
#                             return True
#                     root = child
#                 else:
#                     return False
#             return False

# class Solution:
#     def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
#         words = sorted(words, key=len)
#         trieObj = Trie()
#         ans = []
#         for word in words:
#             if trieObj.search(trieObj.root, word):
#                 ans.append(word)
#             trieObj.insert(word)
#         return ans

from typing import List, Optional


class TrieNode:
    def __init__(self, value=None):
        self.value : str = value
        self.children: List[Optional[TrieNode]] = [None] * 26
        self.word_count: int = 0

            
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = ord(char) - 97
            if curr.children[index] is None:
                curr.children[index] = TrieNode(char)
                
            curr = curr.children[index]
        curr.word_count += 1

    
    def search(self, root: Optional[TrieNode], s: str, count) -> str:
        for i, char in enumerate(s):
            index = ord(char) - 97  
            child = root.children[index]
            
            if not child:
                return False
            
            if child.word_count > 0:
                if i == len(s)-1:
                    return count >= 1
                
                if self.search(self.root, s[i+1:], count + 1):
                    return True
    
            root = child
        return False
            
        
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = sorted(words, key=len)
        trieObj = Trie()
        ans = []
        
        for word in words:
            if len(word) == 0:
                continue
            trieObj.insert(word)
            
        for word in words:
            if len(word) == 0:
                continue
            if trieObj.search(trieObj.root, word, 0):
                ans.append(word)
            
        return ans
# More optimized


if __name__ == '__main__':
    sol = Solution()
    print(sol.findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
    print(sol.findAllConcatenatedWordsInADict(["cat","dog","catdog"]))