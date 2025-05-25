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


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        graph = defaultdict(list)

        for busId, route in enumerate(routes):
            for busStop in route:
                graph[busStop].append(busId)
        
        if source not in graph or target not in graph:
            return -1
        
        queue = deque([(source, 0)])
        bus = set()
        stop = set()

        while queue:
            stoppage, cost = queue.popleft()

            for busId in graph[stoppage]:
                if busId in bus:
                    continue
                
                bus.add(busId)

                for busStop in routes[busId]:
                    if busStop in stop:
                        continue
                    
                    if busStop == target:
                        return cost + 1 
                    
                    queue.append((busStop, cost + 1))
                    stop.add(busStop)
        return -1
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
        

if __name__ == '__main__':
    s = Solution()
    print(s.numBusesToDestination([[1,2,7],[3,6,7]], 1, 6))
    print(s.numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12))
