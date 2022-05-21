# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

# Example 2:

# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

# Example 3:

# Input: numCourses = 1, prerequisites = []
# Output: [0]


from typing import List
from collections import defaultdict


class Graph:
    def __init__(self, n) -> None:
        self.graph = {}
        self.n = n
    
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def addVertice(self, u):
        self.graph[u] = []

    def dfs(self, u, visited, recursionStack):
        visited[u] = True
        recursionStack[u] = True

        for v in self.graph[u]:
            if not visited[v]:
                if self.dfs(v, visited, recursionStack):
                    return True
            
            if recursionStack[v]:
                return True
        
        recursionStack[u] = False
        return False

    def isCycle(self):
        visited = defaultdict(bool)
        recursionStack = defaultdict(bool)

        for u in range(self.n):
            if not visited[u]:
                if self.dfs(u, visited, recursionStack):
                    return True
        return False

    def topsort(self, u, visited, ordering):
        visited[u] = True

        for v in self.graph[u]:
            if not visited[v]:
                self.topsort(v, visited, ordering)
        
        ordering.append(u)

    def topologicalOrdering(self):
        visited = defaultdict(bool)
        ordering = []

        for u in range(self.n):
            if not visited[u]:
                self.topsort(u, visited, ordering)
        return ordering


class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = Graph(numCourses)

        for numCourses in range(numCourses):
            g.addVertice(numCourses)

        for subject1, subject2 in prerequisites:
            g.addEdge(subject1, subject2)
        
        if g.isCycle():
            return []
        
        return g.topologicalOrdering()


if __name__ == '__main__':
    sol = Solution()
    print(sol.findOrder(numCourses = 2, prerequisites = [[1,0]]))
    print(sol.findOrder(numCourses = 2, prerequisites = [[0, 1]]))
    print(sol.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))
    print(sol.findOrder(numCourses = 1, prerequisites = []))
    print(sol.findOrder(numCourses = 2, prerequisites = [[1,0],[0,1]]))