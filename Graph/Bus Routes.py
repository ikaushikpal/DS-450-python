# You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

# For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
# You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

# Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

# Example 1:
# Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# Output: 2
# Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.



# Example 2:
# Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
# Output: -1


from typing import List
from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def bfs(self, source, target):
        visited = set()
        visited.add(source)
        queue = deque([(0, source)])

        while queue:
            dist, node = queue.popleft()
            
            if node == target:
                return dist
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((dist + 1, neighbor))
        return -1


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        g = Graph()
        for route in routes:
            for bus in route:
                g.graph[bus].extend(route)
        
        return g.bfs(source, target)


if __name__ == '__main__':
    s = Solution()
    print(s.numBusesToDestination([[1,2,7],[3,6,7]], 1, 6))
    print(s.numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12))
