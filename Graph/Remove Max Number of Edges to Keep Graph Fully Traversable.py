# Alice and Bob have an undirected graph of n nodes and 3 types of edges:

# Type 1: Can be traversed by Alice only.
# Type 2: Can be traversed by Bob only.
# Type 3: Can by traversed by both Alice and Bob.
# Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

# Return the maximum number of edges you can remove, or return -1 if it's impossible for the graph to be fully traversed by Alice and Bob.

 

# Example 1:
# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
# Output: 2
# Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.



# Example 2:
# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
# Output: 0
# Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.



# Example 3:
# Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
# Output: -1
# Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.


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
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = Disjoint(n+1)
        bob = Disjoint(n+1)
        canRemoveEdges = 0

        # edges= [type, u, v]
        for typeofEdge, u, v in edges:
            # Type 3: Can by traversed by both Alice and Bob.
            if typeofEdge == 3 and (not alice.union(u, v) or not bob.union(u, v)):
                # if already connected two vertices
                    canRemoveEdges += 1
        
        # rest types
        # Type 1: Can be traversed by Alice only.
        # Type 2: Can be traversed by Bob only.
        for typeofEdge, u, v in edges:
            if typeofEdge == 1 and not alice.union(u, v):
                canRemoveEdges += 1
            
            if typeofEdge == 2 and not bob.union(u, v):
                canRemoveEdges += 1

        # checking if alice can traverse all vertices
        if min(alice.array) != -n:
            return -1

        # checking same for bob
        if min(bob.array) != -n:
            return -1
        
        return canRemoveEdges
# Time Complexity : O(M)
# Space Complexity : O(N)
# where M is the count of all edges in graph
# N is total number of vertices


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]))
    print(sol.maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]))
    print(sol.maxNumEdgesToRemove(n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]))