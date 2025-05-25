# Given a binary tree and a node data called target. Find the minimum time required to burn the complete binary tree if the target is set on fire. It is known that in 1 second all nodes connected to a given node get burned. That is its left child, right child, and parent.
# Note: The tree contains unique values.

# Examples : 

# Example 1:
# Input: root[] = [1,2,3,4,5,N,6,N,N,7,8,N,9,N,N,N,N,N,10],  target = 8
# Output: 7
# Explanation: If leaf with the value 8 is set on fire. 
# After 1 sec: 5 catches fire.
# After 2 sec: 2, 7 catches fire.
# After 3 sec: 4, 1 catches fire.
# After 4 sec: 3 catches fire.
# After 5 sec: 6 catches fire.
# After 6 sec: 9 catches fire.
# After 7 sec: 10 catches fire.
# It takes 7s to burn the complete tree.

# Example 2:
# Input: root[] = [1, 2, 3, 4, 5, N, 7, 8, N, 10], target = 10
# Output: 5
# Explanation: If leaf with the value 10 is set on fire. 
# - After 1 sec: Node 5 catches fire.
# - After 2 sec: Node 2 catches fire.
# - After 3 sec: Nodes 1 and 4 catches fire.
# - After 4 sec: Node 3 and 8 catches fire.
# - After 5 sec: Node 7 catches fire.
# It takes 5s to burn the complete tree.

# Constraints:
# 1 ≤ number of nodes ≤ 10^5
# 1 ≤ node->data ≤ 10^5


from collections import defaultdict, deque


class Solution:
    
    def dfs(self, root, parent, graph):
        if root is None:
            return 
        
        graph[root.data].append(parent.data)
        graph[parent.data].append(root.data)

        self.dfs(root.left, root, graph)
        self.dfs(root.right, root, graph)

    def minTime(self, root, target):
        graph = defaultdict(list)

        self.dfs(root.left, root, graph)
        self.dfs(root.right, root, graph)

        seen = set([target])
        queue = deque([(target, 0)])
        max_dist = 0

        while queue:
            val, dist = queue.popleft()

            max_dist = max(max_dist, dist)

            for neighbour in graph[val]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    queue.append((neighbour, dist + 1))
        return max_dist
# Time Complexity: O(N)
# Space Complexity: O(N)



