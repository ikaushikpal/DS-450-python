# Given a list of contacts contact[] of length n where each contact is a string which exist in a phone directory and a query string s. The task is to implement a search query for the phone directory. Run a search query for each prefix p of the query string s (i.e. from  index 1 to |s|) that prints all the distinct contacts which have the same prefix as p in lexicographical increasing order. Please refer the explanation part for better understanding.
# Note: If there is no match between query and contacts, print "0".

# Example 1:

# Input: 
# n = 3
# contact[] = {"geeikistest", "geeksforgeeks", 
# "geeksfortest"}
# s = "geeips"
# Output:
# geeikistest geeksforgeeks geeksfortest
# geeikistest geeksforgeeks geeksfortest
# geeikistest geeksforgeeks geeksfortest
# geeikistest
# 0
# 0
# Explaination: By running the search query on 
# contact list for "g" we get: "geeikistest", 
# "geeksforgeeks" and "geeksfortest".
# By running the search query on contact list 
# for "ge" we get: "geeikistest" "geeksforgeeks"
# and "geeksfortest".
# By running the search query on contact list 
# for "gee" we get: "geeikistest" "geeksforgeeks"
# and "geeksfortest".
# By running the search query on contact list 
# for "geei" we get: "geeikistest".
# No results found for "geeip", so print "0". 
# No results found for "geeips", so print "0".


from typing import List, Optional


class TrieNode:
    def __init__(self, value=None, word_count=0):
        self.value= value
        self.children= [None] * 26
        self.word_count= word_count
        self.hasChild= False

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

    def search(self, root: Optional[TrieNode], searchWord: str, word: str) -> str:
        if root is None:
            return

        if self.remaining == 0:
            return
        
        if len(searchWord) > 0:
            child = root.children[ord(searchWord[0]) - 97]
            if child:
                self.search(child,
                            searchWord[1:],
                            word + child.value)
        else:
            if root.word_count > 0:
                self.res.append(word)
                self.remaining -= 1

            for child in root.children:
                if child and self.remaining > 0:
                    self.search(child, '', word + child.value)
        

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trieObj = Trie()
        for word in products:
            trieObj.insert(word)

        res = []
        for i in range(1, len(searchWord) + 1):
            trieObj.res = []
            trieObj.remaining = 100
            trieObj.search(trieObj.root, searchWord[:i], '')
            
            if len(trieObj.res) > 0:
                res.append(trieObj.res)
            else:
                res.append(['0'])

        return res
        
    def displayContacts(self, n, contact, s):
        return self.suggestedProducts(contact, s)


if __name__ =='__main__':
    sol = Solution()
    print(sol.displayContacts(3, ["geeikistest", "geeksforgeeks", 
"geeksfortest"], "geeips"))
