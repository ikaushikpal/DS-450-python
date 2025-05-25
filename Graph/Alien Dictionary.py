# A new alien language uses the English alphabet, but the order of letters is unknown. You are given a list of words[] from the alien language’s dictionary, where the words are claimed to be sorted lexicographically according to the language’s rules.

# Your task is to determine the correct order of letters in this alien language based on the given words. If the order is valid, return a string containing the unique letters in lexicographically increasing order as per the new language's rules. If there are multiple valid orders, return any one of them.

# However, if the given arrangement of words is inconsistent with any possible letter ordering, return an empty string ("").

# A string a is lexicographically smaller than a string b if, at the first position where they differ, the character in a appears earlier in the alien language than the corresponding character in b. If all characters in the shorter word match the beginning of the longer word, the shorter word is considered smaller.

# Note: Your implementation will be tested using a driver code. It will print true if your returned order correctly follows the alien language’s lexicographic rules; otherwise, it will print false.

# Examples:
# Input: words[] = ["baa", "abcd", "abca", "cab", "cad"]
# Output: true
# Explanation: A possible corrct order of letters in the alien dictionary is "bdac".
# The pair "baa" and "abcd" suggests 'b' appears before 'a' in the alien dictionary.
# The pair "abcd" and "abca" suggests 'd' appears before 'a' in the alien dictionary.
# The pair "abca" and "cab" suggests 'a' appears before 'c' in the alien dictionary.
# The pair "cab" and "cad" suggests 'b' appears before 'd' in the alien dictionary.
# So, 'b' → 'd' → 'a' → 'c' is a valid ordering.

# Input: words[] = ["caa", "aaa", "aab"]
# Output: true
# Explanation: A possible corrct order of letters in the alien dictionary is "cab".
# The pair "caa" and "aaa" suggests 'c' appears before 'a'.
# The pair "aaa" and "aab" suggests 'a' appear before 'b' in the alien dictionary. 
# So, 'c' → 'a' → 'b' is a valid ordering.

# Input: words[] = ["ab", "cd", "ef", "ad"]
# Output: ""
# Explanation: No valid ordering of letters is possible.
# The pair "ab" and "ef" suggests "a" appears before "e".
# The pair "ef" and "ad" suggests "e" appears before "a", which contradicts the ordering rules.

# Constraints:
# 1 ≤ words.length ≤ 500
# 1 ≤ words[i].length ≤ 100
# words[i] consists only of lowercase English letters.


from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = {}
    
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, vertex, visited, order):
        visited[vertex] = True
        
        for neighbour in self.graph[vertex]:
            if visited[neighbour] == False:
                self.dfs(neighbour, visited, order)
                
        order.append(vertex)

    def topologicalSort(self):
        visited = defaultdict(bool)
        order = []

        for vertex in list(self.graph):
            if visited[vertex] == False:
                self.dfs(vertex, visited, order)
        
        return order
    
    def hasCycleUtil(self, node, visited, stack):
        visited.add(node)
        stack.append(node)

        for neighbour in self.graph[node]:
            if neighbour not in visited:
                if self.hasCycleUtil(neighbour, visited, stack):
                    return True
            elif neighbour in stack:
                return True
        
        stack.pop()
        return False
    
    def hasCycle(self):
        visited = set()
        stack = []

        for node in self.graph:
            if node not in visited:
                if self.hasCycleUtil(node, visited, stack):
                    return True
        return False
    
class Solution:
    def findOrder(words):
        g = Graph()
        N = len(words)

        for word in words:
            for char in word:
                if char not in g.graph:
                    g.graph[char] = []
        
        for i in range(N-1):
            word1, word2 = words[i], words[i + 1]

            
            min_len = min(len(word1), len(word2))
            mismatched = False
            for j in range(min_len):
                if word1[j] != word2[j]:
                    mismatched = True
                    g.addEdge(word1[j], word2[j])
                    break
                    
            # if word1 is not a prefix of word2
            if not mismatched and len(word2) < len(word1):
                return ""
            
        if g.hasCycle():
            return ""
        
        order = g.topologicalSort()
        return ''.join(order)[::-1]
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)


if __name__ == '__main__':
    print(Solution.findOrder(['baa', "abcd","abca","cab","cad"]))
    print(Solution.findOrder(['caa', "aaa", "aab"]))
    print(Solution.findOrder(['ab', "cd", "ef", "ad"]))