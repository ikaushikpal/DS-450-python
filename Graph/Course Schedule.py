# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

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

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = Graph(numCourses)

        for numCourses in range(numCourses):
            g.addVertice(numCourses)

        for subject1, subject2 in prerequisites:
            g.addEdge(subject1, subject2)
        
        return not g.isCycle()


if __name__ == '__main__':
    sol = Solution()
    print(sol.canFinish(numCourses = 2, prerequisites = [[1,0]]))
    print(sol.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]))
    print(sol.canFinish(numCourses = 1, prerequisites = []))