# Given an array of strings arr[]. You have to find the longest string which is lexicographically smallest and also all of its prefix strings are already present in the array.


# Example 1:
# Input: ab a abc abd
# Output: abc
# Explanation: We can see that length of the longest 
# string is 3. And there are two string "abc" and "abd"
# of length 3. But for string "abc" , all of its prefix
# "a" "ab" "abc" are present in the array. So the
# output is "abc".


# Example 2:
# Input: ab a aa abd abc abda abdd abde abdab
# Output: abdab
# Explanation: We can see that each string is fulfilling
# the condition. For each string, all of its prefix 
# are present in the array.And "abdab" is the longest
# string among them. So the ouput is "abdab".


from string import ascii_lowercase


class TrieNode:
    def __init__(self, char):
        self.char = char
        self.hasOcc = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode('')
    
    def insert(self, string):
        curr = self.root
        
        for char in string:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        curr.hasOcc = True
    
    def searchUtil(self, currNode, currString):
        if len(currString) > len(self.ans):
            self.ans = currString
            
        for char in ascii_lowercase:
            child = currNode.children.get(char, None)
            
            if char not in currNode.children:
                continue
            
            if not child.hasOcc:
                continue
            
            self.searchUtil(child, currString + char)
        
    def search(self):
        self.ans = ''
        self.searchUtil(self.root, '')
        return self.ans


class Solution():
    def longestString(self, arr, n):
        t = Trie()
        for string in arr:
            t.insert(string)
        
        return t.search()
# Time Complexity: O(N * L)
# Space Complexity: O(N * L)


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestString(['ab', 'a', 'abc', 'abd'], 4))
    print(sol.longestString(['ab', 'a', 'aa', 'abd', 'abc', 'abda', 'abdd', 'abde', 'abdab'], 9))

