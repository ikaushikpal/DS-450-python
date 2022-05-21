# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

 

# Example 1:
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2


# Example 2:
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3


from typing import List


class Solution:
    def dfs(self, isConnected, visited, u):
        for v in range(len(isConnected)):
            if u!=v and not visited[v] and isConnected[u][v]:
                visited[v] = True
                self.dfs(isConnected, visited, v)
                
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ROWS = len(isConnected)
        visited = [False] * ROWS
        countProvinces = 0
        
        for u in range(ROWS):
            if not visited[u]:
                visited[u] = True
                countProvinces += 1
                self.dfs(isConnected, visited, u)
        
        return countProvinces


if __name__ == '__main__':
    sol = Solution()
    print(sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
    print(sol.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))
    print(sol.findCircleNum([[1,1,0,0,0],[1,1,0,0,0],[0,0,1,1,1],[0,0,1,1,1],[0,0,1,1,1]]))