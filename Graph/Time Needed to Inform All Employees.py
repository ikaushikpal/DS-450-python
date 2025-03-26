# A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

# Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.

# The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

# The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

# Return the number of minutes needed to inform all the employees about the urgent news.

 

# Example 1:
# Input: n = 1, headID = 0, manager = [-1], informTime = [0]
# Output: 0
# Explanation: The head of the company is the only employee in the company.


# Example 2:
# Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
# Output: 1
# Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
# The tree structure of the employees in the company is shown.


from collections import defaultdict
from typing import List


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
    
    def dfs(self, u, t, visited):
        visited.add(u)
        
        for v, w in self.graph[u]:
            if v not in visited:
                self.dfs(v, t+w, visited)
        self.time = max(self.time, t)
        
    def find_total_time(self, src):
        self.time = 0
        visited = set()
        self.dfs(src, 0, visited)
        return self.time


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = Graph()
        for i in range(n):
            if manager[i] == -1:
                continue
            g.add_edge(manager[i], i, informTime[manager[i]])
        
        print(g.graph)
        return g.find_total_time(headID)
# Time Complexity : O(n)
# Space Complexity : O(n)


if __name__ == "__main__":
    sol = Solution()
    print(sol.numOfMinutes( n = 15, 
                            headID = 0,
                            manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6],
                            informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]))
    
    print(sol.numOfMinutes( n = 6,
                            headID = 2,
                            manager = [2,2,-1,2,2,2],
                            informTime = [0,0,1,0,0,0]))

    print(sol.numOfMinutes( n = 7,
                            headID = 6,
                            manager = [1,2,3,4,5,6,-1],
                            informTime = [0,6,5,4,3,2,1]))

    print(sol.numOfMinutes(7,
                            6,
                            [1,2,3,4,5,6,-1],
                            [0,6,5,4,3,2,1]))