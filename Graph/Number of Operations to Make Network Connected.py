# There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

# You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

# Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

 

# Example 1:
# Input: n = 4, connections = [[0,1],[0,2],[1,2]]
# Output: 1
# Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.



# Example 2:
# Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
# Output: 2


# Example 3:
# Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
# Output: -1
# Explanation: There are not enough cables.


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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        dsu = Disjoint(n)
        redundantWires = 0

        for u, v in connections:
            if not dsu.union(u, v):
                redundantWires += 1
        
        # check if all computers are already connected
        if min(dsu.array) == -n:
            return 0
        
        connectedComponents = 0
        for i in range(n):
            if i == dsu.find(i)[0]:
                connectedComponents += 1
        
        if connectedComponents -1 <= redundantWires:
            return connectedComponents - 1
        return -1
# Time Complexity: O(V + E)
# Space Complexity: O(V)
# where V is the number of vertices and E is the number of edges
# V = n and E = len(connections)


if __name__ == '__main__':
    sol = Solution()
    print(sol.makeConnected(n = 4, connections = [[0,1],[0,2],[1,2]]))
    print(sol.makeConnected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]))
    print(sol.makeConnected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]))