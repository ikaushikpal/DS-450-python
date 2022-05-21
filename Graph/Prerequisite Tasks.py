# There are a total of N tasks, labeled from 0 to N-1. Some tasks may have prerequisites, for example to do task 0 you have to first complete task 1, which is expressed as a pair: [0, 1]
# Given the total number of tasks N and a list of prerequisite pairs P, find if it is possible to finish all tasks.


# Example 1:
# Input: 
# N = 4, P = 3
# prerequisites = {{1,0},{2,1},{3,2}}
# Output:
# Yes
# Explanation:
# To do task 1 you should have completed
# task 0, and to do task 2 you should 
# have finished task 1, and to do task 3 you 
# should have finished task 2. So it is possible.


# Example 2:
# Input:
# N = 2, P = 2
# prerequisites = {{1,0},{0,1}}
# Output:
# No
# Explanation:
# To do task 1 you should have completed
# task 0, and to do task 0 you should
# have finished task 1. So it is impossible.


from collections import defaultdict
import sys


sys.setrecursionlimit(10**5)
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, starting_vertex, end_vertex):
        self.graph[starting_vertex].append(end_vertex)
    
    def isCyclic(self):
        visitedVertices = defaultdict(bool)
        recursionStack = defaultdict(bool)

        FLAG = False

        for u in list(self.graph):
            if visitedVertices[u] == False:
                if self.dfsUtil(u, visitedVertices, recursionStack):
                    return True
        return False


    def dfsUtil(self, starting_vertex, visitedVertices, recursionStack):
        recursionStack[starting_vertex] = True
        visitedVertices[starting_vertex] = True


        for vertex in self.graph[starting_vertex]:
            if visitedVertices[vertex] == False:
                if self.dfsUtil(vertex, visitedVertices, recursionStack):
                    return True
                    
            if recursionStack[vertex] == True:
                return True
        
        recursionStack[starting_vertex] = False
        return False
        
        
class Solution:
    def isPossible(self, N, prerequisites):
        g = Graph()
        for u, v in prerequisites:
            g.addEdge(u, v)
        
        return not g.isCyclic()