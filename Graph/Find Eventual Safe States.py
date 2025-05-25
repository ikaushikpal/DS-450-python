# There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

# A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node.

# Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

 

# Example 1:
# Illustration of graph
# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]
# Explanation: The given graph is shown above.
# Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
# Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.



# Example 2:
# Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
# Output: [4]
# Explanation:
# Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.


from typing import List


class Solution:
    def dfs(self, vertex, visited, stack, safe, graph):
        visited[vertex] = True
        stack[vertex] = True

        # initially vertex is not safe node
        safe[vertex] = False

        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                if self.dfs(neighbour, visited, stack, safe, graph):
                    return True
            
            # have found cycle
            if stack[neighbour]:
                return True

        stack[vertex] = False

        # at end will only come is no cycle is detected then vertex is safe
        safe[vertex] = True
        return False   

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        visited = [False] * V # mark if vertex is visited
        stack = [False] * V # mark if vertex is in stack, for cycle detection
        safe = [False] * V # mark if vertex is safe
        # safe node is a node that has no outgoing edge

        for i in range(V):
            if not visited[i]:
                self.dfs(i, visited, stack, safe, graph)
        
        ans = []
        for i, isSafe in enumerate(safe):
            if isSafe:
                ans.append(i)
        return ans
# Time Complexity : O(V + E)
# Space Complexity : O(V)


if __name__ == '__main__':
    sol = Solution()
    print(sol.eventualSafeNodes(graph = [[1,2],[2,3],[5],[0],[5],[],[]]))
    print(sol.eventualSafeNodes(graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]))