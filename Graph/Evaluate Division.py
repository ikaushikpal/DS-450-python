# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

# Return the answers to all queries. If a single answer cannot be determined, return -1.0.

# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

 

# Example 1:

# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation: 
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]


# Example 2:
# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]


# Example 3:
# Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]


from collections import defaultdict, deque
from typing import List


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v, weight):
        self.graph[u].append((v, weight))
    
    def isValid(self, vertex):
        return vertex in self.graph

    def calcDiv(self, src, dest):
        queue = deque([(src, 1.0)])
        visited = defaultdict(bool)

        while queue:
            curr, product = queue.popleft()
            visited[curr] = True

            if curr == dest:
                return product

            for neighbour, weight in self.graph[curr]:
                if not visited[neighbour]:
                    queue.append((neighbour, product * weight)) 

        return -1.0


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = Graph()
        
        for (op1, op2), val in zip(equations, values):
            g.addEdge(op1, op2, val)
            g.addEdge(op2, op1, 1/val)
        
        ans = []
        for query in queries:
            op1, op2 = query
            if g.isValid(op1) and g.isValid(op2):
                if op1 == op2:
                    ans.append(1.0)
                else:
                    ans.append(g.calcDiv(op1, op2))
            else:
                ans.append(-1.0)

        return ans
# Time Complexity: O(q*(V+E))
# Space Complexity: O(V+E)
# where V is number of vertices and E is number of edges
# V = unique variables in equations and E = 2 * number of equations
# Q is number of queries


if __name__ == '__main__':
    equations = [["a","b"],["b","c"]]
    values = [2.0,3.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    print(Solution().calcEquation(equations, values, queries))

    equations = [["a","b"],["b","c"],["bc","cd"]]
    values = [1.5,2.5,5.0]
    queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    print(Solution().calcEquation(equations, values, queries))