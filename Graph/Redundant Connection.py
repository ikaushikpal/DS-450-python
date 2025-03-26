# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

# Example 1:
# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]


# Example 2:
# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]


from typing import List


class Disjoint:
    def __init__(self, n=0):
        self.n = n
        self.array = [-1] * self.n

    def add(self):
        self.array.append(-1)
        self.n += 1

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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        d = Disjoint(len(edges))
        for u, v in edges:
            if not d.union(u, v):
                return [u, v]
        return []
# Time Complexity: O(n)
# Space Complexity: O(n)
# where n is the number of nodes in the graph. n = len(edges) + 1
# We use a Disjoint data structure to keep track of the parent of each node.
# The space complexity is due to the Disjoint data structure.


if __name__ == '__main__':
    s = Solution()
    print(s.findRedundantConnection([[1,2],[1,3],[2,3]]))
    print(s.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))