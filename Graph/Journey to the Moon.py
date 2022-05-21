from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def findComponentLength(self, u, visited):
        visited[u] = True
        count = 1

        for v in self.graph[u]:
            if not visited[v]:
                count += self.findComponentLength(v, visited)
        
        return count


class Solution:
    def journeyToMoon(self, n, astronaut):
        g = Graph()
        for a, b in astronaut:
            g.addEdge(a, b)
            g.addEdge(b, a)

        # total ways to connect all the astronauts
        # if all are belong to different country
        totalWays = n * (n -1) // 2
        visited = defaultdict(bool)

        for i in range(n):
            if not visited[i]:
                compSize = g.findComponentLength(i, visited)
                if compSize > 1:
                    totalWays -= (compSize * (compSize-1) // 2)
        
        return totalWays

def journeyToMoon(self, n, astronaut):
    return Solution().journeyToMoon(n, astronaut)
# Time Complexity: O(N)
# Space Complexity: O(N)


if __name__ == "__main__":
    print(journeyToMoon(5, [[0, 1], [2, 3], [0, 4]]))
    print(journeyToMoon(4, [[0, 2]]))
    print(journeyToMoon(10, [[0, 2],
                            [1, 8],
                            [1, 4],
                            [2, 8],
                            [2, 6],
                            [3, 5],
                            [6, 9],]))