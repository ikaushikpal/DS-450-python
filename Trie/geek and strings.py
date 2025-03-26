# Geek has a list Li containing (not necessarily distinct) N words and Q queries. Each query consists of a string x. For each query, find how many strings in the List Li has the string x as its prefix. 


# Example 1:
# Input: 
# N = 5, Q = 5
# li[] = {'abracadabra', 'geeksforgeeks', 
#       'abracadabra', 'geeks', 'geeksthrill'}
# query[] = {'abr', 'geeks', 'geeksforgeeks', 
#          'ge', 'gar'}
# Output: 2 3 1 3 0

# Explaination: 
# Query 1: The string 'abr' is prefix of 
# two 'abracadabra'. 
# Query 2: The string 'geeks' is prefix of three 
# strings 'geeksforgeeks', 'geeks' and 'geeksthrill'. 
# Query 3: The string 'geeksforgeeks' is prefix 
# of itself present in li. 
# Query 4: The string 'ge' also is prefix of three 
# strings 'geeksforgeeeks', 'geeks', 'geeksthrill'. 
# Query 5: The string 'gar' is not a prefix of any 
# string in li.


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.occCount = 0
    

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, string):
        curr = self.root
        for char in string:
            index = ord(char) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index] 
            curr.occCount += 1
    
    def search(self, string):
        curr = self.root
        for char in string:
            index = ord(char) - ord('a')
            if not curr.children[index]:
                return 0
            curr = curr.children[index] 
        return curr.occCount
        
        
class Solution:
    def prefixCount(self, N, Q, li, query):
        t = Trie()
        for string in li:
            t.insert(string)
        
        return [t.search(string) for string in query]


if __name__ == '__main__':
    sol = Solution()
    print(sol.prefixCount(5, 5, ['abracadabra', 'geeksforgeeks', 
      'abracadabra', 'geeks', 'geeksthrill'], ['abr', 'geeks', 'geeksforgeeks', 
         'ge', 'gar']))