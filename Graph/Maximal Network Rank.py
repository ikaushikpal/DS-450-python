# There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

# The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

# The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

# Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

 
# Example 1:
# Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
# Output: 4
# Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.


# Example 2:
# Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
# Output: 5
# Explanation: There are 5 roads that are connected to cities 1 or 2.


# Example 3:
# Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
# Output: 5
# Explanation: The network rank of 2 and 5 is 5. Notice that all the cities do not have to be connected.


from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adjMatrix = [[False]*n for _ in range(n)]
        degree = [0] * n
        bucket = {}
        # first is highest degree and second is second highest degree
        first = second = 0

        for u, v in roads:
            adjMatrix[u][v] = True
            adjMatrix[v][u] = True
            degree[u] += 1
            degree[v] += 1
            
        for i in range(n):
            if degree[i] not in bucket:
                bucket[degree[i]] = [i]
            else:
                bucket[degree[i]].append(i)
            
            if degree[i] > first:
                second = first
                first = degree[i]
            
            elif degree[i] > second:
                second = degree[i]
        
        # CASE 1:
        # only one element is present at highest degree
        if len(bucket[first]) == 1:
            u = bucket[first][0]
            # pick element from next degree
            for v in bucket[second]:
                # no edge from city[a] to city[b]
                if adjMatrix[u][v] == False:
                    return first + second
            return first + second - 1

        # CASE 2:
        # do nested loop and find there is any two cities 
        # where those two are not connected
        else:
            for u in bucket[first]:
                for v in bucket[first]:
                    if u == v: continue

                    if adjMatrix[u][v] == False:
                        return 2 * first
            return 2 * first - 1
# Time Complexity : O(N * N)
# Space Complexity : O(N * N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximalNetworkRank(n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]))