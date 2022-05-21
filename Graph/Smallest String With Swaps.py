# You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

# You can swap the characters at any pair of indices in the given pairs any number of times.

# Return the lexicographically smallest string that s can be changed to after using the swaps.

 

# Example 1:

# Input: s = "dcab", pairs = [[0,3],[1,2]]
# Output: "bacd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[1] and s[2], s = "bacd"



# Example 2:

# Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# Output: "abcd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[0] and s[2], s = "acbd"
# Swap s[1] and s[2], s = "abcd"



# Example 3:

# Input: s = "cba", pairs = [[0,1],[1,2]]
# Output: "abc"
# Explaination: 
# Swap s[0] and s[1], s = "bca"
# Swap s[1] and s[2], s = "bac"
# Swap s[0] and s[1], s = "abc"


from collections import defaultdict
from typing import List


class Disjoint:
    def __init__(self, n=0):
        self.n = n
        self.array = [-1] * self.n

    def add(self):
        self.array.append(-1)

    def find(self, n):
        if self.array[n] < 0:
            return (n,  -self.array[n])
        result = self.find(self.array[n])
        self.array[n] = result[0]
        return result
    
    def union(self, set1, set2):
        parent_of_set1, rank_of_set1 = self.find(set1)
        parent_of_set2, rank_of_set2 = self.find(set2)

        if parent_of_set1 == parent_of_set2:
            return False

        if rank_of_set1 > rank_of_set2:
            self.array[parent_of_set1] += self.array[parent_of_set2]
            self.array[parent_of_set2] = parent_of_set1
            
        else:
            self.array[parent_of_set2] += self.array[parent_of_set1]
            self.array[parent_of_set1] = parent_of_set2
        return True


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        ds = Disjoint(len(s))
        for pair in pairs:
            ds.union(pair[0], pair[1])
        
        parent = defaultdict(list)
        for i in range(len(s)):
            parent[ds.find(i)[0]].append(i)
        
        res = list(s)
        for p in parent:
            indices = parent[p]
            values = [res[i] for i in indices]
            indices.sort()
            values.sort()

            for i in range(len(values)):
                res[indices[i]] = values[i]
        
        return ''.join(res)

        
if __name__ == '__main__':
    sol = Solution()
    print(sol.smallestStringWithSwaps("dcab", [[0,3],[1,2], [0,2]]))
    print(sol.smallestStringWithSwaps(s = "cba", pairs = [[0,1],[1,2]]))
    print(sol.smallestStringWithSwaps("zdcyxbwa", [[0,3],[4,6],[3,4],[1,7],[2,5],[5,7]]))

